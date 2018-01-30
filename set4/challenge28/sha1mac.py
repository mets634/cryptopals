#!/usr/bin/env python

import os
os.sys.path.append(os.path.dirname(os.path.abspath('.')))

from sha1 import sha1

def mac_auth(msg, mac):
    KEY = 'Secret!!! Not Saying!!!'

    return sha1(KEY + msg)
