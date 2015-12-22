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

if __name__ == '__main__':
    waves = wave.loadWave(sys.argv[1])
    frames = wave.getSamples(waves)
    # frames = stdMovArg(frames)
    frames = flt.clean(frames)
    frames = stdMovArg(frames)
    frames = flt.halfRate(frames)
    frames = flt.norm(frames)
    frames = flt.movingAverage(frames, 16)
    frames = flt.movingAverage(frames, 8)
    # frames = flt.lowPass(frames, 0.5)

    # chart.drawGraphJob(frames)
    frames = flt.avgStep(frames, 100, 50)
    # chart.drawGraphJob(frames)
    frames = flt.shannon(frames)
    chart.drawGraphJob(frames)
    # result = pul.findBeats(frames, 50)
    # for i in range(result[0].size):
    #     print(result[0][i])
