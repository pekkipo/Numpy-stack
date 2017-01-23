# Inner dimension must match
# if A is of size (2,3) and B is of size (3,3)
# Can do AB (inner dim is 3), Cannot do BA (inner dim is 3/2)

# IMPORTANT
# in Numpy * means element by element multiplication
# dot means matrices multiplication
# so in numpy: C = A.dot(B)

import numpy as np

# Matrix inverse
A = np.array([ [1, 2], [3, 4] ])
A_inv = np.linalg.inv(A)
print(A, A_inv)

print(A_inv.dot(A))  # gives the identity matrix. ones on the main diagonal

# Determinant
D = np.linalg.det(A)
print(D)  # -2

# Diagonal elements
d = np.diag(A)
print(d)  # [1, 4]

# Can create a matrix with a given diagonal and other elements will be zero
n = np.diag([1, 2])
print(n)  # [[1,0], [0,2]]


# Inner / Outer products

c = np.array([1, 2])
d = np.array([3, 4])

print(np.outer(c, d))  # Matrix multiplication [1*3 1*4] [2*3 2*4] = [1 4] [6 8]
print(np.inner(c, d))  # Inner - same as dot product. Same as a.dot(b). Gives 11

# Matrix trace. Sum of the diagonals of the matrix
np.diag(A).sum()  # gives 5
# or
np.trace(A)

# Eigen
