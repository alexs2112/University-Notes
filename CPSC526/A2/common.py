import os, pathlib, sys, socket, subprocess

MAX_LINE_LENGTH = 2**30
MAX_READ_BUFF_SIZE = 4096

FILE_SIZE_BYTES = 16        # Max file size stored as a number to send to the receiver
FILE_BUFFER_SIZE = 1448     # For some reason if the server and client are on different computers,
                            # file transfer only does 1448 bytes before printing the rest to stdout
                            # I literally don't understand this at all, 32 kb works fine on the same linux machine

def get_secret():
    # check environment variable SECRET526
    try:
        return os.environ["SECRET526"]
    except Exception:
        pass

    # check the source directory for .secret526 file
    secret_fname = pathlib.Path(__file__).parent / ".secret526"
    try:
        with secret_fname.open() as fp:
            return fp.readline().strip()
    except Exception:
        pass

    print("No configured secret found.")
    print("Either hardcode one in common.py,")
    print("or use environment variable SECRET526,")
    print("or save one in", secret_fname)
    sys.exit(-1)

# Format the output of subprocess
def subprocess_output(output):
    stdout = output.stdout.decode("ascii", "ignore").split("\n")
    stderr = output.stderr.decode("ascii", "ignore").split("\n")
    all = stdout + stderr
    all = [line for line in all if len(line)]
    return all

# Use the sha256sum command to get the hash of a file
def sha_files(files):
    cmd_out = subprocess.run(["sha256sum"] + files, capture_output=True)
    cmd_out = subprocess_output(cmd_out)
    output = []

    # sha256sum also lists filenames, get rid of those and only return hashes
    for line in cmd_out:
        if line.endswith("No such file or directory"):
            output.append("No such file or directory")
        else:
            output.append(line.split()[0])
    return output

class Receiver:
    def __init__(self, socket: socket.socket):
        self.socket = socket
        self.buffer = ""

    def receive(self):
        while True:
            # Check if we have a full line in buffer
            first_line, sep, rest = self.buffer.partition('\n')
            if sep:
                # Full line found, remove it from buffer
                self.buffer = rest
                if len(first_line) > MAX_LINE_LENGTH:
                    raise ConnectionError("Line too long")
                return first_line

            if len(self.buffer) > MAX_LINE_LENGTH:
                raise ConnectionError("line too long")

            # Read more data into the buffer
            part = self.socket.recv(MAX_READ_BUFF_SIZE)
            if len(part) == 0:
                self.socket.close()
                raise ConnectionError("Unexpected client disconnect")
            self.buffer += part.decode('ascii', "ignore")

class FileTransfer:
    def __init__(self, socket: socket.socket):
        self.socket = socket
        self.buffer = None

    def send_file(self, filepath: str):
        # First send the length of the file to the client
        size = os.path.getsize(filepath)
        size_b = size.to_bytes(FILE_SIZE_BYTES, 'little')
        self.socket.sendall(size_b)

        # Read the file and send it across the socket chunk by chunk
        with open(filepath, "rb") as file:
            while True:
                self.buffer = file.read(FILE_BUFFER_SIZE)
                if not self.buffer:
                    break
                self.socket.sendall(self.buffer)
    
    def receive_file(self, filepath: str):
        # Read the length of the file to receive
        size_b = self.socket.recv(FILE_SIZE_BYTES)
        rem_file_size = int.from_bytes(size_b, 'little')

        # Read the bytes and write them chunk by chunk into a file
        with open(filepath, "wb") as file:
            while True:
                # Determine the size of the next chunk and read it
                chunk_size = min(FILE_BUFFER_SIZE, rem_file_size)
                rem_file_size -= chunk_size
                self.buffer = self.socket.recv(chunk_size)

                # Write the chunk to the file
                if not self.buffer:
                    break
                file.write(self.buffer)

                if (rem_file_size == 0):
                    # No more file remaining, end the file transfer
                    break
        return True
