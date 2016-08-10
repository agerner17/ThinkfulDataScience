import numpy as np
import pandas as pd
import statsmodels.api as sm



loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

interestRate = loansData['Interest.Rate']

loanLength = loansData['Loan.Length']

ficoRange = loansData['FICO.Range']

#.values[] allows you to print whatever value youd like from the array

#cleaning Interest Rates Data
interestRateCleaned = interestRate.map(lambda x: round(float(x.rstrip('%')) / 100, 4))

#cleaning loan length  Data
loanLengthCleaned = loanLength.map(lambda x: int(x.rstrip('months'))) # Notice this ^dtype: int64^ means the data type is an integer. This is what we want. This is why we put int in front of the rstrip.

#cleaning Fico Range 
ficoRangeCleaned = ficoRange.map(lambda x: x.split('-'))

ficoRangeCleaned = ficoRangeCleaned.map(lambda x: [int(n) for n in x])

#Adjusting CSV file
loansData['FICO.Score'] = ficoRangeCleaned.map(lambda x: int(x[0]))


#histogram of fico ranges
#plt.figure()
#p = loansData['FICO.Range'].hist()

#scatter Plot

#a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist') didnt run

#InterestRate = b + a1(FICOScore) + a2(LoanAmount)

intrate = interestRateCleaned
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']


# The dependent variable
y = np.matrix(intrate).transpose()
# The independent variables shaped as columns
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()


x = np.column_stack([x1,x2])


X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

print(f.summary())








