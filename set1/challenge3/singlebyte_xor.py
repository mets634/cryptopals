#!/usr/bin/env python

# fix package problem
import os
os.sys.path.append(os.path.dirname(os.path.abspath('.')))


from challenge2 import hexstr_xor

def singlebyte_xor(hexstr, singlechar):
    charstr = singlechar * len(hexstr.decode('hex'))

    return hexstr_xor(hexstr, charstr.encode('hex'))


import string

cipher = 'ETAOIN SHRDLU'.encode('hex')

for x in range(50, 128):
    print str(x) + ":"
    print str(bytearray(singlebyte_xor(cipher, chr(x)))).decode('hex')
