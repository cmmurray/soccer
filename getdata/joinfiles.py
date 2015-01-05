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
			lbcount = 0
			for item in row:
				#LB Fix - in german data LBH, LBD and LBA all have the the col name LB
				lbdict = {0: 'LBH', 1: 'LBD', 2: 'LBA'}
				if item == 'LB':
					item = lbdict[lbcount]
					lbcount += 1
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
		headers = []
		print 'processing file '+ f
		for row in reader:
			if not header:
				#print row
				newrow = ['NA'] * len(allColumns)
				for item in enumerate(row):
					if item[1] == "" or item[1] == ' ':
						continue
					if item[0] > len(headers):
						print 'data in this row does not have a header: ', row
						break
					#print item
					index = allColumns.index(headers[item[0]])
					newitem = item[1].replace(",","").replace(" ","")
					newrow[index] = newitem
				if newrow[0] != 'NA':
					master.write(','.join(str(element) for element in newrow)+'\n')
			else:
				lbcount = 0
				for item in row:
					#LB Fix - in german data LBH, LBD and LBA all have the the col name LB
					lbdict = {0: 'LBH', 1: 'LBD', 2: 'LBA'}
					if item == 'LB':
						item = lbdict[lbcount]
						lbcount += 1
					col = item.strip()
					if col not in headers and col != "":
						headers.append(col)
				header = False


master.close()

	