#!/usr/bin/env python
import re
import csv

import sys                                                                  
reload(sys)
sys.setdefaultencoding("utf-8")


for i in range (2000,2014):
	year = str(i)
	readFile = open('txt/'+ year+'.txt','r')

	placetime = []
	reason = []
	for i, line in enumerate(readFile):
		if line != "" and line !="\n":
			if i%3>0:
	   			reason.append(line.rstrip())
	   		elif i%3==0:
	   			line = re.sub(r'\xe2\x80\x99','\'',line)
	   			line = [year] + line.split(':')
	   			line[2] = re.sub(r'[a-zA-Z\s]*','',line[2])
	   			placetime.append(line)

	for k, v in enumerate(placetime):
		placetime[k].append(reason[k])

	placetime = [['Closing (Year)','Place','History Lost (Years)','Reason']] + placetime


	readFile.close()

	print len(placetime)
	print placetime

	with open("./csv/"+year+".csv", "wb") as f:
	    writer = csv.writer(f)
	    writer.writerows(placetime)

