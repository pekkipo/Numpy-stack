# create matrices for test data
# like random numbers and so on. like in Matlab

import numpy as np

# Array of zeros
Z = np.zeros(10)
print(Z)

# Matrix of zeros
Z_2 = np.zeros((10, 10))
print(Z_2)

# Array of ones
O = np.ones((10, 10))

# Random numbers
R = np.random.random((10, 10))
print(R)
# they will be greater than 0 but less than 1. Uniformly distributed numbers will be shown

# Random with Gaussian distribution. Around 0 though. With mean = 0 and variance = 1
G = np.random.randn(10, 10)  # doesn't take in tuples!
print(G)

# Mean
print(G.mean())

# Variance
print(G.var())
