#!/usr/bin/env python

# fix package problem
import os
os.sys.path.append(os.path.dirname(os.path.abspath('.')))

from challenge11 import *
from challenge10 import *
from base64 import b64decode
from challenge11 import detect_oracle

POSTFIX = b64decode('Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK')

KEY = gen_aes_key() # constant for all encryptions


def my_encrypt_oracle(data):
    return ecb_encrypt(data + POSTFIX, KEY)

def find_blocksize():
    data = 'a'

    prev = ''
    while True:
        blocksize = len(data)
        cipher = my_encrypt_oracle(data)

        # block(0) == block(1)
        if cipher[:blocksize - 1] == prev[:blocksize - 1] and blocksize > 4:
            return blocksize - 1
        
        prev = cipher
        data = data + 'a'

def byte_byte_attack(blocknum=0, data=None):
    blocksize = find_blocksize()

    # initial block
    if blocknum == 0:
        data = 'a' * blocksize

    block = ''
    for _ in xrange(1, blocksize + 1):
        data = data[:-1]

        outputs = { my_encrypt_oracle(data + block + chr(c))[
            blocksize * blocknum : (blocknum + 1) * blocksize] : 
                
            data + block + chr(c)
            for c in range(256) }

        matching_block = outputs[my_encrypt_oracle(data)[
            blocksize * blocknum : (blocknum + 1) * blocksize]]

        block = block + matching_block[-1]

    return block
    

print 'BLOCK SIZE --> ' + str(find_blocksize())
if detect_oracle(my_encrypt_oracle) == 1:
    print 'AES MODE --> ECB'
else:
    print 'AES MODE --> CBC'

print 'DECRYPTED BLOCK --> ' 
prev = byte_byte_attack()
print prev
print byte_byte_attack(1, prev)
