#!/usr/bin/env python

# fix package problem
import os
os.sys.path.append(os.path.dirname(os.path.abspath('.')))

from challenge10 import *
from random import randint
from random import choice

def gen_aes_key():
    return os.urandom(16)

def encrypt_oracle(data):
    random_garbage = lambda: 'a' * randint(5, 10)
    random_iv = lambda: os.urandom(4)

    msg = random_garbage() + data + random_garbage()
    key = gen_aes_key()

    if choice([True, False]):
        return ecb_encrypt(msg, key)
    return cbc_encrypt(random_iv(), msg, key)

def detect_oracle(encryption_box):
    '''The method used is add enough of the same
    byte (the letter "a" for example) so that
    no matter what the second and third block 
    are the same thing, then if they are encrypted
    the same way then this is ECB other wise it is CBC.'''

    # use black box for generating cipher
    data = 'a' * (32 + 11 * 2)
    cipher = encryption_box(data)

    block = lambda k: cipher[k * 16 : (k + 1) * 16]

    if block(1) == block(2):
        return 1 # ECB
    return 2 # CBC

'''TEST
for _ in range(5):
    print "------------"
    print detect_oracle(encrypt_oracle)
    print "------------"'''
