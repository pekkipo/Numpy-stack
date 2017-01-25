# An image is just a matrix of numbers
# Recall image processing class

# Each value is an intensity at a coordinate i j
# JPG or PNG are not matrices due to a compression
# Decompress them to get back a matrix

# Get data at https://www.kaggle.com/c/digit-recognizer/data
# train.csv

import pandas as pd
import matplotlib.pyplot as plt

# The goal is to display an image

df = pd.read_csv("large_files/train.csv")
print(df.shape)  # 42000 785

M = df.as_matrix()

# We can grab the first image in a data set like this
im = M[0, 1:]  # select 0th row (0th sample) and give me all the columns except the column at position 0. In this data set first is not a pixel but a label
im.shape  # (784,)

im = im.reshape(28, 28)

plt.imshow(im)
plt.show()

print(M[0, 0])  # label = 1

# To show in gray scale
plt.imshow(im, cmap = "gray")
plt.show()

# can reverse the colors like. black on a white background
plt.imshow(255 - im, cmap = "gray")
plt.show()