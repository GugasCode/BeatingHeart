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
    # it only send the first one there
    aux = np.array(['',[],''])
    for item in data:
        for a,b,c in item:
            aux[0] = a
            for i, j in zip(b):
                aux[1] = np.array([i,j])
            aux[2] = c
    return aux

class Bayes():
    """
        Class that will represent the Naive Bayes classifier.
    """
    def __init__(self, data):
        self.data = data
        self.data_size = len(data)
        pass

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
        self.data = data
        self.k = k
        print(data)

    def distance(self, test):
        """
            Method that will calculate the distance of the test subject to the
            data inside the self.data variable that represents the training.
        """
        size = len(test)-2
        distances = []
        for item in self.data: # we need the data to be pairs of T params
            dist = 0
            for element in item[1]:
                dist += (item[element] - test[element])**2
            distances.append((item[2], dist))
        return distances

    def decideClass(self, dists):
        """
            Method that will receive the k nearest neighbors and simply return
            the class which is more present in those distances.
        """
        maximum = {}
        for key, value in dists:
            if maximum[key] == None:
                maximum[key] = 1
            else:
                maximum[key] += 1

        return max(maximum.items(), key=operator.itemgetter(1))[0]

    def classify(self, test, k):
        distances = self.distance(test)
        distances.sort(key=operator.itemgetter(1))

        classification = decideClass(distances[:-k])
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

###myxor###
def deriv(x):
    return x * (1 - x)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def main():
    bits = np.array([
        [0,0],
        [0,1],
        [1,0],
        [1,1]
        ])
    output = np.array([
        [0],
        [1],
        [1],
        [0]
        ])
    np.random.seed(1)
    synapse0 = 2 * np.random.random((2,3)) - 1
    synapse1 = 2 * np.random.random((3,6)) - 1
    synapse2 = 2 * np.random.random((6,12)) - 1
    synapse3 = 2 * np.random.random((12,1)) - 1

    i = 0
    while True:
        layer0 = bits
        layer1 = sigmoid(np.dot(layer0, synapse0))
        layer2 = sigmoid(np.dot(layer1, synapse1))
        layer3 = sigmoid(np.dot(layer2, synapse2))
        layer4 = sigmoid(np.dot(layer3, synapse3))

        l4_error = output - layer4
        l4_delta = l4_error * deriv(layer4)

        if i % 10000 == 0:
            print("Error:" + str(np.mean(np.abs(l4_error))))
        if np.mean(np.abs(l4_error)) < 0.001:
            break

        l3_error = l4_delta.dot(synapse3.T)
        l3_delta = l3_error * deriv(layer3)

        l2_error = l3_delta.dot(synapse2.T)
        l2_delta = l2_error * deriv(layer2)

        l1_error = l2_delta.dot(synapse1.T)
        l1_delta = l1_error * deriv(layer1)

        synapse3 += layer3.T.dot(l4_delta)
        synapse2 += layer2.T.dot(l3_delta)
        synapse1 += layer1.T.dot(l2_delta)
        synapse0 += layer0.T.dot(l1_delta)

        i += 1
    print("output after training:")
    print(layer4)
###myxor###
