#!/bin/env python3

import argparse
import sys
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

def dbg(*args, **kwargs):
    if not dbg.enabled:
        return
    print("[DEBUG] ", *args, **kwargs)
dbg.enabled = False

def parse_args():
    parser = argparse.ArgumentParser(
        prog='dekrypt1',
        description='AES decryptor',
    )
    parser.add_argument('password', help='password used for decryption')
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

def decrypt_stdin(password: str):
    '''
    decrypts data from <stdin> and writes decrypted output to <stdout>
    '''

    # read the iv and salt from the first 32 bytes of stdin
    iv = sys.stdin.buffer.read(16)
    salt = sys.stdin.buffer.read(16)

    # convert password to a key using key stretching
    key = key_stretch(password, salt, 16)

    dbg(f"iv  : {iv.hex()}", file=sys.stderr)
    dbg(f"salt: {salt.hex()}", file=sys.stderr)
    dbg(f"key : {key.hex()}", file=sys.stderr)

    # make a cipher using the key and iv
    decryptor = Cipher(algorithms.AES(key), modes.CTR(iv)).decryptor()

    # feed stdin to decryptor one block at a time and write out the
    # encrypted date to stdout
    while True:
        data = sys.stdin.buffer.read(4096)
        if len(data) == 0:
            break
        cblock = decryptor.update(data)
        sys.stdout.buffer.write(cblock)
    # finalize the cipher
    cblock = decryptor.finalize()
    sys.stdout.buffer.write(cblock)

def main():
    args = parse_args()
    dbg.enabled = args.debug
    decrypt_stdin(args.password)

if __name__ == "__main__":
    main()
