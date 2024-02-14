import argparse, socket, hashlib, shlex
from common import *

class Client:
    def __init__(self):
        self.args = None
        self.socket = None
        self.secret = None

    # Parse command line arguments provided to the program
    def parse_args(self):
        parser = argparse.ArgumentParser(
            prog='client',
            description='client connects to server')
        parser.add_argument('hostname', help='hostname of the server')
        parser.add_argument('port', type=int, help='port where server listens')
        parser.add_argument('-d', '--debug', action='store_true',
                            help="enable debugging output")
        self.args = parser.parse_args()
    
    # Check for either env SECRET526 or the .secret526 file
    def get_secret(self):
        self.secret = get_secret()
        self.debug(f"Using {self.secret=}")

    # Connect to the socket specified in args
    def connect(self):
        print(f"Connecting to {self.args.hostname}:{self.args.port} with {self.secret=}")
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.args.hostname, self.args.port))
        self.debug("Connection succeess")

    # Perform the handshake with the server
    def handshake(self):
        # Receive the challenge from the server
        recv = Receiver(self.socket)
        challenge = recv.receive()
        self.debug(f"Received challenge: {challenge}")

        # Calculate the digest and send to the server
        digest = self.secret + challenge
        digest = hashlib.sha256(digest.encode('utf-8')).hexdigest()
        self.send(digest)
        self.debug(f"Sending digest: {digest}")

    # Minor formatting for sending a string across an open socket
    def send(self, msg):
        msg += "\n"
        self.socket.sendall(msg.encode("ascii", "ignore"))

    # Handle inputted user command, send to the server and print the servers response
    def handle_command(self, cmd: str):
        self.debug(f"Sending command {repr(cmd)}")
        try:
            args = shlex.split(cmd)
        except ValueError:
            print("[ERROR] Error in command format")
            return

        if not args:
            return

        if args[0] == "download":
            if (len(args) < 2):
                print("[ERROR] Specify a file to download")
                return
            self.download_file(args[1])

        elif args[0] == "upload":
            if (len(args) < 2):
                print("[ERROR] Specify a file to upload")
                return

            # Send the file to the server
            self.upload_file(args[1])

        elif args[0] == "exit" or args[0] == "quit":
            print("Goodbye.")
            self.socket.close()
            exit(0)
        
        elif args[0] == "help":
            print("Available Options:")
            print("  pwd  cd  ls  cat  sha256  download  upload  help  exit")

        else:
            # Other basic commands: pwd, cd, ls, cat, sha256
            self.send(cmd)
            self.receive_response()

    # Download a file from the server to the client
    def download_file(self, filepath: str):
        # Make sure the file exists on the server
        self.send(f'sha256 "{filepath}"')
        line = self.get_server_output()
        if line.endswith("No such file or directory"):
            print(f"[ERROR] Cannot access '{filepath}': No such file or directory")
            return
        
        # If the file exists locally (under file.basename, not the full filepath) check the SHA
        filename = os.path.basename(filepath)
        if os.path.isfile(filename):
            self.debug(filename)
            sha_local = sha_files([filename])[0]
            self.debug(f"Local SHA:  {sha_local}")
            self.debug(f"Server SHA: {line}")
            if sha_local == line:
                print("Local file is up to date.")
                return

        # Receive the file from the server, download it to the pwd
        self.send(f'download "{filepath}"')
        ft = FileTransfer(self.socket)
        ft.receive_file(filename)
        self.receive_response()

    # Upload a file to the server
    def upload_file(self, filepath: str):
        # First ensure that the file actually exists
        if not os.path.isfile(filepath):
            self.debug(f"Could not find file: {filepath}")
            print("[ERROR] File not found")
            return
    
        # Compare the local SHA with the remote SHA
        filename = os.path.basename(filepath)
        self.send(f'sha256 "{filename}"')
        remote_sha = self.get_server_output()
        local_sha = sha_files([filepath])[0]
        self.debug(f"Local SHA:  {local_sha}")
        self.debug(f"Server SHA: {remote_sha}")
        if remote_sha == local_sha:
            print("Remote file is up to date.")
            return

        # Send the file to the server
        self.debug(f"Sending file: {filepath}")
        self.send(f'upload "{filename}"')
        ft = FileTransfer(self.socket)
        ft.send_file(filepath)
        self.receive_response()
        self.debug(f"File transfer complete.")

    # Receive response from server after sending a command
    def receive_response(self, print_output = True):
        recv = Receiver(self.socket)
        while True:
            line = recv.receive()
            if line == "---":
                break
            if print_output: print(line)
    
    # Receive a response from the server and return the first line
    def get_server_output(self):
        recv = Receiver(self.socket)
        out = None
        while True:
            line = recv.receive()
            if out == None:
                out = line
            if line == "---":
                break
        return out

    # Print debug messages if debug is enabled in args
    def debug(self, *args, **kwargs):
        if not self.args.debug:
            return
        print("[DEBUG] ", *args, **kwargs)

# Main program loop
def main():
    client = Client()
    client.parse_args()
    client.get_secret()
    try:
        client.connect()
    except ConnectionRefusedError:
        print("Could not connect to server. Connection refused.")
        exit(1)

    try:
        client.handshake()
        while True:
            cmd = input("> ").strip()
            client.handle_command(cmd)
    except ConnectionError:
        print("Server connection closed.")
    except KeyboardInterrupt:
        print("Goodbye.")
        exit(0)

if __name__ == "__main__":
    main()
