#!/usr/bin/python

import numpy as np
import sys

# A program to convert each index of ordered combinations for a given number of total positions (Npos) and substitutions (Nsub)
# to the corresponding positions of those subsitutions

if len(sys.argv) != 3:
    print "Usage: comb2sub.py Npos Nsub"
    exit(0)

Npos = int(sys.argv[1])
Nsub = int(sys.argv[2])

def get_tri(N):
    return N*(N+1)/2

c = Npos - (Nsub -1)
incr = []
for j in np.arange(1, c+1):
    incr.append(get_tri(j)) 
print incr

#for i in range(220):
#
#    if i > get_tri(c):
#        test = get_tri(c-1)
#
#    if i < get_tri(c):
