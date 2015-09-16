#!/usr/bin/python

import sys
import numpy as np
from DataFileParser import ParseXYZ
from itertools import permutations, combinations

if len(sys.argv) !=3:
    print "Usage: BuildCuDistMat.py Structure_XYZ number_substitutions"
    exit(0)

struc = sys.argv[1]
Nsub = int(sys.argv[2])

def get_combinations(Npos, Nsub):

    combs = []
    for i in combinations(range(Npos), Nsub):
        combs.append(i)
    return combs

def get_distance(p1, p2):

    dist = np.sqrt((x[p1]-x[p2])**2 + (y[p1]-y[p2])**2 + (z[p1]-z[p2])**2)
    return dist

def build_dist_matrix(combs, idx, Nsub):

    mat = np.zeros((Nsub, Nsub))
    for i in range(Nsub):
        for j in range(Nsub):
            BL = get_distance(combs[idx][i], combs[idx][j])
            mat[i][j] = mat[i][j] + BL
    return mat

def dist_signature(combs, idx, Nsub):

    signature = np.zeros(6)
    for i in range(Nsub):
        for j in range(Nsub):
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

def get_last_sub(combs, idx, Nsub):

    last = Nsub - 1
    last_pos = combs[idx][last]
    return last_pos

if __name__ == "__main__":

    Natoms, sym, x, y, z = ParseXYZ(struc)
    combs = get_combinations(Natoms, Nsub)
 
    degen_mat = np.zeros((Natoms, Natoms))

    for i in range(len(combs)):
        if combs[i][0] == 0 and combs[i][1] == 1: # As long as I am only looking at the last atom in the combination, the matrix works great. Two options: gneralize this if-statement or the matrix.
            sig = dist_signature(combs, i, Nsub)
            count = 0
            for j in range(len(combs)):
                if combs[j][0] == 0 and combs[j][1] == 1:
                    sig1 = dist_signature(combs, j, Nsub)
                    b = np.array_equal(sig, sig1)
                    if b == True:
                        n = get_last_sub(combs, i, Nsub)
                        m = get_last_sub(combs, j, Nsub)                        
                        degen_mat[n][m] += 1

                        count += 1
                        print combs[i],"-",combs[j],"degen =",count
    print degen_mat
