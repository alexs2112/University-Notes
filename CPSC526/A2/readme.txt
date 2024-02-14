### Implementations
 - Correct handshake implementation
 - `cd` works with accessible directories and prints an error message for non-accessible directories
 - `pwd` works
 - `ls` works with unusual file and directory names
 - `cat` works
 - `upload` and `download` work for all files while considering digest
 - All commands work with unusual filenames and dirnames

### To Run:
 - Server: `SECRET526=111111 python server.py -d <port>`
 - Client: `SECRET526=111111 python client.py -d <hostname> <port>`
 - `common.py` must be present in the same directory for both `server.py` and `client.py`
