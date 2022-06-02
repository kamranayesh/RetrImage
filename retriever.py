import numpy as np
import csv
class Retriever:
	def __init__(self, indexPath):
		# store our index path
		self.indexPath = indexPath
	def retrieve(self, queryFeatures, limit = 5):
		# initialize our dictionary of results
		results = {}
		# open the index file for reading
		with open(self.indexPath) as f:
			# initialize the CSV reader
			reader = csv.reader(f)
			# loop over the rows in the index
			for row in reader:
				features = [float(x) for x in row[1:]]
				d = self.squared_distance(features, queryFeatures)
				# now that we have the distance between the two feature
				# vectors, we can udpate the results dictionary -- the
				# key is the current image ID in the index and the
				# value is the distance we just computed, representing
				# how 'similar' the image in the index is to our query
				results[row[0]] = d
			# close the reader
			f.close()
		# we sort our results, so that the smaller distances (i.e. the
		# more relevant images are at the front of the list)
		results = sorted([(v, k) for (k, v) in results.items()])
		# return our (limited) results
		return results[:limit]
	def squared_distance(self, histA, histB, eps = 1e-10):
		# we compute the chi-squared distance which better than sse in case of histogram
		d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps)
			for (a, b) in zip(histA, histB)])
		# return the squared distance
		return d