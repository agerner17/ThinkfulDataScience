import pandas as pd 
import sqlite3 as lite
import collections
from dateutil.parser import parse 
import datetime 
import matplotlib.pyplot as plt
con = lite.connect("citi_bike.db")
cur = con.cursor()

df = pd.read_sql_query("SELECT * FROM available_bikes ORDER BY execution_time",con,index_col='execution_time')

df = df.dropna()

hour_change = collections.defaultdict(int)

for col in df.columns:
	station_vals = df[col].tolist()
	stationid =col[1:]
	station_change = 0
	#enumerate function returns not only the item in the list but also the index of the item.
	#This allows us to find the value (with index of k) just after it in sequence (k + 1). 
	#We run the loop until k is equal to the index for the second to last element in the list.
	for k,v in enumerate(station_vals):
		if k < len(station_vals) - 1:
			station_change += abs(station_vals[k] - station_vals[k+1])
		hour_change[int(stationid)] = station_change #convert the station id back to integer


def keyWithHighestValue(d):
	"""Find the key with the greatest value"""
	return max(d, key = lambda k: d[k])

# assign the max key to max_station
max_stationChange = keyWithHighestValue(hour_change)


cur.execute("SELECT id, stationname, latitude, longitude FROM citibike_reference WHERE id = ?", (max_stationChange,))
data = cur.fetchone()
print("The most active station is station id %s at %s latitude: %s longitude: %s " % data)
print("With %d bicycles coming and going in the hour between %s and %s" % (
    hour_change[max_stationChange],
    datetime.datetime.fromtimestamp(int(df.index[0])).strftime('%Y-%m-%dT%H:%M:%S'),
    datetime.datetime.fromtimestamp(int(df.index[-1])).strftime('%Y-%m-%dT%H:%M:%S'),
))

print "The station with the most bike traffic is station ",max_stationChange

plt.figure()
plt.xlabel("Station Id")
plt.ylabel("Number of Bikes in Station")
plt.bar(hour_change.keys(), hour_change.values())
plt.savefig("BikeTrafficOneHour.png")