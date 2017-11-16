#!/usr/bin/env python

import os
os.sys.path.append(os.path.dirname(os.path.abspath('.')))

import sys
from challenge18 import *
import string

def get_strings():
    with open('strings.txt', 'r') as f:
        return [l.decode('base64') for l in f.read().split('\n')[:-1]]

def bad_encrypt():
    return [encrypt(l, NONCE, KEY) for l in get_strings()]


KEY = '\xed\xd8\xf8\xaf\xd3\xc1\x06u\xa5T\xba\xf6\x10w\x0cb'
NONCE = '\x00' * 16

printable = set(string.printable) - set(r'$%/~@#&*^{}[]|\><=+-_():;"')


def calc_freq(data):
    freqs = { chr(k) : data.count(chr(k))
            for k in range(0, 256) }

    return sorted(freqs, key=lambda (k, v): v, reverse=True)

def attack_next(ciphers, keystream):
    '''Attack next byte in cipher by checking all
    keys that end up with printable characters'''

    length = len(keystream)

    possible_keys = [k for k in range(0, 256)
            if all([chr(k ^ ord(c[length])) in printable
                for c in ciphers if len(c) > len(keystream)])
            ]

    return possible_keys

def sub_non_print(s):
    s = list(s)
    for k in xrange(len(s)):
        if s[k] not in printable:
            print "NON-PRINT: index %d cipher-byte %s" % (k, str(hex(ord(s[k]))))
            s[k] = '$'

    return ''.join(s)

cip_num = 37
keystream = [0x1c, 0x83, 0xa1, 0x43, 0x36, 0xfb, 0xa5, 0x2b, 0x6a, 0xae, 0x3b, 0x2e, 0xca, 0xd1, 0x46, 0xa0, 0x18, 0xe7, 0x92, 0x68, 0x4d, 0x7, 0x96, 0x50, 0xbb, 0xa4, 0x5, 0x92, 0xc6, 0xcb, 0x48, 0x99, 0xc3, 0x3e, 0x10, 0xaf, 0x96, 0x65]


keystream = ''.join([chr(k) for k in keystream])
ciphers = bad_encrypt()

# DONE
if max([len(c) for c in ciphers]) <= len(keystream):
    print "YAYYY WE DID IT!!!\n"
    for c in ciphers:
        print sxor(c, keystream)
    sys.exit(0)

# need to test against another ciphertext
if len(keystream) >= len(ciphers[cip_num]):
    print "CHANGE CIPHER!!!"
    print sxor(keystream[:len(ciphers[cip_num])], ciphers[cip_num])
    sys.exit(0)

for k in attack_next(ciphers, keystream):
    res = sxor(ciphers[cip_num], keystream + chr(k))
    res = sub_non_print(res)
    print str(hex(k)) + " " + res
