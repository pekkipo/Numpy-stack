# Inner dimension must match
# if A is of size (2,3) and B is of size (3,3)
# Can do AB (inner dim is 3), Cannot do BA (inner dim is 3/2)

# The file includes info in EIGENVECTORS and EIGENVALUES

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

# Eigenvalues and eigenvectors
X = np.random.randn(100, 3)
# Convention: Sample takes up a row, columns - features. So 100 samples, 3 features
# Covariance m-x
cov = np.cov(X)
print(cov.shape)  # shows the shape of the covariance matrix

# Shows 100 by 100. This is wrong. Our cov matrix should be 3 by 3
# Solve using transposing
cov = np.cov(X.T)
print(cov)  # now 3 by 3 as expected
# TRANSPOSE FOR THE CALCULATION THE COVARIANCE MATRIX

# tow funcs two calculate eigenvectors and eigenvalues
# np.linalg.eig(A)
# or
# np.lingalg.eigh(A)  # for symmetric and Hermittian matrices only!
# symmetric: A = A_transposed    hermittian: A = A_h. A_h is a conjugate transpose of A

# Covariance is symmetric, so we can use eigh
print(np.linalg.eigh(cov))  # gives a tuple. First tuple contains three eigenvalues. Second tuple gives 3 eigenvectores stored in columns
print(np.linalg.eig(cov))
