#!/usr/bin/env python

import string

printable = set(string.printable)

def validate_padding(msg):
    if len(msg) % 16 > 0:
        raise ValueError('Invalid Padding')

    # remove padding
    while msg[-1] == '\x04':
        msg = msg[:-1]

    filtered_msg = [c for c in msg if c in printable]

    if len(filtered_msg) == len(msg):
        return msg
    
    raise ValueError('Invalid Padding')

"""TEST
msg1 = 'ICE ICE BABY\x04\x04\x04\x04'
msg2 = 'ICE ICE BABY\x05\x05\x05\x05'
msg3 = 'ICE ICE BABY\x01\x02\x03\x04'

assert validate_padding(msg1)
assert validate_padding(msg2) == False
assert validate_padding(msg3) == False

print 'YAYYYYY WE DID IT !!!!'"""
