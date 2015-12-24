from os import listdir
from os.path import isfile, join, isdir

import csv
import numpy as np

def listDir(dir_path):
    if not isdir(dir_path):
        return None
    return [f for f in listdir(dir_path) if isfile(join(dir_path, f))]

def searchDir(dir_path):
    if not isdir(dir_path):
        return None
    return [join(dir_path, f)\
            for f in listdir(dir_path) if isfile(p)]

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
    return nlines

def grabFile(filepath):
	"""
	Function that will grab the contents of a file and puts them in a numpy
	array with two dimensions.
	"""
	content = np.array([[],[]])
	content[0], content[1] = np.loadtxt(filepath, unpack=True, delimiter=',')
	return content

def save(outfile, data):
	np.save(outfile, data)

def load(infile):
	return np.load(infile)
