import csv
import pandas as pd

input_dataframe = pd.read_csv('data/lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv')	

print(input_dataframe[0:10])

#for panadas remember that it only prints out the last print... not sure on why that it is but keep in mind 
print(input_dataframe['Continent'])
