#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include <errno.h>
#include <error.h>
#include <unistd.h>

#include <sys/wait.h>
#include <sys/prctl.h>

int cheech(const char * cheech)
{
    int ifd[2], ofd[2];
    if (pipe(ifd) != 0)
    {
        error(1, errno, "creating input pipe");
    }
    if (pipe(ofd) != 0)
    {
        error(1, errno, "creating output pipe");
    }

    int status;
    pid_t pid = fork();
    if (pid == 0)
    {
        dup2(ofd[0], STDIN_FILENO);
        dup2(ifd[1], STDOUT_FILENO);
        prctl(PR_SET_PDEATHSIG, SIGTERM);
        execl("/usr/bin/chong", "/usr/bin/chong", (char *) NULL);
        exit(1);
    } else {
        // how long is the payload?
        size_t payload_len = strlen(cheech)+1000; // +1 for the NUL terminator
        // tell server how many bytes to expect
        size_t bytes_written = write(ofd[1], &payload_len, sizeof(payload_len));
        // then write that many bytes
        bytes_written = write(ofd[1], cheech, payload_len);

        // allocate a buffer for the chong
        char chong[payload_len];
        // read the chong
        size_t bytes_read = read(ifd[0], chong, payload_len);
        waitpid(pid, &status, 0);

        int success = strcmp(cheech, chong);
        // check if cheech matches chong
        printf("Cheech =?= chong: %u\n", !success);

        for (int i = 0; i < sizeof(chong); i++) {
            printf("%c", chong[i]);
        }
        return success;
    }
}

int main(int argc, char **argv)
{
    if (argc < 2)
    {
        error(1, 0, "Usage: cheech PAYLOAD");
    }
    return cheech(argv[1]);
}
