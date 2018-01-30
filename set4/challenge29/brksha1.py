#!/usr/bin/env python

import os
os.sys.path.append(os.path.dirname(os.path.abspath('.')))

import struct
import parse

from challenge28 import mac_auth as auth
from challenge28 import sha1
from challenge28 import sha1_raw

def pad(data):
    padding = 'A' + 'X' * (55 - len(data) % 64)
    if len(data) % 64 > 55:
        padding += 'X' * (64 + 55 - len(data) % 64)
    return padding + struct.pack('>Q', 8 * len(data))

def split_hash(h):
    num = int(h, 16)
    a = num >> 128
    b = (num >> 96) & 0xffffffff
    c = (num >> 64) & 0xffffffff
    d = (num >> 32) & 0xffffffff
    e = num & 0xffffffff
    return [a, b, c, d, e]

pre_data = 'comment1=cooking%20MCs;userdata=foo;comment2=%20like%20a%20pound%20of%20bacon'
post_data = ';admin=true'

digest = auth(pre_data)

def validate(msg, h):
    return auth(msg) == h

def forge_msg(keylen):
    key = 'X' * keylen
    padding = pad(key + pre_data)
    return pre_data + padding + post_data
    
def forge_hash():
    # continue hash of sha1 with current state
    h = split_hash(digest)
    return sha1(post_data, h[0], h[1], h[2], h[3], h[4])

def attack():
    dig = forge_hash()
    for k in xrange(1, 50):
        msg = forge_msg(k)
        print k
        if validate(msg, dig):
            return msg, k
    raise Exception("OH NO!!!")

print attack()
