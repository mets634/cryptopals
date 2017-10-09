#!/usr/bin/env python

# fix package problem
import os
os.sys.path.append(os.path.dirname(os.path.abspath('.')))

from Crypto.Cipher import AES
from challenge9 import pad
from math import ceil

def sxor(str1, str2):
    return ''.join(chr(ord(c1) ^ ord(c2)) 
            for (c1, c2) in zip(str1, str2))

def ecb_encrypt(msg, key):
    aes = AES.new(key, AES.MODE_ECB)
    return aes.encrypt(msg)

def ecb_decrypt(cipher, key):
    aes = AES.new(key, MODE_ECB)
    return aes.decrypt(cipher)

def cbc_encrypt(iv, msg, key):
    block = lambda k: msg[k * len(key) : (k + 1) * len(key)]

    block_count = ceil(len(msg) * 1.0 / len(key))
    
    msg = pad(block_count * len(key))

    prev_cipher = iv
    cipher = ''
    for k in xrange(block_count):
        # The algorithm -- > C(i) = Ek( B(i) xor C(i - 1) )

        added_previous = sxor(prev_cipher, block(k)) # B(i) xor C(i - 1)
        prev_cipher = ecb_encrypt(added_previous, key) # E(--previous line--)
        
        cipher += prev_cipher

    return cipher

def cbc_decrypt(iv, cipher, key):
    

with open('10.txt') as f:
    cipher = f.read()
