#!/usr/bin/env python

# fix package problem
import os
os.sys.path.append(os.path.dirname(os.path.abspath('.')))


from challenge1 import base64_to_hex
from challenge5 import repeat_xor
from challenge3 import singlebyte_crack
from challenge2 import hexstr_xor


def hamming_distance(str1, str2):
    xored = hexstr_xor(str1.encode('hex'), str2.encode('hex'))
    return sum([bin(ord(c)).count("1") for c in xored.decode('hex')])

def get_block(cipher, key_size, k):
    return cipher[k * key_size : (k + 1) * key_size]

def calc_IOC(cipher, keysize):
    block = lambda x: get_block(cipher, keysize, x)
    
    distances = [1.0 * hamming_distance(block(k), block(k + 1)) 
                 for k in range(0, 4)]
    
    # average results and normalize
    return (sum(distances) / len(distances)) * 1.0 / keysize

def find_keysize(cipher):
    return sorted([(calc_IOC(cipher, length), length)
        for length in range(3, 40)], key = lambda (a,b): a)

def transpose_blocks(cipher, keysize):
    block = lambda x: get_block(cipher, keysize, x)
    
    blocks = [block(k) for k in range((len(cipher) - 1) / keysize)]

    return [''.join([blocks[b][k]
             for b in range(len(blocks))])
            for k in range(len(blocks[0]))] # all blocks are the same length

def solve_block(block):
    return singlebyte_crack(str(block).encode('hex'))

def find_key(cipher, keysize):
    # VERY UNELEGANT  =(  SORRY
    print len(cipher)
    for k in range(keysize):
        block = transpose_blocks(cipher, keysize)[k]
        print "select correct key..."
        print ""
        for key,msg in solve_block(block):
            print str(key) + " --> " + msg


'''TEST
with open('6.txt', 'r') as f:
    cipher = base64_to_hex(f.read()).decode('hex')

    #find_keysize(cipher)
    #find_key(cipher, 29)
    #print repeat_xor(cipher, 'Terminator X: Bring the noise').decode('hex')
'''

'''HAMMING TEST
test1 = 'this is a test'
test2 = 'wokka wokka!!!'

print hamming_distance(test1, test2)
'''
