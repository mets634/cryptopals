#!/usr/bin/env python

# fix package problem
import os
os.sys.path.append(os.path.dirname(os.path.abspath('.')))


from challenge2 import hexstr_xor
import string


def singlebyte_xor(hexstr, singlechar):
    charstr = singlechar * len(hexstr.decode('hex'))

    return hexstr_xor(hexstr, charstr.encode('hex'))

def letter_frequency(hexstr):
    # NOTE: ignores all non english characters

    # remove all non english characters
    msg = filter(lambda c: ord(c) >= ord('A') and ord(c) <= ord('z'), 
            hexstr.decode('hex'))

    freq = [msg.count(chr(letter)) * 1.0 / len(msg) # frequency in msg
            for letter in range(ord('A'), ord('z'))
            if len(msg) > 0]

    return sum(map(lambda x: x * x, freq))

printable = set(string.printable) - set('{}|;~<>%$^*#+')

def pair_freq(cipher):
    xors = [singlebyte_xor(cipher, chr(letter))
            for letter in range(0, 256)]


    return [(msg, letter_frequency(msg)) 
            for msg in xors
            if all(c in printable for c in str(bytearray(msg)).decode('hex'))]


def brute_force(cipher):
    freq_pairs = pair_freq(cipher)
    if len(freq_pairs) == 0:
        return
    
    min_freq = min(freq_pairs, key=lambda (a,b): b)[1]
    
    for x in[(str(bytearray(a)).decode('hex'), b) 
            for (a, b) in pair_freq(cipher) 
            if abs(b - min_freq) < 0.000001]:

            print x[0]

'''TEST
cipher = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

brute_force(cipher)'''
