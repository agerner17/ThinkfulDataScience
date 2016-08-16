import pandas as pd 
import numpy as np 
import statsmodels.api as sm 
import matplotlib.pyplot as plt
import collections
import statsmodels.formula.api as smf

###SCRUBING DATA LOAD DATA FROM LOAN LENDING
df =  pd.read_csv('https://raw.githubusercontent.com/Thinkful-Ed/curric-data-001-data-sets/master/loans/loansData.csv', index_col = 0)

df["Annual.Income"] = 12 * df["Monthly.Income"]


annualIncome = df["Annual.Income"] 

interestRate = df["Interest.Rate"]


#changing string variables of OWN/Mortgage into 1's because they own the home, and the rest e.g. RENT is 0 because they are not home owners.
df["Home.Ownership.Num"] = pd.Categorical(df["Home.Ownership"]).codes

homeOwnershipNumber = df["Home.Ownership.Num"] 

#droping rows that have nothing in the column
df.dropna(subset=['Annual.Income', 'Interest.Rate', 'Home.Ownership'], inplace=True)

df['Annual.Income'] = df['Annual.Income'].astype(float)

df['Interest.Rate'] = df['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))



#### Use income (annual_inc) to model interest rates (int_rate)

x1 = np.matrix(df['Annual.Income']).transpose()

x2 = np.matrix(df['Home.Ownership.Num']).transpose()

y = np.matrix(df["Interest.Rate"]).transpose()

x = np.column_stack([x1,x2])


X = sm.add_constant(x)


model = sm.OLS(y, X)
f = model.fit()

print f.summary()


##look at interaction HAVING TROUBLE WITH THIS PART!!!!
"""
est = smf.ols(formula = 'interestRate ~ annualIncome * homeOwnershipNumber',
              data=df).fit()
print est.summary()
"""


plt.figure()
plt.scatter(x1, y)
plt.savefig("Annual_Income_VS_Interest_Rate.png")

plt.figure()
plt.scatter(x2,y)
plt.savefig("Home_OwnerShip_VS_Interest_RATE.png")

plt.figure()
plt.scatter(x2,x1)
plt.savefig("Home_OwnerShip_VS_AnnualIncome")




