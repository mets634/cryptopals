#!/usr/bin/env python

import os
os.sys.path.append(os.path.dirname(os.path.abspath('.')))

from challenge18 import *
import string


def get_strings():
    with open('cipher.txt', 'r') as f:
        return [l.decode('base64') for l in f.read().split('\n')[:-1]]

def bad_encrypt():
    return [encrypt(l, NONCE, KEY) for l in get_strings()]


KEY = '\xed\xd8\xf8\xaf\xd3\xc1\x06u\xa5T\xba\xf6\x10w\x0cb'
NONCE = '\x00' * 16

# ATTACK TIME (=

printable = set(string.printable) - set(r'')
def isprintable(s):
    for c in s:
        if c not in printable:
            return False

    return True

def score(s):
    if not isprintable(s):
        return -5

    chars = 'etaoinshrdlu'
    return sum(s.lower().count(c) for c in chars)

def singlebyte_xor(s, c):
    return ''.join([chr(ord(s[k]) ^ c) for k in range(len(s))])

def trunc(ciphers):
    '''Cut all ciphers to size of the shortest cipher'''
    
    length = min([len(c) for c in ciphers])

    print "USING LENGTH --> " + str(length)
    return [''.join(c[:length]) for c in ciphers]


def transpose(ciphers):
    '''Split ciphers into blocks using the same key.
    Assumes all ciphers are same length'''

    length = len(ciphers[0])
    return [''.join([c[k] for c in ciphers])
        for k in range(length)]

def break_single(block):
    '''Attack single-byte encryption on 
    block using letter-frequency'''
    
    decipher = lambda k: singlebyte_xor(block, k)
    

    scores = [(k, score(decipher(k))) for k in range(0xff)]

    key = max(scores, key=lambda p: p[1])[0]
    return key


def attack(ciphers):
    blocks = transpose(ciphers)
    return [break_single(b) for b in blocks]


ciphers = trunc(bad_encrypt())
blocks = transpose(ciphers)
keystream = attack(ciphers)

# Fixing singlebyte errors
keystream[0] = ord(ciphers[0][0]) ^ ord('I')
keystream[7] = ord(ciphers[0][7]) ^ ord('e')
keystream[14] = ord(ciphers[-1][14]) ^ ord('e')
keystream[29] = ord(ciphers[-1][29]) ^ ord('h')
keystream[46] = ord(ciphers[-2][46]) ^ ord('t')

keystream = ''.join([chr(k) for k in keystream])
msgs = [sxor(keystream, c) for c in ciphers]

for m in msgs:
    print '---------'
    print m
