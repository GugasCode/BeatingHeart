"""
Classifiers module that will have all of the classifiers being used in this
project, for now there is the kNN and the Naive Bayes classifiers.
"""

# Using Python 3
import numpy as np
import math
import random
import operator
# from collections import Counter

# clearly we need a function that is going to make all of the data turn into
# arrays os T param arrays
def parseData(data):
    # it only sends the first one there
    aux = np.array(['',[],''])
    for item in data:
        for a,b,c in item:
            aux[0] = a
            for i, j in zip(b):
                aux[1] = np.array([i,j])
            aux[2] = c
    return aux

def confusionMatrix(data):
    """
        Function that will make the confusion matrix for the classification.
    """
    # Structure of the confusion matrix
              # |  normais | extra | murmurios|
    # -----------------------------------------
    # normais   |
    # ----------|------------------------------
    # extra     |
    # ----------|------------------------------
    # murmurios |
    # ----------|------------------------------
    contagem0 = {'normais': 0,
            'extraSistolicos': 0,
            'murmurios':0}
    contagem1 = {'normais': 0,
            'extraSistolicos': 0,
            'murmurios':0}
    contagem2= {'normais': 0,
            'extraSistolicos': 0,
            'murmurios':0}
    matrix = {'normais': contagem0, 'extraSistolicos': contagem1,
            'murmurios': contagem2}
    for item in data:
        a = item[0]
        b = item[1]
        # this will actually work but item[0] needs to be the expected
        # and subsequently the item[1] is the result after classification
        matrix[a][b] += 1

    return matrix # matrix with all of the information.

def printMatrix(matrix):
    """
        Function that will print all of the information inside the matrix.
    """
    pass

def formatting(data):
    """
        Function that will prepare the data for our classifiers to work with.
        Returning the final array as a numpy array of 3 possitions, the name of
        the file and also the params in a numpy array as well and finally the
        classification. This way we have more then just one sample per file.
    """
    final = []
    for item in data:
        name = item[0]
        label = item[2]
        # get the smallest length array of that position
        length = len(item[1][0][0])
        if len(item[1][0][0]) > len(item[1][1][0]):
            length = len(item[1][1][0])
        for n in range(length):
            x = int(item[1][0][0][n])
            y = int(item[1][1][0][n])
            z = int(item[1][2][0][n])
            w = int(item[1][3][0][n])
            params = np.array([x, y, z, w])
            aux = [name, params, label]
            final.append(aux)
    return final

class Bayes():
    """
        Class that will represent the Naive Bayes classifier.
    """
    def __init__(self, data):
        self.data = formatting(data)
        self.data_size = len(data)

    def seperate(self):
        """
            Method that will seperate the existing data into the different
            classes of the data.
        """
        seperated = {}
        for item in data:
            key = itme[3]
            if key in data.keys():
                seperated[key].append(item)
            else:
                seperated[key] = [item]

        # new data already seperated between classes
        self.data = seperated

    def probabilities(self):
        """
            Method that will calculate all of the porbabilities of being from
            each class.
        """
        self.class_probs = {}
        for key, value in self.data:
                self.class_probs[key] = len(values)

    def conditional(self, test, training_class, param):
        """
            Method to calculate the conditional probability for a specific
            parameter.
        """
        count = 0
        for element in self.data[training_class]:
            if element[param] == test[param]:
                count += 1
        count_x = 0
        for classes, values in self.data:
            for line in values:
                if line[param] == test[param]:
                    count_x += 1

        return (count/self.data[training_class])/(count_x/self.data_size)

    def bayes(self, test):
        """
            Method that will perform the entire algorithm from start to
            finish.
        """
        # seperate the data
        self.separated()

        # calculate the absolut probabilities (porbability of being of a class)
        self.probabilities()

        # get all of the probabilities to check which is highest
        results = {}
        for item in self.data.key():
            sums = 0
            for i in range(0,4):
                sums += math.log(self.conditional(test, item, i))
            results[item] = sums

        #finding the best fit after all of the calculations
        pivot = (0,0)
        for key, value in results.items():
            if value > pivot[1]:
                pivot = (key, value)

        #send the results
        return pivot[0]

class KNN():
    def __init__(self, data, k):
        """
            Initialization method for the kNN algorithm
        """
        self.data = formatting(data)
        self.k = k

    def distance(self, test):
        """
            Method that will calculate the distance of the test subject to the
            data inside the self.data variable that represents the training.
        """
        size = len(test)-2
        distances = []
        for item in self.data: # we need the data to be pairs of T params
            dist = 0
            for element in range(len(item[1])):
                dist += (item[1][element] - test[1][element])**2
            dist = math.sqrt(dist)
            distances.append((item[2], dist))
        return distances

    def decideClass(self, dists):
        """
            Method that will receive the k nearest neighbors and simply return
            the class which is more present in those distances.
        """
        count = {'normais': 0,
                'extraSistolicos': 0,
                'murmurios':0}

        for item in dists:
            count[item[0]] += 1
        aux = -1
        result = 'placeholder'
        for key, value in count.items():
            if value > aux:
                result = key
                aux = value
        return result

    def classify(self, test, k):
        distances = self.distance(test)
        distances.sort(key=operator.itemgetter(1))
        print("k: ",distances[-k:])
        classification = self.decideClass(distances[-k:])
        return classification

class NeuralNet():
    """
        Class that will represent the Neural Network implementation for our
        project.
    """
    def __init__(self, data, params):
        """
            Initialization of the weights of the parameters
        """
        self.data = data
        for item in params:
            self.params[item] = random.random()

    def sigmoid(self, x, deriv=False):
        """
            Method that emulates the sigmoid function.
        """
        if deriv:
            return x*(1-x)
        return 1 / (1+np.exp(-x))

    def iteration(self, data):
        """
            Method that simulates one iteration of the Neural Network.
        """
        l0 = data
        l1 = self.sigmoid(np.dot(l0))

        l1_error = np.array(range(100))

        l1_delta = l1_error * sigmoid(l1, True)
