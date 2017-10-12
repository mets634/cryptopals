#!/usr/bin/env python

# fix package problem
import os
os.sys.path.append(os.path.dirname(os.path.abspath('.')))

from challenge11 import gen_aes_key
from challenge10 import cbc_encrypt
from challenge10 import cbc_decrypt

PREFIX = r'comment1=cooking%20MCs;userdata='
POSTFIX = r';comment2=%20like%20a%20pound%20of%20bacon'

KEY = gen_aes_key()
IV = '\x00' * 4 #os.urandom(4)

def sxor(msg1, msg2):
    return ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(msg1, msg2))

def encrypt(data):
    msg = PREFIX + data.replace(';', '').replace('=', '') + POSTFIX
    return cbc_encrypt(IV, msg, KEY)

def check_admin(cipher):
    msg = cbc_decrypt(IV, cipher, KEY)

    return r';admin=true;' in msg

def attack():
    inject_block = r';admin=true;B=as'
    useless_block = 'A' * 16

    cipher = encrypt(useless_block)

    zero_target_block = sxor(cipher[16:32], useless_block)
    inject_target_block = sxor(inject_block, zero_target_block)

    return cipher[:32] + inject_target_block + cipher[32:] 

print cbc_decrypt(IV, attack(), KEY)
print check_admin(attack())
