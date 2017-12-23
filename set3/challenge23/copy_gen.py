#!/usr/bin/env python

import os
os.sys.path.append(os.path.dirname(os.path.abspath('.')))

from challenge21 import mt

class copy_mt(object):
    def __init__(self, state):
        '''Taken from 
        en.wikipedia.org/wiki/Mersenne_Twister#Initialization'''
        
        def untemper(num): 
            def lsb(n, k):
                if k < 0:
                    return 0
                return (n >> k) & 0x01
            def setlsb(n, k, val):
                return n | (val << k)
            def msb(n, k):
                if k < 0:
                    return 0
                return lsb(n, 31 - k)
            def setmsb(n, k, val):
                return setlsb(n, 31 - k, val)

            def right(n, k):
                res = 0
                for x in xrange(32):
                    res = setmsb(res, x, msb(n, x) ^ msb(res, x - k))
                return res
            def left(n, k, s):
                res = 0
                for x in xrange(32):
                    res = setlsb(res, x, lsb(n, x) ^ (lsb(res, x - k) & lsb(s, x)))
                return res

            num = right(num, 18)
            num = left(num, 15, 0xefc60000)
            num = left(num, 7, 0x9d2c5680)
            num = right(num, 11)

            return num

        self.index = 624
        self.state = [int(untemper(s) & 0xffffffff) for s in state]

    def next(self):
        '''Taken from 
        www.quadibloc.com'''

        def calc_temp(k):
            first = 0x1 & self.state[k]
            last = (0xffffffff - 0x1) & self.state[(k+1) % 624]
            return first | last

        def transform(k, func):
            temp = (calc_temp(k) >> 1) ^ self.state[func(k)]
            if temp & 0x1: # is odd
                temp = temp ^ 0x9908b0df
            self.state[k] = temp 
 
        if self.index >= 624: # need to generate more words
            map(lambda k: transform(k, lambda i: i + 397), range(227))
            map(lambda k: transform(k, lambda i: i - 227), range(227, 623))
            map(lambda k: transform(k, lambda i: 396), [623])
            self.index = 0
        
        # tempering
        res = self.state[self.index]
        res = res ^ (res >> 11)
        res = res ^ ((res << 7) & 0x9d2c5680)
        res = res ^ ((res << 15) & 0xefc60000)
        res = res ^ (res >> 18)

        self.index = self.index + 1
        return res


def test():
    rng = mt(10) 
    state = [rng.next() for _ in range(624)] # get 624 value

    cpy = copy_mt(state) # make copy of mt rng
    for k in xrange(10):
        assert cpy.next() == rng.next()
        print 'Passed --> ' + str(k)

test()
