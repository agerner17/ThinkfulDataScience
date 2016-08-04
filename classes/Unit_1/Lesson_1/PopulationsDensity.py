import collections

density_dict = collections.defaultdict(int)

population_table_1990 = dict()
population_table_2000 = dict()
population_table_2010 = dict()

landarea_table = dict()

with open('data/lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
    header = next(inputFile)
    for line in inputFile:
        line = line.rstrip().split(',')
        line[3] = float(line[3])
        line[4] = float(line[4])
        line[5] = float(line[5])
        line[7] = float(line[7])
        if line[1] == 'Total National Population':
            if line[0] in population_table_1990: 
                population_table_1990[line[0]] += line[3] 
            else:
                population_table_1990[line[0]] = line[3] 
            if line[0] in population_table_2000: 
                population_table_2000[line[0]] += line[4] 
            else:
                population_table_2000[line[0]] = line[4] 
            if line[0] in population_table_2010: 
                population_table_2010[line[0]] += line[5] 
            else:
                population_table_2010[line[0]] = line[5] 
            if line[0] in landarea_table: 
                landarea_table[line[0]] += line[7] 
            else:
                landarea_table[line[0]] = line[7]

for key in landarea_table:
    density_1990 = population_table_1990[key] / landarea_table[key]
    density_2000 = population_table_2000[key] / landarea_table[key]
    density_2010 = population_table_2010[key] / landarea_table[key]
    density_list = [density_1990, density_2000, density_2010] 
    density_list_string = str(density_list)
    density_dict[key] = density_list_string

print density_dict