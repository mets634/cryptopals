#!/usr/bin/env python

# fix package problem
import os
os.sys.path.append(os.path.dirname(os.path.abspath('.')))

from challenge3 import brute_force


def get_strings():
    with open('4.txt', 'r') as f:
        return f.read().splitlines()

count = 1

# USE GREP TO SORT THE LINE NUMBER!!!
for line in get_strings():
    print count
    count = count + 1

    brute_force(line)
