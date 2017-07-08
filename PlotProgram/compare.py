from scipy.stats import norm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np
import scipy
import statistics

# read data from a text file. One number per line

import sys

# get argument list using sys module
sys.argv
if (len(sys.argv)>2):
    print("arg true")
    dataPoints = str(sys.argv[1])
    dataPoints2 = str(sys.argv[2])
else:
    exit(0)


dataArray = []
for item in open(dataPoints,'r'):
    item = item.strip()
    if item != '':
        try:
            dataArray.append(float(item)/1000.0)
        except ValueError:
            pass
dataArray2 = []
for item in open(dataPoints2,'r'):
    item = item.strip()
    if item != '':
        try:
            dataArray2.append(float(item)/1000.0)
        except ValueError:
            pass
# best fit of data
(mu, sigma) = norm.fit(dataArray)
(mu2, sigma2) = norm.fit(dataArray2)
sigma1 = np.std(dataArray, ddof = 1)
median = statistics.median(dataArray)

# the histogram of the data
n, bins, patches = plt.hist(dataArray, 500, normed=1, facecolor='green', alpha=0.5)
n2, bins2, patches2 = plt.hist(dataArray2, 500, normed=1, facecolor='blue', alpha=0.5)
# add a 'best fit' line
y = mlab.normpdf( bins, mu, sigma)
y2 = mlab.normpdf( bins2, mu2, sigma2)
l = plt.plot(bins, y, 'g--', linewidth=2)
l = plt.plot(bins2, y2, 'b--', linewidth=2)

#plot
plt.xlabel('Latency (ms)')
plt.ylabel('Probability')
plt.title(r'$\mathrm{Stick\ to\ servo\ latency:}\ \mu=%.3f,\ \sigma=%.3f, median=%.3f,$' %(mu, sigma, median))
plt.grid(True)

plt.show()
