#include <cstdlib>
#include <cstdio>
#include <cerrno>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/prctl.h>
#include <signal.h>
#include <error.h>
#include <pthread.h>

#include "constants.h"

// xorbuf is to be xored with the second last block of cipher text before passing it to the oracle
unsigned char query_oracle(unsigned char ctbuf[], size_t ctlen, int ifd[2], int ofd[2], unsigned int xorbuf[16]) {
    int status;
    pid_t pid = fork();
    if (pid == 0) {
        // this is the child; it will simply exec into our desired
        // oracle program, but first it replaces stdin and stdout with
        // the provided pipes so that the parent can both write to
        // and read from it
        dup2(ofd[0], STDIN_FILENO);
        dup2(ifd[1], STDOUT_FILENO);

        // ask kernel to deliver SIGTERM in case the parent dies
        prctl(PR_SET_PDEATHSIG, SIGTERM);

        // run the oracle
        execl(ORACLE, ORACLE, (char *)NULL);
        // we'll never get here, unless execl fails for some reason
        perror("execl");
        exit(1);
    } else {
        // tell the oracle how long of a ciphertext to expect
        ssize_t bytes_written = write(ofd[1], &ctlen, sizeof(ctlen));
        if (bytes_written != sizeof(ctlen)) error(1, errno, "writing ciphertext length");

        // and then write that many bytes after xoring the second last block of ciphertext
        unsigned char temp[16];
        unsigned char last[16];
        for (short i = 0; i < 16; i++) {
            temp[i] = (unsigned char)((unsigned int)(ctbuf[ctlen - 32 + i]) ^ xorbuf[i]);
            last[i] = ctbuf[ctlen - 16 + i];
        }
        bytes_written = write(ofd[1], ctbuf, ctlen - 32);
        bytes_written += write(ofd[1], temp, 16);
        bytes_written += write(ofd[1], last, 16);

        if (bytes_written != ctlen) error(1, errno, "writing ciphertext");
        //printf("Wrote %lu bytes of ciphertext\n", bytes_written);

        // now fetch the response
        unsigned char result = 0;
        ssize_t bytes_read = read(ifd[0], &result, sizeof(char));
        //printf("Oracle responded: %c\n", result);

        // reap the execl'd child before we return
        waitpid(pid, &status, 0);
        return result;
    }
}

// Decrypt a single 16 byte block of the ciphertext
// Params:
// - ctbuf: The full ciphertext
// - ctlen: The length of the ciphertext
// - ifd: input pipe
// - ofd: output pipe
// - last_block: if this is decrypting the last block of the plaintext (will include padding)
// - ptbuf: The 16 byte plaintext array that will be modified
struct decrypt_params {
    unsigned char * ctbuf;
    size_t ctlen;
    bool last_block;
    unsigned char * ptbuf;
};

void * decrypt_block(void *params) {
    decrypt_params p = ((decrypt_params *)params)[0];
    unsigned int working[16] = { 0 };
    unsigned char c;
    int i, b, pt;

    // create some pipes for directional communication with the child process
    int ifd[2], ofd[2];
    if (pipe(ifd) != 0) error(1, errno, "creating input pipe");
    if (pipe(ofd) != 0) error(1, errno, "creating output pipe");

    for (b = 15; b >= 0; b--) {
        for (i = 15; i > b; i--)
            working[i] = p.ptbuf[i] ^ (16 - b);

        for (i = 1; i <= 255; i++) {
            working[b] = i;
            c = query_oracle(p.ctbuf, p.ctlen, ifd, ofd, working);
            if (c == 'M') {
                pt = i ^ (16 - b);
                p.ptbuf[b] = (unsigned char)pt;

                // The last padding byte of the last block tells us what the last n bytes are
                if (p.last_block && b == 15) {
                    int k = 14;
                    for (int j = 0; j < pt - 1; j++) {
                        p.ptbuf[k] = (unsigned char)pt;
                        k--;
                    }
                    b = 15 - pt + 1;
                }
                break;
            } else if (i >= 255) { error(1, errno, "ran out of bytes to test"); }
        }
    }

    for (i = 0; i < 16; i++) {
        printf("%c", p.ptbuf[i]);
    }
    printf("\n");

    // clean up the pipes
    close(ofd[0]);
    close(ofd[1]);
    close(ifd[0]);
    close(ifd[1]);

    return NULL;
}

int main(int argc, char * argv[]) {
        ssize_t bytes_read;
        unsigned char ctbuf[IVLEN + MACLEN + CTLEN] = { '\0' };
        unsigned char ptbuf[IVLEN + MACLEN + CTLEN] = { '\0' };

        // read the ciphertext from a file
        int ctfd = open(CTFILE, O_RDONLY);
        if (ctfd == -1) error(1, errno, "opening %s", CTFILE);
        bytes_read = read(ctfd, ctbuf, IVLEN + MACLEN + CTLEN);
        if (bytes_read <= IVLEN + MACLEN) error(1, errno, "ciphertext too short");
        close(ctfd);

        // loop till we're done...
        size_t ctlen = bytes_read;
        size_t ctrem = ctlen;
        size_t ptlen = 0;

        bool done = false;
        int block_start = ctlen - 16;
        int num_threads = (ctlen - IVLEN - MACLEN) / 16;
        pthread_t threads[num_threads];
        for (int i = 0; i < num_threads; i++) {
            // set up the params for each thread
            decrypt_params p;
            p.ctbuf = ctbuf;
            p.ctlen = ctrem;
            p.last_block = (i == 0);
            p.ptbuf = &ptbuf[block_start];
            pthread_create(&threads[i], NULL, decrypt_block, (void *)&p);

            ctrem -= 16;
            block_start -= 16;
        }

        for (int i = 0; i < num_threads; i++)
            pthread_join(threads[i], NULL);

        // print the plaintext minus the padding
        int padlen = (unsigned short)ptbuf[IVLEN + MACLEN + ctlen - 17];
        for (int i = IVLEN + MACLEN; i < ctlen - padlen; i++)
            printf("%c", ptbuf[i]);
        printf("\n");

        return 0;
}
