from os import listdir
from os.path import isfile, join, isdir
import numpy as np

import csv

def listDir(dir_path):
    if not isdir(dir_path):
        return None
    return [f for f in listdir(dir_path) if isfile(join(dir_path, f))]

def getDir(dir_path):
    if not isdir(dir_path):
        return None
    return [f for f in listdir(dir_path) if isdir(join(dir_path, f))]

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
        writer.writerow(data.astype(int))
        nlines += 1
        csvfile.close()
    return nlines

def write(filename, data):
    f = open(filename, "w")
    for i in range(len(data[0])):
        f.write(str(data[0][i]) + "," + str(data[1][i]) + "\n")
    f.close()

def reader(filename):
    f, fi = np.loadtxt(filename, unpack=True, delimiter=',')
    return np.append([np.array(f, np.int32)], [np.array(fi, np.int32)], axis=0)
