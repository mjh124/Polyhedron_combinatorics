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
    while index >= 0:
        index -= nchoosek(Npos-(2+count), Nsub-2)
        if index < 0:
            break
        count += 1
    second_index = count + 2

    return second_index

def get_third_index(index, second):

    start = second-2
    for i in range(start):
        index -= nchoosek(Npos-(2+i), Nsub-2)

    count = 0
    while index >= 0:
        index -= nchoosek(Npos-(3+count), Nsub-3)
        if index < 0:
            break
        count += 1
    third_index = count + start + 3

    return third_index

if __name__ == "__main__":

    if index >= nchoosek(Npos-1, Nsub-1):
        exit("index is too high!")

    second = get_second_index(index)
    third = get_third_index(index, second)
    print '1', second, third
