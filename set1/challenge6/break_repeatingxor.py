#!/usr/bin/env python

# fix package problem
import os
os.sys.path.append(os.path.dirname(os.path.abspath('.')))


from challenge1 import base64_to_hex
from challenge2 import hexstr_xor


def hamming_distance(str1, str2):
    xored = hexstr_xor(str1.encode('hex'), str2.encode('hex'))
    return sum([bin(ord(c)).count("1") for c in xored.decode('hex')])

def calc_IOC(cipher, keysize):
    block = lambda x: cipher[x * keysize: (x + 1) * keysize]

    distances = [hamming_distance(block(k), block(k + 1)) for k in range(0, 4)]
    return sum(distances) / len(distances)

def find_keysize(cipher):
    return min([(calc_IOC(cipher, length), length)
        for length in range(0, 41)], key = lambda (a,b): b)

def 
