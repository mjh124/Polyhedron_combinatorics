#!/usr/bin/python

import sys
import numpy as np
from itertools import combinations

if len(sys.argv) != 4:
    print "Usage: comb_indexing3.py number-positions number-substitutions index"
    exit(0)

Npos = int(sys.argv[1])
Nsub = int(sys.argv[2])
index = int(sys.argv[3])

def idx_2_comb(Npos, Nsub, index):

    combs = list(combinations(range(Npos), Nsub))
    return combs[index]

if __name__ == "__main__":

    combination = idx_2_comb(Npos, Nsub, index)
    print combination
