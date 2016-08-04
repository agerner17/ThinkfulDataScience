from collections import defaultdict

def populations2():
	with open('data/lecz-urban-rural-population-land-area-estimates_country-1km-90m.csv', 'rU') as inputFile:
		header = next(inputFile)

		populationChange_dict = defaultdict(int)
		for line in inputFile:
			line = line.rstrip().split(',')
			line[9] = int(line[9])
			line[11] = float(line[11])
			if line[3] == "Total National Population":
				populationChange_dict[line[1]] += line[11] - line[9]
		print(populationChange_dict)

		inputFile.close()

	with open('national_populationChange.csv', 'w') as outPutFile:
		outPutFile.write('continent, Population_Change\n')
		#we have to write a for loop for a dictionary because while we were modifying the data we change it from a list to a dictionary
		for k , v in populationChange_dict.iteritems():
			#The function iteritems() iterates through each key-value pair in the dictionary. 
			#In this case, we're assigning the key to the variable k and the value to the variable v
			#the population is an integer so we have to convert it to a string (using str())
			#We add the comma to delimit the two and then add the \n to indicate the new line
			outPutFile.write(k + ',' + str(v) + '\n')	
populations2()