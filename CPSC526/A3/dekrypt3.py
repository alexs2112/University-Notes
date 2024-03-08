#!/bin/env python3

import argparse
import sys, os

BLOCK_SIZE = 1024

def dbg(*args, **kwargs):
    if not dbg.enabled:
        return
    print("[DEBUG] ", *args, **kwargs)
dbg.enabled = False

def error(msg="Cannot decrypt"):
    print("[ERROR] ", msg)

def parse_args():
    parser = argparse.ArgumentParser(
        prog='dekrypt3',
        description='''
        assuming f2=enc_aes_ctr(f1) and f3=enc_aes_ctr(f4) using the same password,
        this program tries to figure out f4. This is possible if the nonces
        used to produce f2 and f3 were the same.
        '''
    )
    parser.add_argument('f1', help='plaintext1')
    parser.add_argument('f2', help='ciphertext1')
    parser.add_argument('f3', help='ciphertext2')
    parser.add_argument('-d', '--debug', action='store_true',
                            help="enable debugging output")
    return parser.parse_args()

def files_exist(file_list):
    '''
    Ensure that all files passed in as file_list actually exist
    '''
    for f in file_list:
        if not os.path.isfile(f):
            error(f"Could not find file {f}")
            return False
    return True

def dekrypt(p1, c1, c2):
    if not files_exist([p1,c1,c2]):
        error()
        return

    with open(c1, "rb") as ct1, open(c2, "rb") as ct2:
        # First, ensure that the nonces are the same between c1 and c2
        nonce1 = ct1.read(32)
        nonce2 = ct2.read(32)
        dbg(f"Nonce1: {nonce1}")
        dbg(f"Nonce2: {nonce2}")
        if (nonce1 != nonce2):
            error("Nonces do not match")
            error()
            return
        
        with open(p1, "rb") as pt1:
            while True:
                # Read block by block of each file
                # key = PT1 XOR CT1
                # PT2 = CT2 XOR key
                pt1_block = pt1.read(BLOCK_SIZE)
                ct1_block = ct1.read(BLOCK_SIZE)
                key_block = [a^b for a, b in zip(pt1_block, ct1_block)]

                # If the key_block is empty, then one of the files is also empty
                if key_block == []:
                    break

                # Find the output plaintext block and spit it out to stdout
                ct2_block = ct2.read(BLOCK_SIZE)
                out_block = [a^b for a, b in zip(ct2_block, key_block)]
                if out_block == []:
                    break
                sys.stdout.buffer.write(bytes(out_block))

def main():
    args = parse_args()
    dbg.enabled = args.debug
    dekrypt(args.f1, args.f2, args.f3)

if __name__ == "__main__":
    main()
