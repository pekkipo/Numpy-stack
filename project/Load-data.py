# Turn csv data into a matrix

import numpy as np
import pandas as pd

X = []

# data_2d.csv has 100 lines and 3 columns


# Usual way of loading data in Python
for line in open("resource/data_2d.csv"):
    row = line.split(',')
    sample = list(map(float, row))  # map applies func to all items (here rows)
    # in Python 3 map returns map object, so converted it into a list
    X.append(sample)

X = np.array(X)
print(X.shape)  # gives (100,3)


# LOADING DATA WITH PANDAS
# Pandas is a lot like R
# A lot of features, but here mostly the loading of data and immediate conversion into a Numpy array is considered

Y = pd.read_csv("resource/data_2d.csv", header=None)  # consult Pandas docs for arguments
print(type(Y))
# read_csv returns an object of type DataFrame
print(Y.info())

# Preview of a data set. Prints a first ew rows. Number of rows can be specified like Y.head(10)
print(Y.head())

# To access a certain data we can:
# Convert it to a matrix
M = Y.as_matrix()
print(type(M))  # returns numpy array rather than numpy matrix

# Access the entire column
print(Y[0])  # in Numpy array Y[0] this would give us the first ROW
             # in Pandas Y[0] gives us the first COLUMN (column that has a name 0)

print(type(Y[0]))  # gives us a Series type

# How to get a row in Pandas?
one_row = Y.iloc[0]
# or
one_row = Y.ix[0]
# These are also of type Pandas Series

# Select more than one column
# 0th and the 2nd columns. (By order 1st and 3rd)
two_columns = Y[[0, 2]]
print(two_columns)

# Find all the rows with a data for the 0th columns is less than 5
print(Y[ Y[0] < 5 ])
# this will give rows where in 0th column the value is less than 5

# Can get the booleans like
print(Y[0] < 5)  # this will show all rows showing where the condition is True of False
# type: Series

# Column Names
df = pd.read_csv("resource/international-airline-passengers.csv", engine="python", skipfooter=3)
print(df)
print(df.columns)  # column names are ugly

# Reassign column names passing the list
df.columns = ["month", "passengers"]

# Access a column by its name
print(df["passengers"])

# Alternative method when column names are strings
print(df.passengers)
# Wouldnt have worked if column name contains spaces

# ADDING A COLUMN
df['ones'] = 1  # adds new column named ones and each row contains 1

print(df.head())
