import requests 
import pandas as pd 
import matplotlib.pyplot as plt 
from pandas.io.json import json_normalize 
import sqlite3 as lite
# a package with datetime objects
import time
# a package for parsing a string into a Python datetime object
from dateutil.parser import parse 
import collections
from datetime import date



r = requests.get('http://www.citibikenyc.com/stations/json')

df = json_normalize(r.json()['stationBeanList'])

#activeStations vs Inactive Stations

condition = (df["statusValue"] == "In Service")

condition1 = (df["statusValue"] == "Not In Service")

averageActiveStation = df[condition]["totalDocks"].mean()

averageInactiveStation = df[condition1]['totalDocks'].mean()

#median 

allStationMedian = df['totalDocks'].median()
medianActiveStation = df[df["statusValue"] == "In Service"]["totalDocks"].median()

"""
print "The average amount of active stations: ",averageActiveStation
print "The average amount of inactive stations: ", averageInactiveStation 
print "The median of active stations is: ",medianActiveStation
"""
#######################################SQL###################################### 

con = lite.connect('citi_bike.db')
cur = con.cursor()
cur.execute("DROP TABLE if exists citibike_reference")
cur.execute("DROP TABLE if exists available_bikes")

#take the string and parse it into a Python datetime object

#a prepared SQL statement we're going to execute over and over again
sql = "INSERT INTO citibike_reference (id, totalDocks, city, altitude, stAddress2, longitude, postalCode, testStation, stAddress1, stationName, landMark, latitude, location) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)"

#extract the column from the DataFrame and put them into a list
stationIds = df['id'].tolist()

#add the '_' to the station name and also add the data type for SQLite
#in this case, we're concatenating the string and joining all the station ids (now with '_' and 'INT' added)
stationIds = ['_' + str(x) + ' INT' for x in stationIds]

### TABLES ###

# create table for citibike reference STATIONARY DATA
def createReferencesTable():
	#for loop to populate values in the database
	with con:
		cur.execute("CREATE TABLE citibike_reference (id INT PRIMARY KEY, totalDocks INT, city TEXT, altitude INT, stAddress2 TEXT, longitude NUMERIC, postalCode TEXT, testStation TEXT, stAddress1 TEXT, stationName TEXT, landMark TEXT, latitude NUMERIC, location TEXT)")

		for station in r.json()["stationBeanList"]:
			#id, totalDocks, city, altitude, stAddress2, longitude, postalCode, testStation, stAddress1, stationName, landMark, latitude, location)
			cur.execute(sql,(station['id'],station['totalDocks'],station['city'],station['altitude'],station['stAddress2'],station['longitude'],station['postalCode'],station['testStation'],station['stAddress1'],station['stationName'],station['landMark'],station['latitude'],station['location']))
createReferencesTable() 

#create table for available bike NONSTATIONARY DATA
def availableBikesTable():
	with con:
		cur.execute("CREATE TABLE available_bikes ( execution_time INT, " +  ", ".join(stationIds) + ");")
		
		for i in range(60):
			r = requests.get('http://www.citibikenyc.com/stations/json')
    	exec_time = parse(r.json()['executionTime']).strftime("%s")

    	cur.execute('INSERT INTO available_bikes (execution_time) VALUES (?)', (exec_time,))
    	counter = 1
			#loop through the stations in the station list
    	for station in r.json()['stationBeanList']:
    		cur.execute("UPDATE available_bikes SET _%d = %d WHERE execution_time = %s" % (station['id'], station['availableBikes'], exec_time))
    		print(counter, station['id'], station['availableBikes'])

			#iterate through the defaultdict to update the values in the database
    	con.commit()
    	counter = counter + 1 

    	time.sleep(60)
			# pause the program for 60 seconds  

availableBikesTable()


###/TABLES###

