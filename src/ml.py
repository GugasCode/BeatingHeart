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

def sorting(array, rule='asc'):
    """
        Auxiliary function that will sort all of the array ascending or descending
        and keeping track of the original results.
    """
    count = 0
    for i in array:
        pos = 0

def kNN(data, k, params=None):
    """
        Function that will perform the k-Nearest Neighbors algorithm for data,
        using all of the params. These params are the parameters that the user
        might want to test, default is all of them.
    """
    # these params is to make sure we are only using the parameters necessary to
    # the test, this way we could have a more selective approach if it needs to
    # come down to that.

    # make the param array if it wasn't given
    param_len = []
    if params == None:
        for el in data[0]:
            param_len.append(True)
        params = np.array(param_len)

    # only perform the algorithm to the fields that are True in the params array
    # n_params = params[params == True]
    n_params = params[params]
    dists = []
    for sub in data:
        dist = 0
        for el in sub:
            dist += el
        dists.append(dist/n_params)

    # now we have the list of distances and we only need to see which ones are
    # the k closest.
    position = 0
    sorting = []

def naiveBayes(data, target):
    gnb = GaussianNB()
    y_pred = gnb.fit(data, target).predict(data)

    return y_pred

def sort(data, rule='asc'):
    """
        Auxiliary function that will sort all of the results based on the second
        parameter, the distance in our case.
    """
    if rule == 'desc':
        return sorted(data, key=lambda tup: tup[1]).reverse()
    return sorted(data, key=lambda tup: tup[1])

def kNN(data, target, k, params=None):
    """
        Function for the kNN classification of a target element with the data
        from the training set. The k could be defined and it will resolve draws
        it will get the next element until the draw is resolved.
        The optional params argument will be in charge of the selection of
        characteristics to be used for the classification. It will be an array
        of booleans.
    """
    # Making all of the params to work with for the distance.
    select = []
    if params is None:
        # there are 4 params so you multiply by 4
        select = list(range(0, 4))
    else:
        for i in len(params):
            if params[i]:
                select.append(i)

    n_params = len(select)
    final = np.array([])
    count = 0
    for el in data:
        for i in select:
            total += (el[i] - target[i])**2

        final.append((count, total/n_params))
        count += 1

    # sort the results
    return sort(final)

def probs(data, target):
    """
        Function for conditional probability calculation.
    """
    count = 0
    for i in data:
        if data == target:
            count +=1

    return count

# def getWhere(data, index, target):
#     result = np.array()
#     for el in data:
#         if data[index] == target

def bayes(data, target):
    """
        Function that will perform the Naive Bayes algorithm.
    """
    probabilities = {
            'Normais': probs(data, 0),
            'Murmurios': probs(data, 1),
            'Sistolicos': probs(data, 2)
            }
