import csv
import urllib2
import os
from os import listdir

masterpath = './Data/master.csv'
if os.path.exists(masterpath):
 	os.remove(masterpath)

master = open(masterpath,'wb')

filedir = './Data/'
allColumns = []
for f in listdir(filedir):
	if not f.endswith('.csv'): 
		continue
	with open('./Data/'+f,'rb') as csvfile:
		reader = csv.reader(csvfile,delimiter = ',')
		for row in reader:
			for item in row:
				col = item.strip()
				if col not in allColumns and col != "":
					allColumns.append(col)
			break

master.write(','.join(allColumns)+ '\n')

for f in listdir(filedir):
	if not f.endswith('.csv') or f.startswith('master'): 
		continue
	with open('./Data/'+f,'rb') as csvfile:
		reader = csv.reader(csvfile,delimiter = ',')
		header = True
		print 'processing file '+ f
		for row in reader:
			if not header:
				newrow = ['NA'] * len(allColumns)
				itemindex = 0
				for item in row:
					index = allColumns.index(allColumns[itemindex])
					if item == "" or item == ' ':
						continue
					item = item.replace(",","").replace(" ","")
					newrow[index] = item
					itemindex += 1
				if newrow[0] != 'NA':
					master.write(','.join(str(element) for element in newrow)+'\n')
			else:
				headers = row
				header = False


master.close()

	