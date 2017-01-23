import numpy as np

# Matrix. One way
# Matrix is a 2D array
M = np.array([ [1, 2], [3, 4] ])

# 1  2
# 3  4

# Python list
L = [ [1, 2], [3, 4] ]
print(L[0])  # [1,2]
print(L[0][0])  # 1

# In Numpy we can access the matrix's element like in Matlab (but starting with 0 element)
# Convention to access: first index - row, second - column
print(M[0][1])  # 2

# Matrix. Second way
M2 = np.matrix( [ [1, 2], [3, 4] ] )
print(M2)

# IT IS RECOMMENDED TO USE ARRAYS INSTEAD OF MATRICES!

# Can convert to normal array:
A = np.array(M2)


# With array we also can use matrix operation
# TRANSPOSE: .T
print(A.T)

