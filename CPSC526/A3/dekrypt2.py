#!/bin/env python3

import argparse, sys, numpy
from multiprocessing import Process, Queue
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

MAX_THREADS = 32

class PasswordPattern:
    def __init__(self, pattern: str):
        self.stack = [pattern]
        self.passwords = []
        self.num = 0
    
    def setup(self):
        while self.stack != []:
            i = self.stack.pop()
            if '_' in i:
                for c in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '']:
                    self.stack.append(i.replace('_', c, 1))
            else:
                self.passwords.append(i)
                self.num += 1

def dbg(*args, **kwargs):
    if not dbg.enabled:
        return
    print("[DEBUG] ", *args, **kwargs)
dbg.enabled = False

def parse_args():
    parser = argparse.ArgumentParser(
        prog='dekrypt2',
        description='AES decryptor',
    )
    parser.add_argument('password', help='password pattern used for decryption')
    parser.add_argument('-d', '--debug', action='store_true',
                            help="enable debugging output")
    return parser.parse_args()

def key_stretch(password: str, salt: bytes, key_len: int) -> bytes:
    '''
    converts a text password to a key(bytes) suitable for AES
    '''
    key = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=key_len,
        salt=salt,
        iterations=10,
    ).derive(password.encode())
    return key

def find_passwords(queue, passwords, salt, iv, data):
    # keep track of found passwords to prevent printing them twice
    for password in passwords:
        # get a decryptor using the current password pattern
        key = key_stretch(password, salt, 16)
        decryptor = Cipher(algorithms.AES(key), modes.CTR(iv)).decryptor()

        # decrypt the data block
        cblock = decryptor.update(data)
        if cblock.isascii():
            queue.put(password)

def decrypt_stdin(password: str):
    '''
    decrypts data from <stdin> and writes decrypted output to <stdout>
    '''
    # read the iv and salt from the first 32 bytes of stdin
    iv = sys.stdin.buffer.read(16)
    salt = sys.stdin.buffer.read(16)
    dbg(f"iv  : {iv.hex()}", file=sys.stderr)
    dbg(f"salt: {salt.hex()}", file=sys.stderr)

    # read the first block of file into a buffer
    data = sys.stdin.buffer.read(4096)

    # find all permutations of the password pattern
    pp = PasswordPattern(password)
    pp.setup()

    # split the possible passwords into chunks, each process iterates on a single chunk
    num_threads = min(MAX_THREADS, pp.num)
    passwords = numpy.array_split(pp.passwords, num_threads)

    # set up a pool of processes to operate on chunks, storing their found passwords in an output 2d array
    pool = []
    queue = Queue()
    for i in range(num_threads):
        t = Process(target=find_passwords, args=[queue, passwords[i], salt, iv, data])
        pool.append(t)
        t.start()

    for thread in pool:
        thread.join()

    # iterate over all found passwords and print them
    found = []
    while not queue.empty():
        p = queue.get()
        if p not in found:
            print(f"found password that seems to work: '{p}'")
            found.append(p)

def main():
    args = parse_args()
    dbg.enabled = args.debug
    decrypt_stdin(args.password)

if __name__ == "__main__":
    main()
