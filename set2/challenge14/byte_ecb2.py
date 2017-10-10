#!/usr/bin/env python

# fix package problem
import os
os.sys.path.append(os.path.dirname(os.path.abspath('.')))

from challenge12 import my_encrypt_oracle
from challenge11 import gen_aes_key
from random import randint
from challenge10 import ecb_encrypt
from math import ceil
from base64 import b64decode

KEY = gen_aes_key()

PREFIX = os.urandom(randint(0, 30))
POSTFIX = b64decode('Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK')


def encrypt_oracle3(data):
    msg = PREFIX + data + POSTFIX
    return ecb_encrypt(msg, KEY)

def get_prefix_padding():
    return 'a' * (16 - len(PREFIX) % 16)

def byte_byte_attack2(blocknum=0, deciphered=''):
    padding = get_prefix_padding()
    prefix_padding_length = len(PREFIX) + len(padding)

    current_block = lambda cipher: cipher[
            prefix_padding_length + blocknum * 16 : 
            prefix_padding_length + (blocknum + 1) * 16]

    data = 'b' * 16

    block = ''
    for _ in xrange(16):
        data = data[1:]

        outputs = { current_block(
            encrypt_oracle3(padding + data + deciphered + block + chr(c))) :
            chr(c)

            for c in range(256) }

        matching_byte = outputs[
            current_block(encrypt_oracle3(padding + data))]

        block = block + matching_byte

    return block
    
def main():
    print '-----------------'
    msg = ''
    for k in xrange(int(ceil(len(POSTFIX) / 16.0))):
        msg = msg + byte_byte_attack2(k, msg)
    print msg

main()
