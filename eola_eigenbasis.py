from math import *

import numpy as np


EPSILON = 1e-6

def equal(a, b):
    return abs(a - b).max() < EPSILON


A = np.matrix([[0, 1],
               [1, 1]])

evecs = [
    np.array([2, 1 + sqrt(5)]),
    np.array([2, 1 - sqrt(5)]),
]

# Change of basis matrix:
# Input: vector expressed in their coordinates
# Output: vector expressed in our coordinates
cob = np.matrix(evecs).T

# Inverse change of basis matrix:
# Input: vector expressed in our coordinates
# Output: vector expressed in their coordinates
cob_inv = -(1/(4 * sqrt(5))) * np.matrix([[  1 - sqrt(5),   -2],
                                          [-(1 + sqrt(5)),   2]])

assert equal(cob_inv, np.linalg.inv(cob))


# Transformation A expressed in eigenbasis
# cob_inv * A * cob
A_star = np.matrix([[(1 + sqrt(5))/2,         0        ],
                    [    0,          (1 - sqrt(5)) / 2]])

assert equal(A_star, cob_inv * A * cob)


def A_power(v, n):
    # 1. Convert v to eigenbasis
    # 2. Compute power in eigenbasis
    # 3. convert back
    return cob * (A_star ** n) * cob_inv * v


v = np.matrix([[3, 2]]).T
n = 17

assert equal(A_power(v, n), (A ** n) * v)
