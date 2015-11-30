"""
Sound processing module for the detection of the heart beats and also for the
implementation of noise reduction algorithms.
"""

import numpy as np

def fourier(data):
    return np.fft(data)

def averageReduction(data):
    """
    Function that will perform the average method for nosie reduction. First it
    calculates the average value of the data and then cuts everything that is
    within that interval in order to reduce the amount of noise to heartbeat
    ratio.
    """
    mean = np.average(data)
    return data
