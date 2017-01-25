import numpy as np
from scipy.stats import norm, multivariate_normal as mvn
import matplotlib.pyplot as plt

# Scipy is to calculate Gaussian PDF for instance
# It is just a faster way to calculate such things

norm.pdf(0)

# mean other than zero, variance other than 1
norm.pdf(0, loc=5, scale=10)
# mean = 5, standard deviation = 10

# PDFs of many different value in array
# No need to do it in a loop
r = np.random.randn(10)
norm.pdf(r)  # pdf of all values at the same time

#  Usually we need a log PDF
#  With log we can add up all probabilities together
#  Adding operation is cheaper than multiplication
#  So it is advantageous to work with log PDF

norm.logpdf(r)

# CDF accumulative distribution function
# Compute numerically

norm.cdf(r)
norm.logcdf(r)

#  Sampling from a Gaussian distribution (1-D)
g = np.random.randn(100000)
#  one can check that it will be normally distributed. use plotting

#  What if i want to sample from a Gaussian distribution that has an arbitrary mean and standard deviation
#  Use the same function but scale it (10) and add mean (5)
g = 10*np.random.randn(10000) + 5

plt.hist(g, bins=100)
plt.show()

#  Sampling from a Gaussian distribution (Spherical and Axis Aligned Elliptical)
#  In ML a lot of work deals with multidimensional data
#  We can use the same func but adding more dimensions

r = np.random.randn(10000, 2)
plt.scatter(r[:, 0], r[:, 1])
plt.show()  # pretty much like a circle

#  Elliptical Gaussian. Where the scale is different for different dimensions
r[:, 1] = 5*r[:, 1] + 2
plt.scatter(r[:, 0], r[:, 1])
# plt.show()  # ellipse

#  Make axes equal
plt.axis('equal')
plt.show()


#  Now make real use of Scipy
#  Sampling from a General Multivariate Normal
#  Dimensions are not necessarily independent on each other

cov = np.array([[1, 0.8], [0.8, 3]])
mu = np.array([0, 2])

# Look at the Scipy documentation
r = mvn.rvs(mean=mu, cov=cov, size=1000)

plt.scatter(r[:, 0], r[:, 1])
plt.axis('equal')
plt.show()

r = np.random.multivariate_normal(mean=mu, cov=cov, size=1000)
plt.scatter(r[:, 0], r[:, 1])
plt.axis('equal')
plt.show()


# Other scipy functions

# scipy.io.loadmat  # opens matlab data files

# Read sound file
# scipy.io.wavfile.read # or write

# Signal Processing
# Convolution
# scipy.signale.convolve
# for images scipy.signal.convolve2d

# Fast Fourier Transform is not is Scipy but in Numpy
# Convert from a time domain to frequency domain
# Example:

# Create a sic wave with multiple frequencies
x = np.linspace(0, 100, 10000)
y = np.sin(x) + np.sin(3*x) + np.sin(5*x)

plt.plot(y)
plt.show()

Y = np.fft.fft(y)
plt.plot(np.abs(Y))

plt.show()

# Find what frequencies are represented. Two spikes in x 16, 48 and 80. These are the original frequencies
print(2*np.pi*16/100)

print(2*np.pi*48/100)

