import pandas as pd
loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

interestRate = loansData['Interest.Rate'][0:5]


#.values[] allows you to print whatever value youd like from the array


x = interestRate.values[1]

x = x.rstrip('%')  # Removes the % from the end

x = float(x)

x = x / 100 # because this is a percentage

x = round(x , 4) # We don't need that much precision, round to 4 digit


print(x)