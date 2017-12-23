#!/usr/bin/env python

from random import randint
import os
from Crypto.Cipher import AES
import string

printable = set(string.printable)

def get_strings():
    with open('strings.txt', 'r') as f:
        return f.read().split('\n')[:-1]

KEY = os.urandom(16)
#KEY = '\x10' * 16 # JUST FOR TESTING
IV = '\x00' * 16 # CHOOSE ANYONE, doesn't effect program


def pad(data):
    length = 16 - len(data) % 16
    if length == 16:  # needs to be 0
        length = 0

    return data + chr(length) * length

def unpad(msg):
    if len(msg) % 16 > 0 or len(msg) == 0:
        raise ValueError('Invalid Padding')

    length = ord(msg[-1])
    for k in xrange(length):
        if ord(msg[- (k + 1)]) != length:
            raise ValueError('Invalid Padding')

    return msg[:-length]


def oracle():
    strings = get_strings()
    msg = strings[randint(0, len(strings) - 1)]
    #msg = strings[0] # JUST FOR TESTING

    crypt = AES.new(KEY, AES.MODE_CBC, IV)
    return crypt.encrypt(pad(msg.decode('base64')))

def decrypt(cipher):
    crypt = AES.new(KEY, AES.MODE_CBC, IV)
    
    msg = crypt.decrypt(cipher)
    try:
        unpad(msg)
        return True
    except Exception:
        return False

def get_byte(block, res, k):
    target = 16 - k
    fake = [res[i] ^ target for i in range(16)]
    
    #print res
    for i in xrange(256):
        fake[k] = i
        #print [chr(c) for c in fake]
        temp = ''.join(chr(c) for c in fake)
        if decrypt(temp + block):
            return i ^ target

    return 0x00 # error, try without correct byte

def intermediate(block):
    res = [0 for _ in range(16)]
    for k in xrange(15, -1, -1):
        res[k] = get_byte(block, res, k)
    '''
    print '----------'
    print res
    print '---------'
    '''
    return [chr(c) for c in res]

    
def attack(cipher):
    sxor = lambda s1, s2: ''.join([chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2)])

    blocks = [cipher[k * 16 : (k + 1) * 16] for k in range(len(cipher) / 16)]

    res = ''
    for k in xrange(len(blocks)):
        if k == 0:
            prev = IV
        else:
            prev = blocks[k - 1]
        
        res = res + sxor(prev, intermediate(blocks[k]))
    
    return res

cipher = oracle()
print unpad(attack(cipher))
