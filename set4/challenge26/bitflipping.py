#!/usr/bin/env python

import os
os.sys.path.append(os.path.dirname(os.path.abspath('.')))

from challenge25 import encrypt as ctr_encrypt
from challenge25 import decrypt as ctr_decrypt


PREFIX = r'comment1=cooking%20MCs;userdata='
POSTFIX = r';comment2=%20like%20a%20pound%20of%20bacon'

KEY = os.urandom(16)

def sxor(data, key):
    return bytearray(a^b for a, b in zip(*map(bytearray, [data, key])))

def encrypt(data):
    msg = PREFIX + data.replace(';', '').replace('=', '') + POSTFIX
    return ctr_encrypt(msg, KEY)

def check_admin(cipher):
    msg = ctr_decrypt(cipher, KEY)

    return r';admin=true;' in msg

def attack():
    inject_block = r':admin<true:'
    cipher = encrypt(inject_block)

    cipher[32] ^= 1
    cipher[38] ^= 1
    cipher[43] ^= 1

    return cipher

print check_admin(attack())
