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

def get_index(index, order):

    count = 0
    while index >= 0:
        index -= nchoosek(Npos-(order+count), Nsub-order)
        if index < 0:
            break
        count += 1
    index = count + order
    return index

def get_third_index(index, second):

    start = second-2
    for i in range(start):
        index -= nchoosek(Npos-(2+i), Nsub-2)

    third_index = get_index(index, 3)

    return third_index + start

def get_fourth_index(index, second, third):

    # The subtraction of these depend on eachother
    start = second-2
    for i in range(start):
        index -= nchoosek(Npos-(2+i), Nsub-2)
    start1 = third-3
    for i in range(start1):
        index -= nchoosek(Npos-(3+i), Nsub-3)

    fourth_index = get_index(index, 4)

    return fourth_index + start1

if __name__ == "__main__":

    if index >= nchoosek(Npos-1, Nsub-1):
        exit("index is too high!")

    second = get_index(index, 2)
    third = get_third_index(index, second)
#    fourth = get_fourth_index(index, second, third)
#    print '1', second, third, fourth
    print '1', second, third
