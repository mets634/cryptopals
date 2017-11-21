#!/usr/bin/env python

import os
os.sys.path.append(os.path.dirname(os.path.abspath('.')))

from challenge21 import mt
import time
from random import randint


def gen():
    # sleep random seconds
    print 'Sleeping ZZzzzzz...'
    time.sleep(randint(40, 1000))

    # get time
    seed = int(time.time())
        
    # sleep again
    time.sleep(randint(40, 1000))

    # get value
    rng = mt(seed)
    return rng.next()

def crack(num):
    print 'Starting cracking...'
    now = int(time.time())
    for k in xrange(now, 0, -1): # countdown from now because seed is time
        rng = mt(k)
        if rng.next() == num:
            return k


res = crack(gen())
print 'Done'
print 'Seed --> ' + str(res)
