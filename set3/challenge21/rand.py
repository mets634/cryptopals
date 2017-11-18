#!/usr/bin/env python

import os
os.sys.path.append(os.path.dirname(os.path.abspath('.')))


class mt(object):
    def __init__(self, seed=1):
        '''Taken from 
        en.wikipedia.org/wiki/Mersenne_Twister#Initialization'''

        self.index = 624
        self.state = [seed & 0xffffffff]

        def init_gen(k):
            f = 1812433253
            prev = self.state[k-1]
            return (f * (prev ^ (prev >> 30)) + k) & 0xffffffff

        map(lambda k: self.state.append(init_gen(k)), range(1, 624))
        

    def next(self):
        '''Taken from 
        www.quadibloc.com'''

        def calc_temp(k):
            first = 0x1 & self.state[k]
            last = (0xffffffff - 0x1) & self.state[(k+1) % 624]
            return first | last

        def transform(k, func):
            temp = (calc_temp(k) >> 1) ^ 0x9908b0df
            if temp & 0x1: # is odd
                temp = temp ^ self.state[func(k)]
            self.state[k] = temp 
 
        if self.index >= 624: # need to generate more words
            map(lambda k: transform(k, lambda i: i + 397), range(227))
            map(lambda k: transform(k, lambda i: i - 227), range(227, 623))
            map(lambda k: transform(k, lambda i: 396), [623])
            self.index = 0
        
        # tempering
        res = self.state[self.index]
        res = res ^ res >> 11
        res = res ^ ((res << 7) & 0x9d2c5680)
        res = res ^ ((res << 15) & 0xefc60000)
        res = res ^ (res >> 18)

        self.index = self.index + 1
        return res

def test():
    rand = mt(10)
    for k in xrange(15):
        print str(k) + " --> " + str(rand.next())
