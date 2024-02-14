import argparse, socket, subprocess
import random, string, hashlib, shlex
from common import *

class Server:
    def __init__(self):
        self.args = None
        self.socket = None
        self.client = None
        self.client_addr = None
        self.secret = None

    # Parse command line arguments provided to the program
    def parse_args(self):
        parser = argparse.ArgumentParser(
            prog='server',
            description='server that the client connects to')
        parser.add_argument('port', type=int, help='port where server listens')
        parser.add_argument('-d', '--debug', action='store_true',
                            help="enable debugging output")
        self.args = parser.parse_args()
    
    # Check for either env SECRET526 or the .secret526 file
    def get_secret(self):
        self.secret = get_secret()
        self.debug(f"Using {self.secret=}")

    # Open a listening socket, port defined in args
    def open_socket(self):
        host = socket.gethostname()
        port = self.args.port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((host, port))
        self.socket.listen(1)
        self.debug(f"Starting server on port {port}")
        self.debug(f"Connect with:")
        self.debug(f"  SECRET526={self.secret} ./client.py {host} {port}")
        self.debug(f"  nc {host} {port}")
    
    # Accept client connection
    def accept_client(self):
        (self.client, self.client_addr) = self.socket.accept()
        self.debug(f"Client connected from {self.client_addr}")

    # Perform the handshake with the client
    def handshake(self, recv):
        # Generate a random alphanumeric string of length 16 and send it to the client
        self.debug("Performing handshake")
        challenge = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        self.send(challenge)

        # Calculate the expected digest returned from the client
        expected = self.secret + challenge
        expected = hashlib.sha256(expected.encode('utf-8')).hexdigest()

        # Receive the actual digest from the client and ensure they are the same
        actual = recv.receive()
        self.debug(f"Expected Digest: {expected}")
        self.debug(f"Actual Digest:   {actual}")

        if expected != actual:
            raise ConnectionRefusedError("Handshake did not match")

    # Minor formatting for sending a string across an open socket to the client
    def send(self, msg):
        msg += "\n"
        self.client.sendall(msg.encode("ascii", "ignore"))

    # Main client service loop
    def serve_client(self):
        recv = Receiver(self.client)
        try:
            self.handshake(recv)

            while True:
                cmd = recv.receive()
                res = self.execute_command(cmd)
                for line in res + ["---"]:
                    self.send(line)
        except ConnectionError:
            self.debug(f"Client disconnected from {self.client_addr}")
            self.client = None
            self.client_addr = None
            pass

    # Execute the command provided by the client
    def execute_command(self, cmd):
        self.debug(f"Executing command: {cmd}")
        try:
            args = shlex.split(cmd)
        except ValueError:
            return [ "[ERROR] Error in command format" ]

        if not args:
            return []
        
        elif args[0] == "pwd":
            return [ f"{os.getcwd()}" ]
        
        elif args[0] == "ls" or args[0] == "cat":
            output = subprocess.run(args, capture_output=True)
            return subprocess_output(output)

        elif args[0] == "cd":
            if len(args) > 1:
                try:
                    os.chdir(args[1])
                except FileNotFoundError:
                    return [ "[ERROR] No such file or directory"]
                except NotADirectoryError:
                    return [ "[ERROR] Not a directory" ]
            else:
                os.chdir("~")
            return [ os.getcwd() ]
        
        elif args[0] == "sha256":
            return sha_files(args[1:])

        elif args[0] == "upload":
            output = self.upload_file(args[1])
            return output
    
        elif args[0] == "download":
            output = self.download_file(args[1])
            return output

        return [ f"[ERROR] Unknown command: {cmd}" ]

    # Have the client upload a file to this server
    def upload_file(self, filepath: str):
        # Receive the file from the client
        self.debug(f"Receiving file: {filepath}")
        ft = FileTransfer(self.client)
        ft.receive_file(os.path.basename(filepath))
        self.debug(f"File transfer complete.")
        return [ f"Uploaded file: '{filepath}'" ]

    # Have the client download a file from this server
    def download_file(self, filepath: str):
        # First ensure that the file actually exists
        if not os.path.isfile(filepath):
            self.debug(f"Could not find file: {filepath}")
            return [ "[ERROR] File not found" ]

        # Send the file to the client
        self.debug(f"Sending file: '{filepath}'")
        ft = FileTransfer(self.client)
        ft.send_file(filepath)
        self.debug(f"File transfer complete.")
        return [ f"Downloaded file: {filepath}" ]

    # When the server closes, close the client connection
    def close_clients(self):
        if self.client == None: return
        self.debug(f"Closing client connection at {self.client_addr}")
        self.client.close()

    # Print debug messages if debug is enabled in args
    def debug(self, *args, **kwargs):
        if not self.args.debug:
            return
        print("[DEBUG] ", *args, **kwargs)

# Main program loop
def main():
    server = Server()
    server.parse_args()
    server.get_secret()
    server.open_socket()

    # Wait for client connection and serve that client
    while True:
        try:
            server.accept_client()
            server.serve_client()
        except KeyboardInterrupt:
            server.debug("Closing server.")
            server.close_clients()
            exit(0)

if __name__ == "__main__":
    main()
