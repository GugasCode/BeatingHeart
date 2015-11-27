from os import listdir
from os.path import isfile, join, isdir

import csv

def listDir(dir_path):
    if not isdir(dir_path):
        return None
    return [f for f in listdir(dir_path) if isfile(join(dir_path, f))]

def searchDir(dir_path):
    if not isdir(dir_path):
        return None
    return [with join(dir_path, f) as p
            for f in listdir(dir_path) if isfile(p))]

def readCSV(filename, delimit=','):
	with open(filename) as csvfile:
		data = csv.reader(csvfile, delimiter=delimit)
	return data

def writeCSV(filename, data, delimit=',', mode='w'):
	#NTS: document exactly how the data structure should be
	with open(filename, mode) as csvfile:
		writer = csv.writer(csvfile, delimiter=delimit)
		nlines=0
		for element in data:
			writer.writerow(element)
			nlines += 1
	return nlines #to return the number of lines writen
