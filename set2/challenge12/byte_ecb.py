#!/usr/bin/env python

# fix package problem
import os
os.sys.path.append(os.path.dirname(os.path.abspath('.')))

from challenge11 import *
from challenge10 import *
from base64 import b64decode
from challenge11 import detect_oracle
from math import ceil


POSTFIX = b64decode('Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK')

KEY = gen_aes_key() # constant for all encryptions


def my_encrypt_oracle(data):
    return ecb_encrypt(data + POSTFIX, KEY)

def find_blocksize():
    data = 'a'

    prev = ''
    while True:
        blocksize = len(data)
        cipher = my_encrypt_oracle(data)

        # block(0) == block(1)
        if cipher[:blocksize - 1] == prev[:blocksize - 1] and blocksize > 4:
            return blocksize - 1
        
        prev = cipher
        data = data + 'a'

def byte_byte_attack(blocknum=0, deciphered=''):
    blocksize = find_blocksize()

    current_block = lambda cipher: cipher[
            blocksize * blocknum : blocksize * (blocknum + 1)]

    data = 'a' * blocksize

    block = ''
    for _ in xrange(blocksize):
        data = data[1:] # remove first byte from data (is an 'a' byte)

        outputs = { current_block(
            my_encrypt_oracle(data + deciphered + block + chr(c)) ) :
            chr(c)

            for c in range(256) }

        matching_byte = outputs[
                current_block(my_encrypt_oracle(data))]
        
        block = block + matching_byte

    return block
    
def main():
    print 'BLOCK SIZE --> ' + str(find_blocksize())
    if detect_oracle(my_encrypt_oracle) == 1:
        print 'AES MODE --> ECB'
    else:
        print 'AES MODE --> CBC'

    print 'DECRYPTED BLOCKS --> '
    msg = ''
    for k in xrange(int(ceil(len(POSTFIX) / 16.0))):
        msg = msg + byte_byte_attack(k, msg)
    print msg

# main()
