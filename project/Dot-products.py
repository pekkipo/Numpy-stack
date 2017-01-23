import numpy as np

a = np.array([1, 2])

b = np.array([2, 1])

dot = 0

for e, f in zip(a,b):  # zip return [(1,2), (2,1)]
    dot += e*f

print(dot)

# With numpy can do it easier:
print(a*b)  # gives [2,2] element-wise multiplication

s = np.sum(a*b)  # also can be (a*b).sum() # Sum of two vectors
print(s)
# gives 4. The same as the for loop above

# There is a dot func for this actually
d = np.dot(a, b)  # also a.dot(b) or b.dot(a) would work
print(d)
# gives 4

# Now use one of the definitions of a dot product to calculate the angle between vectors. Using their magnitudes
# One way to find magnitude
a_mag = np.sqrt((a*a).sum())
print(a_mag)
# Numpy way
a_mag = np.linalg.norm(a)
print(a_mag)

# Now find the angle
cos_angle = a.dot(b) / (np.linalg.norm(a) * np.linalg.norm(b))
print(cos_angle)

angle = np.arccos(cos_angle)
print(angle)


