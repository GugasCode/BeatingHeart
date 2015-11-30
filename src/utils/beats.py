"""
Sound processing module for the detection of the heart beats and also for the
implementation of noise reduction algorithms.
"""

import numpy as np

def fourier(data):
    return np.fft(data)
