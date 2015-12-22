import sys
import argparse
import numpy as np
import pulses as pul
import filters as flt
import utils.waves as wave
import utils.files as files
import utils.charts as chart
from random import randint

def main():
    parser = argparse.ArgumentParser(description='Beating Heart Project')
    #parser.add_argument(dest='filenames', metavar='filename',nargs='*')
    #both input and output args optional, use cwd if not supplied or -i
    parser.add_argument('-i',dest='input')
    parser.add_argument('-o',dest='output')
    parser.add_argument('-v',dest='visual')
    parser.add_argument('-c',dest='charts')
    parser.add_argument('-t',dest='params')
    #files like .wav or .csv or .xls
    parser.add_argument('-p',dest='phase')

    args = parser.parse_args()

def stdMovArg(data):
    data = flt.movingAverage(data, 4)
    data = flt.movingAverage(data, 8)
    data = flt.movingAverage(data, 6)
    data = flt.movingAverage(np.fliplr(data), 4)
    data = flt.movingAverage(data, 8)
    data = flt.movingAverage(data, 6)
    return np.fliplr(data)

def stdClean(data):
    frames = flt.clean(data)
    frames = stdMovArg(frames)
    frames = flt.halfRate(frames)
    return flt.norm(frames)

def stdRun(path):
    waves = wave.loadWave(path)
    frames = wave.getSamples(waves)
    chart.drawGraphJob(frames)
    frames = stdClean(frames)
    chart.drawGraphJob(frames)
    return pul.findBeats(frames, 4, 6)

def insertName(path, name, mode='w'):
    f = open(path, mode)
    f.write(name + ',')
    f.close()

def saveFile(path):
    output = "data.xls"
    f = files.listDir(path)
    for i in f:
        print(i)
        result = stdRun(path + i)
        insertName(output, i, mode='a')
        final = result[0]*2
        files.writeCSV(output, final, mode='a')

def classify(path, clas):
    f = files.listDir(path)
    res = []
    for i in f:
        waves = wave.loadWave(path+"/"+i)
        frames = wave.getSamples(waves)
        res.append((i,frames,clas))
    return res

def stdClassify(path, folders):
    l = []
    for p in folders:
        l.extend(classify(path+p, p))
    return l

def makeSets(data, perc=80):
    size = int(len(data) * (perc/100))
    test = []
    while len(data) > size:
        rand = randint(0,len(data)-1)
        test.append(data.pop(rand))
    return (test, data)

if __name__ == '__main__':
    path = sys.argv[1]
    # folders = files.getDir(path)
    # data = stdClassify(path, folders)
    # test, train = makeSets(data)
    output = 'test.csv'
    waves = wave.loadWave(path)
    frames = wave.getSamples(waves)
    files.write(output, frames)
