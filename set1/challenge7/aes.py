#!/usr/bin/env python

# fix package problem
import os
os.sys.path.append(os.path.dirname(os.path.abspath('.')))

from challenge1 import base64_to_hex

with open('7.txt', 'r') as f:
    print base64_to_hex(f.read())

# use online openssl for the rest
