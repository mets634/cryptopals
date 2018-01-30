#!/usr/bin/env python

import os
os.sys.path.append(os.path.dirname(os.path.abspath('.')))

from Crypto.Cipher import AES
import struct


def blocks(s):
    return (s[k : k + 16] for k in xrange(0, len(s), 16))

def sxor(data, key):
    return bytearray(a^b for a, b in zip(*map(bytearray, [data, key])))

def encrypt(msg, key, counter = 0):
    aes = AES.new(key, AES.MODE_ECB)

    res = ''
    for b in blocks(msg):
        key = aes.encrypt(struct.pack('<2Q', 0, counter))
        res = res + sxor(b, key)
        counter = counter + 1

    return res

def decrypt(cipher, key, counter = 0):
    return encrypt(cipher, key, counter)
    
def edit(cipher, key, offset, newtext):
    block_num = offset / 16
    block_count = len(newtext) / 16 + 1
    start = offset % 16

    # decrypt needed blocks
    msg = decrypt(
            cipher[block_num * 16: (block_num + block_count) * 16], 
            key, block_num)

    # substitute newtext into msg
    msg = msg[:start] + newtext + msg[start + len(newtext):]

    # insert new ciphertext into correct index    
    encrypted = encrypt(msg, key, block_num)
    return cipher[:block_num * 16] + encrypted + cipher[(block_num * 16 + len(encrypted)):]

def get_cipher(key):
    msg = open('25.txt').read()
    return encrypt(msg, key)

def attack(secret_cipher, secret_key):
    msg = 'X' * len(secret_cipher)
    cipher = edit(secret_cipher, secret_key, 0, msg)

    keystream = sxor(msg, cipher)
    return sxor(secret_cipher, keystream)

def main():
    key = os.urandom(16)
    cipher = get_cipher(key)

    print attack(cipher, key)

#main()
