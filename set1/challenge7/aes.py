#!/usr/bin/env python

# fix package problem
import os
os.sys.path.append(os.path.dirname(os.path.abspath('.')))

from challenge1 import base64_to_hex
from Crypto.Cipher import AES

with open('7.txt', 'r') as f:
    	cipher =  base64_to_hex(f.read()).decode('hex')
	aes = AES.new('YELLOW SUBMARINE', AES.MODE_ECB)
	print aes.decrypt(cipher)
