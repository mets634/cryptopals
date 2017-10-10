#!/usr/bin/env python

# fix package problem
import os
os.sys.path.append(os.path.dirname(os.path.abspath('.')))

from challenge11 import gen_aes_key
from challenge10 import ecb_encrypt
from challenge10 import ecb_decrypt
from challenge9 import pad
from math import ceil

def parse_cookies(cookie_string):
    cookie_list = cookie_string.split(r'&')
  
    cookies = [cookie.split('=') for cookie in cookie_list]

    return { name : value
            for name, value in cookies }

def profile_for(email):
    email = email.translate(None, r'&=') # remove all '&' and '='
    return r'email=%s&uid=10&role=user' % email

KEY = gen_aes_key()

def encrypt_profile(profile):
    return ecb_encrypt(profile, KEY)

def decrypt_profile(cipher):
    return ecb_decrypt(cipher, KEY)

def unpad_profile(profile):
    return profile.replace('\x04', '')

'''RUN
profile1 = profile_for('dude@dude.com') # must be of length 13
profile2 = profile_for('A' * 9 + '@admin' + '\x04' * 11)

c1 = encrypt_profile(profile1)
c2 = encrypt_profile(profile2)

encrypted_profile = c1[:32] + c2[16:32]

print parse_cookies(decrypt_profile(encrypted_profile))'''
