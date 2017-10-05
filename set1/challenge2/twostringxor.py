#!/usr/bin/env python

# fix package problem
import os
os.sys.path.append(os.path.dirname(os.path.abspath('.')))

from operator import xor
from array import array

def hexstr_xor(hexstr1, hexstr2):
    arr1 = array('B', hexstr1.decode('hex'))
    arr2 = array('B', hexstr2.decode('hex'))

    res = [num1 ^ num2 for (num1, num2) in zip(arr1, arr2)]
    return str(bytearray(res)).encode('hex')

''' TEST
str1 = '1c0111001f010100061a024b53535009181c'
str2 = '686974207468652062756c6c277320657965'

str3 = '746865206b696420646f6e277420706c6179'

res = hexstr_xor(str1, str2)

assert res == str3

print "YAYYY WE PASSED!!!"'''
