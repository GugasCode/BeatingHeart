import numpy as np
from scipy.fftpack import hilbert

def distinguish(data):
    """
        Function that will return True if the file starts with S2 and False if
        the data starts with S1.
    """
    return data[0][1] - data[0][0] > data[0][2] - data[0][1]

def clean(data):
    """
        Simple clean function that just devides all values by the averague of
        thenselfs
    """
    avg = np.mean(np.absolute(data[1]))
    data[1] = data[1]/avg
    return data

def lowPass(data, const):
    result = np.array([data[1][0]])
    for i in range(1,data[1].size-1):
        aux = const * data[1][i] \
            + ( ((1-const)/2) * result[i-1]  )\
            + ( ((1-const)/2) * data[1][i+1] )
        result = np.append(result, [aux])
    result = np.append(result, [data[1][-1]])
    data[1] = result
    return data

def convertFR(frames, fr=2000):
    """
        Function that will convert the frame rate of a given file to a smaller
        one.
    """
    total_frames = len(frames)
    ratio = total_frames % fr
    new_frames = []
    count = 0
    for i in frames[::ratio]:
        # we'll select the maximum value for the ratio interval
        new_frames.append(max(frames[count*ratio:count*ratio+ratio]))
        # we'll also need to register the frame that was select
    return new_frames

def movingAverage(data, step):
    """ Filters the data noise using Moving Averague algorithm """
    step = int(step)
    size = len(data[1]) - step
    for i in range(size):
        aux = 0
        for l in range(step):
            aux += data[1][i+l]
        data[1][i] = aux / step
    return data

def mvgAverageOpt(data, step=10):
    """
        Optimized moving average function for numpy arrays.
    """
    window = np.ones((step)/float(step))
    return np.convolve(data, window, 'same')

def norm(data):
    data = data.astype(np.float32)
    data[1] = data[1]/(np.absolute(data[1])).max()
    return data

def halfRate(data):
    if len(data[1]) % 2 != 0:
        aux = np.delete(data[1], -1)
        result = aux.reshape(-1, 2).mean(axis=1)
    else:
        result = data[1].reshape(-1, 2).mean(axis=1)
    return np.append([np.array(range(len(result)))], [result], axis=0)

def shannon(data):
    n = data[1] ** 2
    return np.append([data[0]], [-n*np.log((n+0.00000001))], axis=0)

def avgShannon(data, width, step):
    size = data[0].size - width
    for i in range(0, size, step):
        aux = 0.0
        for j in range(width):
            aux += data[1][i+j]
        aux /= width
        for j in range(width):
            data[1][i+j] = aux
    return  data

#TODO:make this work
def hilbertEnv(data, step):
    res = np.array([])
    size = data[1].size - step - 1
    print(data[1].size)
    print(size)
    i = 0
    while i < size:
        aux = hilbert(data[1][i:i+step])
        print(data[0][i])
        print(aux)
        res = np.append(res, aux)
        i += 100
    return np.append([range(len(res))], [res], axis=0)

if __name__ == "__main__":
    """ Unit tests """
    import sys
    import utils.waves as wave
    import utils.charts as chart

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
