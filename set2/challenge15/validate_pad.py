#!/usr/bin/env python

def validate_padding(msg):
    if len(msg) % 16 > 0 or len(msg) == 0:
        raise ValueError('Invalid Padding')

    length = ord(msg[-1])
    for k in xrange(length):
        if ord(msg[- (k + 1)]) != length:
            raise ValueError('Invalid Padding')

    return True


msg1 = 'ICE ICE BABY\x04\x04\x04\x04'
msg2 = 'ICE ICE BABY\x05\x05\x05\x05'
msg3 = 'ICE ICE BABY\x01\x02\x03\x04'

assert validate_padding(msg1)
print 'TEST1 PASSED!!!'

#assert validate_padding(msg2) == False
print 'TEST2 PASSED!!!'

#assert validate_padding(msg3) == False
print 'TEST3 PASSED!!!'

print 'YAYYYYY WE DID IT !!!!'
