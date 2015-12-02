import sys
<<<<<<< HEAD
import numpy as np
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
    result = wave.getSamples(waves)
    result = stdMovArg(result)
    result = flt.halfRate(result)
    result = flt.norm(result)

    chart.drawGraphJob(result)
