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
if (len(sys.argv)>1):
    print("arg true")
    dataPoints = str(sys.argv[1])
else:
    print("arg false")
    dataPoints = "data.txt"


dataArray = []
for item in open(dataPoints,'r'):
    item = item.strip()
    if item != '':
        try:
            dataArray.append(float(item)/1000.0)
        except ValueError:
            pass

# best fit of data
(mu, sigma) = norm.fit(dataArray)
sigma1 = np.std(dataArray, ddof = 1)
median = statistics.median(dataArray)

# the histogram of the data
n, bins, patches = plt.hist(dataArray, 500, normed=1, facecolor='green', alpha=0.75)

# add a 'best fit' line
y = mlab.normpdf( bins, mu, sigma)
l = plt.plot(bins, y, 'r--', linewidth=2)

#plot
plt.xlabel('Latency (ms)')
plt.ylabel('Probability')
plt.title(r'$\mathrm{Stick\ to\ servo\ latency:}\ \mu=%.3f,\ \sigma=%.3f, median=%.3f,$' %(mu, sigma, median))
plt.grid(True)

plt.show()
