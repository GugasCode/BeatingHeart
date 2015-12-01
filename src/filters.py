import numpy as np
from sklearn.preprocessing import normalize

def movingAverage(data, step):
    """ Filters the data noise using Moving Averague algorithm """
    step = int(step)
    size = len(data[0]) - step
    for i in range(size):
        aux = 0
        for l in range(step):
            aux += data[0][i+l]
        data[0][i] = aux / step
    return data

def norm(data):
    data = data.astype(np.float32)
    data[0] = data[0]/(np.absolute(data[0])).max()
    return data

def halfRate(data):
    aux = np.delete(data[0], -1)
    result = aux.reshape(-1, 2).mean(axis=1)
    return np.append([result], [np.array(range(len(result)))], axis=0)

import sys
import utils.waves as wave
import utils.charts as chart
if __name__ == "__main__":
    """ Unit tests """
    waves = wave.loadWave(sys.argv[2])
    result = wave.getSamples(waves)
    print(result)
    # chart.drawGraph(result)
    result = movingAverage(result, sys.argv[1])
    print(result)
    # chart.drawGraph(result)

    result = movingAverage(result, 8)
    result = movingAverage(result, 6)

    result = movingAverage(np.fliplr(result), 4)
    result = movingAverage(result, 8)
    result = movingAverage(result, 6)
    result = np.fliplr(result)

    # print(result)
    # chart.drawGraph(result)
    # result = norm(result)
    # print(result)
    # chart.drawGraph(result)

    result = halfRate(result)
    chart.drawGraph(result)
