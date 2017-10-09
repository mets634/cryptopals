#!/usr/bin/env python

def pad(msg, length):
    return msg + '\x04' * (length - len(msg))


msg = 'YELLOW SUBMARINE'
assert pad(msg, 20) == 'YELLOW SUBMARINE\x04\x04\x04\x04'

print "YAYYY"
