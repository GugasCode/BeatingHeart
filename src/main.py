import sys
import argparse
import numpy as np
import pulses as pul
import filters as flt
import utils.waves as wave
import utils.files as files
import utils.charts as chart

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
    frames = stdClean(frames)
    return pul.findBeats(frames, 4, 6)

def insertName(path, name, mode='w'):
    f = open(path, mode)
    f.write(name + ',')
    f.close()

if __name__ == '__main__':
    path = sys.argv[1]
    output = "data.xls"
    f = files.listDir(path)
    for i in f:
        print(i)
        result = stdRun(path + i)
        insertName(output, i, mode='a')
        final = result[0]*2
        files.writeCSV(output, final, mode='a')
        for n in range(result[0].size):
            print(result[0][n]*2)
        print("n beats: " + str(result[1].size))
