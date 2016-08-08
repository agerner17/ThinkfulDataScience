import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats


loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

loansData.dropna(inplace=True)

print(loansData)

loansData.boxplot(column='Amount.Requested')
plt.savefig("boxPlotRequested.png")

loansData.hist(column='Amount.Requested')
plt.savefig("histogramRequested.png")

plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.savefig('amountRequest.png')


#The requested and actually funded data have a lot of similarites.  They share a normal distribution which we clearly see in the QQ-plot.  
#The histogram looks very similar. Small differences on some of the columns which makes sense because the bank may have not given all of the requested funds from the higher requests, and only gave them a portion of the requested amount. Thats why you see the 10000 amount spike up a little, while the higher amounts like 15000 and 20000 drop.
# The box plot data was interesting to see because while the the 25th and 75th percentiles tighented around the 50% mark of 10000, we saw a lot more outliers than in the Requested data. 