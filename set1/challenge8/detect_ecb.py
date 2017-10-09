#!/usr/bin/env python

# fix package problem
import os
os.sys.path.append(os.path.dirname(os.path.abspath('.')))

from challenge6 import *
from challenge5 import repeat_xor

def is_ecb(cipher, blocksize):
    block = lambda x: cipher[x * blocksize : (x + 1) * blocksize]
    
    blocks = [block(k) for k in range((len(cipher) - 1) / blocksize)]

    return len(set(blocks)) < len(blocks)

def check_ecb(cipher):
    return is_ecb(cipher, 16)

def find_cipher(lines):
    lines = [(l, count)
            for l, count in zip(lines, range(len(lines)))
            if check_ecb(l)]

    return lines

with open('8.txt', 'r') as f:
    origin = f.read()
    lines = origin.split('\n')[:-1] # remove last empty line
    lines = [l.decode('hex') for l in lines]
    print find_cipher(lines) 
