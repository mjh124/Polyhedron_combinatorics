#!/usr/bin/python

import sys
import numpy as np
from itertools import combinations, permutations

if len(sys.argv) !=2:
    print "Usage: BuildCuDistMat.py num_positions"
    exit(0)

num_pos = int(sys.argv[1])

# Combinations automatic
for j in range(num_pos+1):
    count = 0
    for i in combinations(range(num_pos), j):
        count += 1
    print num_pos,"choose",j,"=",count

#for i in combinations(range(num_pos), 4):
#    print i
