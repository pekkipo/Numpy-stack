# Example

#  The admission fee at a small fair is 1.50$ for children and 4.00$ for adults. On a certain day, 2200 people enter the fair
#  and 5050$ is collected. How many children and how many adults attended?

import numpy as np

# Let X1 - number of children
# X2 - number of adults
# X1 +_X2 = 2200
#1.5*X1 +4*X2 = 5050

# Solution:
# A = 1  1
#    1.5 4
# x = x1
#     x2
# b = 2200
#     5050

A = np.array([[1, 1], [1.5, 4]])
b = np.array([2200, 5050])

sol = np.linalg.solve(A, b)
print('{} children and {} adults have attended the fair'.format(sol[0], sol[1]))

# 1500 children and 700 adults have attended the fair