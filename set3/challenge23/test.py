#!/usr/bin/env python

def right(num, k):
    def msb(k):
        return 0xffffffff << (32 - k) & 0xffffffff
    def lsb(k):        
        return 0xffffffff >> (32 - k) & 0xffffffff
    
    m = num & msb(32 - k)
    mid = num & (0xffffffff - (msb(32 - k) | lsb(k)))
    l = num & lsb(k)
    
    return m | (m >> k) ^ mid | (((m >> k) ^ mid) >> k) ^ l

def left(num, k, n):
    def lsb(num, k):
        if k < 0:
            return 0
        return (num >> k) & 1

    def set_lsb(num, k, val):
        return num | (val << k)

    temp = 0
    for i in xrange(32):
        temp = set_lsb(num, i, lsb(num, i) ^ (lsb(temp, i - n) & lsb(n, i)))
    return temp




num = 0xfa34ae5
print num

t = num ^ (num >> 11)
print t

print right(t, 11)

l = num ^ ((num >> 15) & 0xefc60000)
print l
print left(l, 15, 0xefc60000)
