#!/usr/bin/env python

import os
os.sys.path.append(os.path.dirname(os.path.abspath('.')))

from challenge21 import mt
import time
from random import randint

def gen():
    print 'Sleeping ZZzzzzz...'
    time.sleep(randint(40, 180))
    seed = int(time.time())
    
    print 'Using seed ' + str(seed)
    rng = mt(seed)
    return rng.next()

def crack(first):

