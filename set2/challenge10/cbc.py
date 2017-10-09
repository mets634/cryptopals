#!/usr/bin/env python

# fix package problem
import os
os.sys.path.append(os.path.dirname(os.path.abspath('.')))

from Crypto.Cipher import AES

def ecb_encode(msg, key):
    aes = AES.new(key, AES.MODE_ECB)
    return aes.encrypt(msg)

def cbc_encode(iv, msg, 
