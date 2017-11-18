#!/usr/bin/env python

from random import randint
import os
from Crypto.Cipher import AES
import string

printable = set(string.printable)

def get_strings():
    with open('strings.txt', 'r') as f:
        return f.read().split('\n')[:-1]


KEY = os.urandom(16)
IV = '\x00' * 16


def pad(data):
    length = 16 - len(data) % 16
    return data + chr(length) * length

def unpad(msg):
    if len(msg) % 16 > 0 or len(msg) == 0:
        raise ValueError('Invalid Padding')

    length = ord(msg[-1])
    for k in xrange(length):
        if ord(msg[- (k + 1)]) != length:
            raise ValueError('Invalid Padding')

    return msg[:-length]


def oracle():
    strings = get_strings()
    msg = strings[randint(0, len(strings) - 1)]

    crypt = AES.new(KEY, AES.MODE_CBC, IV)
    return crypt.encrypt(pad(msg))

def decrypt(cipher):
    crypt = AES.new(KEY, AES.MODE_CBC, IV)
    
    msg = crypt.decrypt(cipher)
    try:
        unpad(msg)
        return True
    except Exception:
        return False

for k in range(4):
    print decrypt(oracle())
