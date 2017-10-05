#!/usr/bin/env python

from base64 import b64encode # doesn't add newline at end of result

def hex_to_base64(hexstr):
    return b64encode(hexstr.decode('hex'))

def base64_to_hex(base64str):
    return base64str.decode('base64').encode('hex')

''' TEST
start = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
end = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'


conv1 = hex_to_base64(start)
conv2 = base64_to_hex(end)

assert conv1 == end
assert conv2 == start

print "yayyyy we did it!!!"'''
