"""
Machine Learning Module where there will be the algorithms for the analysis of
the data.
Mostly if not all of the components present here will be implemented with numpy
and scipy libs in order to keep feasable results in terms of time and resources.
"""

import numpy as np
import scipy as sp
from sklearn.neighbors import NearestNeighbors
from sklearn.naive_bayes import GaussianNB

def kNN(data, k):
    """
    Implementation of the kNN algorithms for classification. This function
    accepts the array of data, the k and returns a list with of the k nearest
    neighbors.
    """
    nbrs = NearestNeighbors(n_neighbors=k, algorithm='ball_tree').fit(data)
    distances, indices = nbrs.kneighbors(data)
    return (distances, indices)

def naiveBayes(data, target):
    gnb = GaussianNB()
    # incomplete mus check later
    y_pred = gnb.fit(data, target).predict(data)

    return y_pred
