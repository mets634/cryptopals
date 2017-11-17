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
    if len(data) % 16 == 0:
        return data

    return data + '\x04' * (16 - len(data) % 16)

def unpad(msg):
    if len(msg) % 16 > 0:
        raise ValueError('Invalid Padding')

    # remove padding
    while msg[-1] == '\x04':
        msg = msg[:-1]

    filtered_msg = [c for c in msg if c in printable]

    if len(filtered_msg) == len(msg):
        return msg
    
    raise ValueError('Invalid Padding')

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
