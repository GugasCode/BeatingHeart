import sys
import argparse
import numpy as np
import pulses as pul
import filters as flt
import utils.waves as wave
import utils.files as files
import utils.charts as chart
from classifiers import Bayes, KNN, formatting, confusionMatrix
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

def convertToSCV(inputFolder, outputFolder):
    """
        Standard function to convert wave files in folders
        to their respective csv files
    """
    src = files.listDir(inputFolder)
    for f in src:
        waves = wave.loadWave(inputFolder+f)
        frames = wave.getSamples(waves)
        files.write(outputFolder + f[:-4] + ".csv", frames)

def stdMovArg(data):
    """
        A good standard to run the moving average filter passes
    """
    data = flt.movingAverage(data, 4)
    data = flt.movingAverage(data, 8)
    data = flt.movingAverage(data, 6)
    data = flt.movingAverage(np.fliplr(data), 4)
    data = flt.movingAverage(data, 8)
    data = flt.movingAverage(data, 6)
    return np.fliplr(data)

def stdClean(data):
    """
       Standard run using the clean function for each sound file
    """
    frames = flt.clean(data)
    frames = stdMovArg(frames)
    frames = flt.halfRate(frames)
    return flt.norm(frames)

def stdRun(path, graph=True):
    frames = files.reader(path)
    # if graph:
    #     chart.drawGraphJob(frames)
    frames = stdClean(frames)
    if graph:
        chart.drawGraphJob(frames)
    return pul.findBeats(frames, 4, 6)

def stdShannonRun(path, graph=True, reader=True):
    if reader:
        frames = files.reader(path)
    else:
        frames = path
    # if graph:
    #     chart.drawGraphJob(frames)
    frames = flt.halfRate(frames)
    frames = flt.norm(frames)
    frames = stdMovArg(frames)
    frames = flt.shannon(frames)
    frames = flt.avgShannon(frames, 40, 20)
    if graph:
        chart.drawGraphJob(frames)
    # return pul.findBeats(frames, 4, 6)
    return frames

def insertName(path, name, mode='w'):
    f = open(path, mode)
    f.write(name + ',')
    f.close()

def saveFile(path):
    """
        Saves the results in a specific file format.
        For latter comparison
    """
    output = "data.xls"
    f = files.listDir(path)
    for i in f:
        result = stdRun(path + i)
        insertName(output, i, mode='a')
        final = result[0]*2
        files.writeCSV(output, final, mode='a')

def classify(path, clas):
    """
        Makes a tuple with the file name, its frames and its classification
    """
    f = files.listDir(path)
    res = []
    j = 0
    for i in f:
        frames = files.reader(path + "/" + i)
        res.append([i,frames,clas])
        if j > 10:
            break
        j += 1
        # break#TODO: remove this
    return res

def stdClassify(path, folders):
    """
        Makes a list of tuples with all files classified for use in training and
        test.
    """
    l = []
    for p in folders:
        l.extend(classify(path+p, p))
        # break#TODO: remove this
    return l

def makeSets(data, perc=80):
    """
        Makes a test and training set from a list of all files,
        the devision is given by the perc(entage) attribute that specifies
        how much of the total will be used for the training set.
        The selection itself is made at random.
    """
    size = int(len(data) * (perc/100))
    test = []
    while len(data) > size:
        rand = randint(0,len(data)-1)
        test.append(data.pop(rand))
    return (test, data)

def stdRunClassify(path):
    """
        Standard run for classify pre given files based on their respective
        folders.
        Returns a tuple with the test and data sets.
    """
    folders = files.getDir(path)
    data = stdClassify(path, folders)
    return makeSets(data)

def runOnClassified(data):
    for i in range(len(data)):
        aux = stdShannonRun(data[i][1], graph=False, reader=False)
        beats = pul.findBeats(aux, 4, 6)
        t1, t2 = pul.getT(aux, beats, flt.distinguish(aux), 0.01)
        t11 = pul.getT11(beats[0], flt.distinguish(aux))
        t12 = pul.getT12(beats[0], flt.distinguish(aux))
        data[i][1] = [[t11],[t12],[t1],[t2]]
    return data

if __name__ == '__main__':
    import os
    path = sys.argv[1]
    folders = files.getDir(path)
    cl = stdClassify(path, folders)
    cl = runOnClassified(cl)
    test, train = makeSets(cl, perc=80)
    print("test",test)
    print("train",train)
    pass
    knn = KNN(train, 1)
    print(test[0])
    formated = formatting(test)
    result = []
    for item in formated:
        classification = knn.classify(item,5)
        print('We got a new one!', classification)
        result.append([item[-1], classification])
    print(result)
    matrix = confusionMatrix(result)
    print(matrix)
    # os.system('speaker-test -c 1 -D plughw:0')
