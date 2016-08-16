import pandas as pd 
import numpy as np 
import statsmodels.api as sm 
import statsmodels.formula.api as smf



df_adv = pd.read_csv('http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv', index_col = 0)

X = df_adv[["TV", "Radio"]]
y = df_adv[["Sales"]]
"""
The multiple regression model describes the response as a weighted sum of the predictors:

Sales=β0+β1×TV+β2×Radio


"""
## fit a OLS model with intercept on TV and Radio
X = sm.add_constant(X)
est = sm.OLS(y, X).fit()
est.summary()

# formula: response ~ predictor + predictor
"""
You can also use the formulaic interface of statsmodels to compute regression with multiple predictors. 
You just need append the predictors to the formula via a '+' symbol.
"""
est = smf.ols(formula = 'Sales ~ TV + Radio', data = df_adv).fit

