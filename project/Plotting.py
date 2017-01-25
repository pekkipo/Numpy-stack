import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Line chart

# Create a data points for x axis
x = np.linspace(0, 10, 100)  # start ending points in between

y = np.sin(x)  # element by element

plt.plot(x, y)
plt.xlabel("Time")
plt.ylabel("Function of time")
plt.title("Chart")

plt.show()



# In machine learning we do approximation
# Scatterplot

A = pd.read_csv('resource/data_1d.csv', header=None).as_matrix()

x = A[:, 0]  # select everything in that dimension (like in Matlab)
y = A[:, 1]  # select all samples but only second column

plt.scatter(x,y)
# plt.show()

# Line and scatter on the same plot
x_line = np.linspace(0, 100, 100)
y_line = 2*x_line + 1

plt.plot(x_line, y_line)

plt.show()


# Histogram
# Discretized probability distribution

plt.hist(x)
plt.show()

R = np.random.random(10000)
plt.hist(R, bins=20)  # bins - number of columns in a hist
plt.show()

# Assumption in a linear regression - the error is normally distributed
# Take y data points and subtract it from its corresponding place on a fitted line.
# Make a histogram

y_actual = 2*x + 1
residuals = y - y_actual

plt.hist(residuals)
plt.show()




