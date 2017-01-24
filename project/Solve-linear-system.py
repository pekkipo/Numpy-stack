#  Linear system: Ax = b
#  A is a m-x, x is a column vector of values we are trying to solve for and B is a vector of numbers
# Solution: A^-1 Ax = x = A^-1 b
# System of D equations and D unknowns

import numpy as np

# Example:

A = np.array([ [1, 2], [3, 4] ])
b = np.array([1, 2])

x = np.linalg.inv(A).dot(b)  # x = A^-1 b
print(x)

# There is a better way to do it in Numpy!
x = np.linalg.solve(A, b)
print(x)

# ALWAYS USE SOLVE FOR SUCH PROBLEM