#!/usr/bin/python

import sys
import numpy as np
from DataFileParser import ParseXYZ
from itertools import combinations

if len(sys.argv) != 3:
    print "Usage: ConnectivitySignature.py Structure_XYZ number_substitutions"
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

def build_degen_matrix(combs, Nsub):

    degen_mat = np.zeros((len(combs), len(combs)))
    for i in range(len(combs)):
        sig = dist_signature(combs, i, Nsub)
        count = 0
        for j in range(len(combs)):
            sig1 = dist_signature(combs, j, Nsub)
            b = np.array_equal(sig, sig1)
            if b == True:
                degen_mat[i][j] += 1
                count += 1
    return degen_mat

def read_degen_matrix(degen_mat, num_rows):

    skip = []
    degen = []
    unique_row = []

    for i in range(num_rows):
        if i in skip:
            continue
        array1 = degen_mat[i,:]
        unique_row.append(i)
        degeneracy = 0
        for j in range(num_rows):
            array2 = degen_mat[j,:]
            a = np.array_equal(array1, array2)
            if a == True:
                degeneracy += 1
                skip.append(j)
        degen.append(degeneracy)

    return unique_row, degen

def write_summary_file(unique_row, degen):

    fout = str(Nsub) + '_summary.txt'
    with open(fout, 'w') as f:
        f.write('# i struc degen\n')
        for i in range(len(unique_row)):
            f.write('%d  %d  %d\n' % (i, unique_row[i], degen[i]))

if __name__ == "__main__":

    Natoms, sym, x, y, z = ParseXYZ(struc)
    combs = get_combinations(Natoms, Nsub)
 
    degen_mat = build_degen_matrix(combs, Nsub)
#    print degen_mat
    unique_row, degen = read_degen_matrix(degen_mat, len(combs))
    write_summary_file(unique_row, degen)
#    print unique_row, degen
