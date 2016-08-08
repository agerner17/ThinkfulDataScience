from scipy import stats
import collections
import pandas as pd
import matplotlib.pyplot as plt




# Load the reduced version of the Lending Club Dataset
loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')
# Drop null rows


loansData.dropna(inplace=True)

freq = collections.Counter(loansData['Monthly.Income'])

plt.figure()
plt.bar(freq.keys(), freq.values(), width=1)
chi, p = stats.chisquare(freq.values())
print(chi, p)
plt.savefig("chiSquareCredit.png")
