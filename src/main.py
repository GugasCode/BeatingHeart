import sys
import numpy as np
import pulses as pul
import filters as flt
import utils.waves as wave
import utils.files as files
import utils.charts as chart

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
    # frames = flt.shannon(frames)
    chart.drawGraphJob(frames)
    # result = pul.findBeats(frames, 50)
    # for i in range(result[0].size):
    #     print(result[0][i])
