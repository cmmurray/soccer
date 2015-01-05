#Simport psycopg2
import csv
import urllib2
import os

years = []
yearFormat = '%02d%02d' 
baseAddress = 'http://www.football-data.co.uk/mmz4281/'

for i in range(93,117):
	year = yearFormat %(i % 100,(i+1) % 100)
	years.append(year)

filenames = {"E0", "E1", "E2", "E3", "EC", "SP1", "SP2", "I1", "I2","SC0", "SC1","SC2","SC3","D1","D2","F1","F2","N1","B1","P1","T1","G1"}
allFiles = []
for year in years:
	for filename in filenames:
		allFiles.append(baseAddress + year + '/' + filename + ".csv")

downloadedFiles = []
for fileurl in allFiles:
	filename = fileurl.split('/')[-2] + fileurl.split('/')[-1]
	filePath = './Data/' + filename
	if not os.path.exists(filePath):
		try:
			response = urllib2.urlopen(fileurl)
			output = open(filePath, 'wb')
			output.write(response.read())
			output.close()
			print "Got file : " + filename
			downloadedFiles.append(filePath)
		except StandardError:
			print "Error :" + filename
	else:
		downloadedFiles.append(filePath)
		print "Already have : " + filename



