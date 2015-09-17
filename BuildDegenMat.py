import numpy as np
from itertools import combinations

###
# Build degeneracy matrix for a given set of combinations
# Use a dictionary to control the looping structure
###

def get_combinations(Npos, Nsub):

    combs = []
    for i in combinations(range(Npos), Nsub):
        combs.append(i)
    return combs

# Need to map combs triple index to a continuous index, and back
# Continuous index = len(combs)

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
