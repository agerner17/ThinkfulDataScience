import matplotlib.pyplot as plt
import statsmodels.api as sm
import pandas as pd
import numpy as np
from IPython import embed as ip




loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

interestRate = loansData['Interest.Rate']

loanLength = loansData['Loan.Length']

ficoRange = loansData['FICO.Range']

#.values[] allows you to print whatever value youd like from the array

#cleaning Interest Rates Data
interestRateCleaned = interestRate.map(lambda x: round(float(x.rstrip('%')) / 100, 4))
loansData['Interest.Rate'] = interestRateCleaned

#cleaning loan length  Data
loanLengthCleaned = loanLength.map(lambda x: int(x.rstrip('months'))) # Notice this ^dtype: int64^ means the data type is an integer. This is what we want. This is why we put int in front of the rstrip.
loansData['Loan.Length'] = loanLengthCleaned

#cleaning Fico Range 
ficoRangeCleaned = ficoRange.map(lambda x: x.split('-'))
ficoRangeCleaned = ficoRangeCleaned.map(lambda x: [int(n) for n in x])

#Adjusting CSV file
loansData['FICO.Score'] = ficoRangeCleaned.map(lambda x: int(x[0]))

loansData.to_csv('loansData_clean.csv', header=True, index=False)

loansData['IR_TF'] = 0 + (loansData['Interest.Rate'] <= 0.12)

loansData['Intercept'] = 1

ind_vars = ['Intercept', 'FICO.Score', 'Amount.Requested']

logit = sm.Logit(loansData['IR_TF'], loansData[ind_vars])
result = logit.fit()
coeff = result.params

print(coeff)

confidenceInterval = result.conf_int()

loansData["IR_TF"][loansData['Interest.Rate'] < 0.10].head() # should all be True
loansData["IR_TF"][loansData['Interest.Rate'] > 0.13].head() # should all be False

#1/(1 + e^(intercept + 0.087423(FicoScore) − 0.000174(LoanAmount))

def logistic_function(fico_score, loan_amount, coefficients):
    #'Calculate the probability to have a given loan with a given fico score\ at an interest <= 12%'
    b, a1, a2 = coefficients   
    x = b + a1*fico_score + a2*loan_amount
    p = 1./(1.+np.exp(-x))
    return p
"""
Determine the probability that we can obtain a loan at ≤12% Interest for $10,000 with a FICO score of 720 using this function.
"""
p1 = logistic_function(720, 10000, coeff)

print "Probability that we can obtain a loan at ≤12% Interest for $10,000 with a FICO score of 720"
print "p = ", p1

"""
Is p above or below 0.70? Do you predict that we will or won't obtain the loan?
"""
print "p > 0.70?"
print p1 > 0.70

"""
If you're feeling really adventurous, you can create a new function pred to predict whether or not we'll get the loan automatically.
"""
def future(fico_score, loan_amount, coefficients):
    return logistic_function(fico_score, loan_amount, coefficients) > 0.70

p2 = logistic_function(500,90000, coeff)
print "Are we getting a loan at ≤12% Interest for $90,000 with a FICO score of 500"
print(p2)
print future(500, 90000, coeff)
