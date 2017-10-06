#!/usr/bin/env python


from itertools import cycle


def repeat_xor(msg, key):
    keys = cycle(key)
    
    res = [chr(ord(letter) ^ ord(next(keys))) for letter in msg]
    return str(bytearray(res)).encode('hex')


'''TEST
key = 'ICE'

teststring = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"

testcipher = '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'

print repeat_xor(teststring, key)
print
print testcipher'''
