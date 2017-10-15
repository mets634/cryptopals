#!/usr/bin/env python

from Crypto.Cipher import AES
from math import ceil
import struct

def sxor(msg1, msg2):
    index = min(len(msg1), len(msg2))

    msg1 = msg1[: index - 1]
    msg2 = msg2[: index - 1]

    return ''.join([chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(msg1, msg2)])

def encrypt(msg, nonce, key):
    block = lambda k: msg[16 * k : 16 * (k + 1)]

    crypt = AES.new(key, AES.MODE_ECB)

    cipher = ''
    for counter in xrange(int(ceil(len(msg) / 16.0))):
        keystream = crypt.encrypt(struct.pack('<8sQ', nonce, counter))

        cipher = cipher + sxor(block(counter), keystream)
    
    return cipher

def decrypt(cipher, nonce, key):
    return encrypt(cipher, nonce, key)


cipher = 'L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ=='.decode('base64')

print decrypt(cipher, '\x00' * 16, 'YELLOW SUBMARINE')
