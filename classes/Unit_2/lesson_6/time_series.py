from matplotlib import pyplot as plt
import pandas as pd
import numpy as np 
import statsmodels.api as sm
from pandas.tools.plotting import autocorrelation_plot



df = pd.read_csv('LoanStats3b.csv', header=1, low_memory=False)

# converts string to datetime object in pandas:
df['issue_d_format'] = pd.to_datetime(df['issue_d']) 
dfts = df.set_index('issue_d_format') 
year_month_summary = dfts.groupby(lambda x : x.year * 100 + x.month).count()

#first column is the year 201201 is january 2012
loan_count_summary = year_month_summary['issue_d']
#values is important to be able to graph the data
values = loan_count_summary.values
print(values)

plt.plot(loan_count_summary.values)
plt.xlabel("Month")
plt.ylabel("Num_Loans")
plt.savefig("Not_Stationary.png")
#it is clear that this data is not stationary because of the exponential growth trend from the graph.

fig = plt.figure(figsize=(12,8))
ax1 = fig.add_subplot(211)
sm.graphics.tsa.plot_acf(values)
plt.savefig("AutoCorrelation.png")

#because there are two spikes in the autocorrelation graph we can assume there are two parameters to be fitted in the auto-regressive models

ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(values)
plt.savefig("Partial_AutoCorrelation.png")

#because there are two spikes in the partial-autocorrelation graph we can assume there are two parameters to be fitted in the moving-average models


