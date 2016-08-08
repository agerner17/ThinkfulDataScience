import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt 
import collections


test_data = np.random.normal(size=100)

## FREQUENCY 
c = collections.Counter(test_data)

count_sum = sum(c.values())

for k,v in c.iteritems():
  print("The frequency of number " + str(k) + " is " + str(float(v) / count_sum))

##BOXPLOT

plt.boxplot(test_data)

plt.savefig("prob.png")

##HISTOGRAM

plt.hist(test_data, histtype='bar')

plt.savefig("histogram.png")


##QQ-PLOT

plt.figure()#this is for data set 1
test_data = np.random.normal(size=1000)
graph1 = stats.probplot(test_data, dist ="norm", plot = plt)
plt.savefig("normalDistribution.png") #this will generate the first graph


plt.figure()#this is for data set 2
test_data2 = np.random.uniform(size=100)
graph2 = stats.probplot(test_data2, dist = "norm", plot = plt)
plt.savefig("uniformDistribution.png") #this will generate the second graph


