#!/usr/bin/env python

# fix package problem
import os
os.sys.path.append(os.path.dirname(os.path.abspath('.')))


from challenge2 import hexstr_xor
import string


def singlebyte_xor(hexstr, singlechar):
    charstr = singlechar * len(hexstr.decode('hex'))

    return hexstr_xor(hexstr, charstr.encode('hex'))


printable = set(string.printable) - set('~#`|')

xor_e = lambda x: chr(x ^ ord('e'))

def letter_freq(cipher):
    msg = cipher.decode('hex')

    counts = [(chr(k), msg.count(chr(k)))
              for k in range(1, 256)
              if msg.count(chr(k)) > 0
              and all([c in printable # makes a legal word
                       for c in singlebyte_xor(cipher, xor_e(k)).decode('hex')])]

    counts.sort(key = lambda (a,b): b, reverse=True)
    return counts

def singlebyte_crack(cipher):
    key = lambda letter: xor_e(ord(letter))
    return [(key(letter), singlebyte_xor(cipher, key(letter)).decode('hex'))
            for letter, _ in letter_freq(cipher)]
    
    

'''TEST
cipher = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

for key, msg in singlebyte_crack(cipher):
    print key + " --> " + msg'''
