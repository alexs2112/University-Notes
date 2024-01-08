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

#include "constants.h"

#ifndef CTFILE
#define CTFILE="./ciphertext2a"
#endif

#ifndef ORACLE
#define ORACLE="/usr/bin/oracle2a"
#endif

unsigned char query_oracle(unsigned char ctbuf[], size_t ctlen, int ifd[2], int ofd[2])
{
    int status;
    pid_t pid = fork();
    if (pid == 0)
    {
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
    }
    else
    {
	// tell the oracle how long of a ciphertext to expect
        ssize_t bytes_written = write(ofd[1], &ctlen, sizeof(ctlen));
	if (bytes_written != sizeof(ctlen)) error(1, errno, "writing ciphertext length");
	// and then write that many bytes
        bytes_written = write(ofd[1], ctbuf, ctlen);
	if (bytes_written != ctlen) error(1, errno, "writing ciphertext");
	printf("Wrote %lu bytes of ciphertext\n", bytes_written);
	// now fetch the response
        unsigned char result = 0;
        ssize_t bytes_read = read(ifd[0], &result, sizeof(char));
	printf("Oracle responded: %c\n", result);
	// reap the execl'd child before we return
        waitpid(pid, &status, 0);
        return result;
    }
}

int main(int argc, char * argv[])
{
        ssize_t bytes_read;
        unsigned char ctbuf[IVLEN + MACLEN + CTLEN] = { '\0' };
        unsigned char ptbuf[IVLEN + MACLEN + CTLEN] = { '\0' };

        // read the ciphertext from a file
        int ctfd = open(CTFILE, O_RDONLY);
        if (ctfd == -1) error(1, errno, "opening %s", CTFILE);
        bytes_read = read(ctfd, ctbuf, IVLEN + MACLEN + CTLEN);
        if (bytes_read <= IVLEN + MACLEN) error(1, errno, "ciphertext too short");
        close(ctfd);

        // create some pipes for directional communication with the child process
        int ifd[2], ofd[2];
        if (pipe(ifd) != 0) error(1, errno, "creating input pipe");
        if (pipe(ofd) != 0) error(1, errno, "creating output pipe");

        // loop till we're done...
        size_t ctlen = bytes_read;
        size_t ptlen = 0;

        bool done = false;
        while (!done) {
	    // perturb the ciphertext in some fancy way
            query_oracle(ctbuf, ctlen, ifd, ofd);
            done = true;
        }

	// clean up the pipes
        close(ofd[0]);
        close(ofd[1]);
        close(ifd[0]);
        close(ifd[1]);

        return 0;
}
