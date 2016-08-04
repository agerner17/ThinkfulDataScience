from collections import defaultdict

def popluations():
	with open('lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
	    header = next(inputFile)

	    population_dict = defaultdict(int)

	    for line in inputFile:
	    	line = line.rstrip().split(",")
	    	line[5] = int(line[5])
	    	if line[1] == "Total National Population":
	    		population_dict[line[0]] += line[5]
	    print(population_dict)
	    inputFile.close()	

	with open('national_population.csv', 'w') as outputFile:
		#this line is writing the header for the file
		outputFile.write('continent, 2010_popluation\n')
		#we have to write a for loop for a dictionary because while we were modifying the data we change it from a list to a dictionary
		for k , v in population_dict.iteritems():
			#The function iteritems() iterates through each key-value pair in the dictionary. 
			#In this case, we're assigning the key to the variable k and the value to the variable v
			#the population is an integer so we have to convert it to a string (using str())
			#We add the comma to delimit the two and then add the \n to indicate the new line
			outputFile.write(k + ',' + str(v) + '\n')
popluations()	

	