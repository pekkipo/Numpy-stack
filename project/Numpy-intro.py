import numpy as np

L = [1, 2, 3]

A = np.array([1, 2, 3])

L.append(4)

L = L + [5]

for e in L:
    print(e)

for e in A:
    print(e)


# For usual list I d use append
# for numpy list append or + [5] won't work

# If I wanted to add the values rather than adding values to the list
L2 = []

for e in L:
    L2.append(e+e)

    # basically L2 = L + L

print(L2)

# Numpy
A2 = A + A

print(A2)

# + sign in Numpy array makes vector (or matrix) addition. While + for usual list would make a concatination

A3 = 2*A
print(A3)
# performs elementwise multiplication

L3 = 2*L
print(L3)
# adds values to the list making it [1,2,3,4,5,1,2,3,4,5]


# L**2 won't work. Can do list comprehension of for loop

# Numpy can't do that
A4 = A**2
print(A4)

# Other math operators will work. Element-wise operations. The case for most numpy functions
A5 = np.sqrt(A)
A6 = np.log(A)
A7 = np.exp(A)

for i in [A5, A6, A7]:
    print(i)

# Numpy arrays are more convenient compared to usual python list
# For lists we would do for loops. But they are very slow!




