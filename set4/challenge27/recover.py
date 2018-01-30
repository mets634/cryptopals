#!/usr/bin/env python

import os
os.sys.path.append(os.path.dirname(os.path.abspath('.')))

from Crypto.Cipher import AES

PREFIX = r'comment1=cooking%20MCs;userdata='
POSTFIX = r';comment2=%20like%20a%20pound%20of%20bacon'

KEY = os.urandom(16)
IV = KEY

def cbc_encrypt(iv, msg, key):
    crypto = AES.new(key, AES.MODE_CBC, iv)
    return crypto.encrypt(msg)

def cbc_decrypt(iv, cipher, key):
    crypto = AES.new(key, AES.MODE_CBC, iv)
    return crypto.decrypt(cipher)

def sxor(data, key):
    return bytearray(a^b for a, b in zip(*map(bytearray, [data, key])))

def verify(msg):
    for m in msg:
        if ord(m) > 128:
            return False
    return True

def encrypt():
    msg = 'A' * 16 + 'B' * 16 + 'C' * 16
    return cbc_encrypt(IV, msg, KEY)

def decrypt(cipher):
    msg = cbc_decrypt(IV, cipher, KEY)
    if not verify(msg):
        raise Exception(msg)
    return True

def attacker():
    cipher = encrypt()
    my_cipher = cipher[:16] + '\x00' * 16 + cipher[:16]

    try:
        decrypt(my_cipher)
        return False
    except Exception, e:
        msg = str(e)
        return sxor(msg[:16], msg[-16:])

def main():
    assert attacker() == KEY
    print 'YAYYY'

#main()
