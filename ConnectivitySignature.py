#!/usr/bin/python

import sys
import numpy as np
from DataFileParser import ParseXYZ
from itertools import permutations, combinations

if len(sys.argv) !=3:
    print "Usage: BuildCuDistMat.py Structure_XYZ number_substitutions"
    exit(0)

struc = sys.argv[1]
num_sub = int(sys.argv[2])

def get_combinations(num_pos, num_sub):

    combs = []
    for i in combinations(range(num_pos), num_sub):
        combs.append(i)
    return combs

def get_distance(p1, p2):

    dist = np.sqrt((x[p1]-x[p2])**2 + (y[p1]-y[p2])**2 + (z[p1]-z[p2])**2)
    return dist

def build_dist_matrix(combs, idx, num_sub):

    mat = np.zeros((num_sub, num_sub))
    for i in range(num_sub):
        for j in range(num_sub):
            BL = get_distance(combs[idx][i], combs[idx][j])
            mat[i][j] = mat[i][j] + BL
    return mat

def dist_signature(combs, idx, num_sub):

    signature = np.zeros(6)
    for i in range(num_sub):
        for j in range(num_sub):
            BL = get_distance(combs[idx][i], combs[idx][j])
            if BL == 0.0:
                signature[0] += 1
            elif BL == 3.5:
                signature[1] += 1
            elif 5.0 < BL < 6.0:
                signature[2] += 1
            elif 7.0 < BL < 8.0:
                signature[3] += 1
            elif BL == 8.9:
                signature[4] += 1
            elif BL > 9.0:
                signature[5] += 1
            else:
                exit("ERROR: Unexpected bond length")
    return signature

###
# Main function
###

if __name__ == "__main__":

    Natoms, sym, x, y, z = ParseXYZ(struc)

    combs = get_combinations(Natoms, num_sub)
 
    for i in range(len(combs)):
        if combs[i][0] == 0:
            #dist_mat = build_dist_matrix(combs, i, num_sub)
            sig = dist_signature(combs, i, num_sub)
            j = i + 2
            print "sub positions are",combs[i],":"
            print sig,"\n"
