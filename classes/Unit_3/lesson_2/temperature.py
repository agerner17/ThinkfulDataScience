import time
import calendar
import requests
import sqlite3 as lite
import time
import datetime
from datetime import datetime as dt
import collections
from dateutil.parser import parse
from pandas.io.json import json_normalize
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



api_key = ('1f588dc060e301460180fb980d7752dd')

cur_time = calendar.timegm(time.gmtime())

url = "https://api.forecast.io/forecast/" + api_key

cities = { "Atlanta": '33.762909,-84.422675',
            "Austin": '30.303936,-97.754355',
            "Boston": '42.331960,-71.020173',
            "Chicago": '41.837551,-87.681844',
            "Cleveland": '41.478462,-81.679435'}


########################## DATABASE ##########################

con = lite.connect("weather.db")
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS city_temp")
cities.keys()
with con:
	cur.execute('CREATE TABLE city_temp(count INT, city TEXT, time  INT, max_temp INT, min_temp INT, mean INT, median INT, range INT, hourly_temps TEXT, hourly_times TEXT, UNIQUE (count, city,time,max_temp, range))')

dataEntry = "INSERT into city_temp(count, city, time, max_temp, min_temp, mean, median, range, hourly_temps, hourly_times) VALUES (?,?,?,?,?,?,?,?,?,?)"

end_date = datetime.datetime.now()
start_date = datetime.timedelta(days=30)
query_date = end_date - start_date

count = 0

for k,v in cities.iteritems():
	query_date = end_date - datetime.timedelta(days=30)
	#print "\nCity: {} Coord: {}".format(k,v)
	while query_date < end_date:
		#print "start_time: {}   type: {}\n".format(query_date,type(query_date))
		req_url = url + '/' + v +',' + query_date.strftime('%Y-%m-%dT%H:%M:%S')
		r = requests.get(req_url)
		#print "{}\n".format(req_url)
		df = json_normalize(r.json())
		#print "{}\n".format(df.columns)
		max = 0
		min = 300
		for i in df["hourly.data"][0]:
			temp_list = []
			for i in df['hourly.data'][0]: temp_list.append(i['temperature'])

			hour_list = []
			for i in df['hourly.data'][0]: 
				hour_list.append(i['time'])
			for t in temp_list:
				if t > max:
					max = t
				if t < min:
					min = t
		query_date += datetime.timedelta(days = 1)#increment query_date to the next day for next operation of loop
		count =  count +1 

		with con:

			cur.execute(dataEntry,(count, k, dt.fromtimestamp(i['time']).strftime('%Y-%m-%d T %H:%M:%S'),max,min,np.mean(temp_list),np.median(temp_list),abs(max-min),str(temp_list).strip('[]'),str(hour_list).strip('[]')))

		#print count, k, dt.fromtimestamp(i['time']).strftime('%Y-%m-%d %T'), max, min, np.mean(temp_list), np.median(temp_list), abs(max - min)

con.close()

###########################################ANALYSIS OF DATA ##############################################



con = lite.connect("weather.db")
cur = con.cursor()

df = pd.read_sql_query("SELECT * FROM city_temp ORDER BY count", con, index_col = "count")

boston = (df['city'] == 'Boston')
Atlanta = (df['city'] == 'Atlanta' )
austin = (df['city'] == 'Austin' )
chicago = (df['city'] == 'Chicago' )
cleveland = (df['city'] == 'Cleveland' )


max_range=0
max_city=0
max_day=''
temps=''
times=''
max_temp = 0
min_temp = 0
maxTemp = []
maxDay = []



for i in df.index:
    if df['range'][i] > max_range:
       max_range=df['range'][i]
       max_city=df['city'][i]
       max_day = i
       temps=df['hourly_temps'][i]
       times=df['hourly_times'][i]
    elif df["max_temp"][i] > max_temp:
    	max_city=df['city'][i]
    	max_temp = df["max_temp"][i]
    	max_day = i
    maxDay.append(i)
    maxTemp.append(df["max_temp"][i])

print "\n\n{} had the highest temperature variation of {} of {} study".format(max_city, max_range, max_day)
print "\n\n{} had the highest temperature of {} on {} of study".format(max_city, max_temp, max_day)

print("TABLE")
print("1-30 Boston")
print("31-60 Atlanta")
print("61-90 Cleveland")
print("91-120 Austin")
print("121-150 Chicago")


plt.bar(maxDay, maxTemp)
plt.xlabel("Days of Study")
plt.ylabel("Max Daily Temperature")
plt.show()

exit()






