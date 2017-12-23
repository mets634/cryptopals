#!/usr/bin/env python

import os
os.sys.path.append(os.path.dirname(os.path.abspath('.')))

from challenge21 import mt
from random import getrandbits
from random import randint

def encrypt(msg, seed=10):
    gen = mt(seed & 0xffff)
    key = [gen.next() & 0xff for _ in range(len(msg))] # only 1-byte numbers
    
    return ''.join([chr(ord(a) ^ b) for a, b in zip(msg, key)])
    
def decrypt(cipher, seed=10):
    return encrypt(cipher, seed)

def crack(cipher):
    length = len(cipher) - 14

    for k in xrange(2**16-1): # largest 16 bit number
        if decrypt(cipher, k)[-14:] == 'A' * 14:
            return k


msg = os.urandom(randint(0, 1024)) + 'A' * 14
key = getrandbits(16)
cipher = encrypt(msg, key)

res = crack(cipher)
assert res == key
print 'Yayyy'
