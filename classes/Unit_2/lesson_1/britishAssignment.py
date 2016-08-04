import pandas as pd
from scipy import stats


data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''

data = data.splitlines()

data = [i.split(',') for i in data]

column_names = data[0] # this is the first row

data_rows = data[1::] # these are all the following rows of data

df = pd.DataFrame(data_rows, columns=column_names)

#MEAN     MEDIAN      MODE 
df['Alcohol'] = df['Alcohol'].astype(float)

df['Tobacco'] = df['Tobacco'].astype(float)

print("Alcohol Mean", df['Alcohol'].mean())

print("Alcohol Median", df['Alcohol'].median())


print("Tobacco Mean", df['Tobacco'].mean())

print("Tobacco Median", df['Tobacco'].median())

print("Alcohol Mode", stats.mode(df['Alcohol']))

print("Tobacco Mode", stats.mode(df['Tobacco']))



# RANGE/VARIANCE/STANDARD DEVIATION  
#We use the std() function to calculate the standard deviation in pandas and the var() function to calculate the variance.

max(df['Alcohol']) - min(df['Alcohol'])
# 2.4500000000000002
df['Alcohol'].std() 
# 0.79776278087252406
df['Alcohol'].var() 
# 0.63642545454546284

max(df['Tobacco']) - min(df['Tobacco'])
# 1.8499999999999996
df['Tobacco'].std() 
# 0.59070835751355388
df['Tobacco'].var() 
# 0.3489363636363606

