import pandas as pd 
import statsmodels.formula.api as smf
from IPython.core.display import HTML



df = pd.read_csv("http://statweb.stanford.edu/~tibs/ElemStatLearn/datasets/SAheart.data", index_col = 0)

# copy data and separate predictors and response
X = df.copy()
y = X.pop('chd')
print(df.head())

"""
The variable famhist holds if the patient has a family history of coronary artery disease. 
The percentage of the response chd (chronic heart disease ) for patients with absent/present family history 
of coronary artery disease is:
"""
# compute percentage of chronic heart disease for famhist
meanHeartDisease = y.groupby(X.famhist).mean()

"""
These two levels (absent/present) have a natural ordering to them, so we can perform linear regression on them,
 after we convert them to numeric. This can be done using pd.Categorical.

"""
# encode df.famhist as a numeric via pd.Factor
df['famhist_ord'] = pd.Categorical(df.famhist).labels
est = smf.ols(formula="chd ~ famhist_ord", data=df).fit()

def short_summary(est):
    return HTML(est.summary().tables[1].as_html())

# fit OLS on categorical variables children and occupation
est = smf.ols(formula='chd ~ C(famhist)', data=df).fit()


"""
After we performed dummy encoding the equation for the fit is now:

ŷ =Intercept+C(famhist)[T.Present]×I(famhist=Present)y^=Intercept+C(famhist)[T.Present]×I(famhist=Present)
where I is the indicator function that is 1 if the argument is true and 0 otherwise.

Hence the estimated percentage with chronic heart disease when famhist == present is 0.2370 + 0.2630 = 0.5000 and the estimated percentage with chronic 
heart disease when famhist == absent is 0.2370.

This same approach generalizes well to cases with more than two levels. For example, if there were entries in our dataset with famhist equal to 'Missing' we could create two 'dummy' variables, one to check if famhis equals 
present, and another to check if famhist equals 'Missing'.

"""