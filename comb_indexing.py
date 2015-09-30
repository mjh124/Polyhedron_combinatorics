#!/usr/bin/env python

import sys
import numpy as np
from itertools import combinations

if len(sys.argv) != 4:
    print "Usage: comb_indexing.py num_pos num_sub index"
    exit(0)

Npos = int(sys.argv[1])
Nsub = int(sys.argv[2])
index = int(sys.argv[3])

def nchoosek(pos, sub):
    count = 0
    for i in combinations(range(pos), sub):
        count += 1
    return count

def get_second_index(index):
    count = 0
    decrease_by = nchoosek(10, 1)
    if index >= nchoosek(11, 2):
        exit("index is too high!")
    while index >= 0:
        index -= (decrease_by - count)
#        print index
#        print "c=", count
        if index < 0:
            break
        count += 1
    skip = Npos - (decrease_by - count) + 1
    index += (decrease_by - count)
    third = skip + index
#    print count
#    print index*-1
    return count+2, third

if __name__ == "__main__":

    second, third = get_second_index(index)
    print '1', second, third
