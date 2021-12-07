import sys
import numpy as np  # Numpy is Python's built in library for matrix operations.

print('You\'re running python %s' % sys.version.split(' ')[0])


# Euclidean Distances in Python
# A naïve implementation to compute pairwise distances:

def l2distanceSlow(X, Z=None):
    if Z is None:
        Z = X
    n, d = X.shape  # dimension of X
    m = Z.shape[0]  # dimension of Z
    D = np.zeros((n, m))  # allocate memory for the output matrix
    for i in range(n):  # loop over vectors in X
        for j in range(m):  # loop over vectors in Z
            D[i, j] = 0.0;
            for k in range(d):  # loop over dimensions
                D[i, j] = D[i, j] + (X[i, k] - Z[j, k]) ** 2;  # compute l2-distance between the ith and jth vector
            D[i, j] = np.sqrt(D[i, j]);  # take square root
    return D


# Efficient Programming with NumPy
# 1. Inner-Product Matrix

def innerproduct(X, Z=None):
    """function innerproduct(X,Z)"""
    if Z is None:  # case when there is only one input (X)
        Z = X;
    G = np.dot(X, Z.T)
    return G


# 2. Implement `calculate_S` and `calculate_R`

def calculate_S(X, n, m):
    """function calculate_S(X)"""
    assert n == X.shape[0]
    S = (X ** 2).sum(axis=1).reshape((n, 1)) * np.ones(shape=(1, m))
    return S


def calculate_R(Z, n, m):
    '''function calculate_R(Z)'''
    assert m == Z.shape[0]
    R = (Z ** 2).sum(axis=1) * np.ones(shape=(n, 1))
    return R


# 3. Implement l2distance

def l2distance(X, Z=None):
    """function D=l2distance(X,Z)"""
    if Z is None:
        Z = X;
    n, d1 = X.shape
    m, d2 = Z.shape
    assert (d1 == d2), "Dimensions of input vectors must match!"

    S = (X ** 2).sum(axis=1).reshape((n, 1)) * np.ones(shape=(1, m))
    R = (Z ** 2).sum(axis=1) * np.ones(shape=(n, 1))
    G = np.dot(X, Z.T)

    Dsq = abs(S + R - 2 * G)
    D = np.sqrt(Dsq)
    return D


# Let's compare the speed of l2-distance function against the previous naïve implementation:

import time

current_time = lambda: int(round(time.time() * 1000))

X = np.random.rand(700, 100)
Z = np.random.rand(300, 100)

print("Running the naïve version...")
before = current_time()
Dslow = l2distanceSlow(X)
after = current_time()
t_slow = after - before
print("{:2.0f} ms".format(t_slow))

print("Running the vectorized version...")
before = current_time()
Dfast = l2distance(X)
after = current_time()
t_fast = after - before
print("{:2.0f} ms".format(t_fast))
