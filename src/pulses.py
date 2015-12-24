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
