"""
Classifiers module that will have all of the classifiers being used in this
project, for now there is the kNN and the Naive Bayes classifiers.
"""
# Using Python 3
import numpy as np

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

	def conditionals(self, test, classification, param):
		"""
			Method to calculate the conditional probability for a specific
			parameter.
		"""
		sum(self.data[classification])


class KNN():
	def __init__(self, data):
		self.data = data

	def distance(self, test):
		size = len(test)-2
		dsitances = []
		for item in self.data:
			dist = 0
			for element in range(1, size):
				dist += (item[element] - test[element])**2
			distances.append(item[0], dist)
		return distances
