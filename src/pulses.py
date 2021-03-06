import numpy as np

def findBeats(data, ignore, factor):
    """
        Finds Beats in data where ignore is the percentage to ignore between
        two beats, and the factor is division for the cut off
    """
    amp = np.array([])
    frames = np.array([])
    cut = data[1].max() / factor
    ignore = data[1].size * (ignore/100)
    while ignore > 500:
        ignore /=2
    skip = 0
    for i in range(1,data[1].size-1):
        if i < skip:
            continue
        skip = 0
        if data[1][i] > cut:
            if data[1][i] >= data[1][i+1] and data[1][i] > data[1][i-1]:
                frames = np.append(frames, [data[0][i]])
                amp = np.append(amp, [data[1][i]])
                skip = i + ignore
    return np.append([frames], [amp], axis=0)

def findPoints(data, cut):
    pass

def getT11(data, startS1):
    start = 0
    if startS1 == True:
        start = 1
    res = np.array([])
    for i in range(start, len(data)-3, 2):
        aux = data[i+2] - data[i]
        res = np.append(res, [aux])
    return res

def getT12(data, startS1):
    start = 0
    if startS1 == True:
        start = 1
    res = np.array([])
    for i in range(start, len(data)-2, 2):
        aux = data[i+1] - data[i]
        res = np.append(res, [aux])
    return res

def getT(data, beats, startS1, cut):
    cut = beats[1].max() / 4
    t1 = []
    t2 = []
    pos = 1
    for jump in beats[0]:
        start = jump
        while data[1][start] > cut:
            start -= 1
        end = jump
        if end != len(data[1]) - 1:
            while data[1][end] > cut:
                if end != len(data[1]) - 1:
                    end += 1
                else:
                    break
        if startS1 == True and pos % 2 != 0:
            t2.append(end - start)
        elif startS1 == True and pos % 2 == 0:
            t1.append(end - start)
        elif startS1 == False and pos % 2 != 0:
            t1.append(end - start)
        elif startS1 == False and pos % 2 == 0:
            t2.append(end - start)
        pos += 1
    return t1, t2
