#!/usr/bin/env python
import re
import csv

import sys                                                                  
reload(sys)
sys.setdefaultencoding("utf-8")

aggregate = []
header = [['Closing (Year)','Place','History Lost (Years)','Reason','Location']] 

for i in range (2000,2015):
	year = str(i)
	readFile = open('txt/'+ year+'.txt','r')

	placetime = []
	reason = []
	location = []
	for i, line in enumerate(readFile):
		if line != "" and line !="\n":
			if i%3>0: # reason and location data 
				data = line.rstrip().split(';')
	   			reason.append(data[0])
	   			if len(data) > 1:
	   				location.append(data[1]) 
	   			else:
	   				location.append('') 
	   		elif i%3==0: # place and year data
	   			line = re.sub(r'\xe2\x80\x99','\'',line)
	   			line = [year] + line.split(':') # year integer inlcuded
	   			line[2] = re.sub(r'[a-zA-Z\s]*','',line[2])
	   			placetime.append(line)

	for k, v in enumerate(placetime):
		placetime[k].append(reason[k])
		placetime[k].append(location[k])

	aggregate += placetime

	placetime = [['Closing (Year)','Place','History Lost (Years)','Reason','Location']] + placetime

	readFile.close()

	print len(placetime)
	print placetime

	with open("./csv/"+year+".csv", "wb") as f:
	    writer = csv.writer(f)
	    writer.writerows(placetime)


with open("vanishingny.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(header + aggregate[::-1])


