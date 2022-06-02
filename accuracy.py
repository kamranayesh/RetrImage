import numpy as np
import csv
import glob
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.cluster import KMeans
class KmeansCLustering:
	def __init__(self, indexPath):
		# store our index path
		self.indexPath = indexPath
	def clusters(self, dataset):
		images=[]
		for imagePath in glob.glob(dataset + "\\*.jpg"):
			imageID = imagePath[imagePath.rfind("\\") + 1:]
			images.append(imageID)
		data = {}
		with open(self.indexPath) as f:
			reader = csv.reader(f)
			for row in reader:
				features = [float(x) for x in row[1:]]
				data[row[0]] = features
			f.close()
		# get a list of the filenames
		filenames = np.array(list(data.keys()))

		# get a list of just the features
		feat = np.array(list(data.values()))
		kmeans = KMeans(n_clusters=10)
		kmeans.fit(feat)
		# holds the cluster id and the images { id: [images] }
		groups = {}
		for file, cluster in zip(filenames, kmeans.labels_):
			if cluster not in groups.keys():
				groups[cluster] = []
				groups[cluster].append(file)
			else:
				groups[cluster].append(file)
		return groups

		# function that lets you view a cluster (based on identifier)
	def view_cluster(self,cluster,groups,dataset):
			plt.figure(figsize=(25, 25));
			# gets the list of filenames for a cluster
			files = groups[cluster]
			# only allow up to 30 images to be shown at a time
			if len(files) > 30:
				print(f"Clipping cluster size from {len(files)} to 30")
				files = files[:29]
			# plot each image in the cluster
			for index, file in enumerate(files):
				plt.subplot(10, 10, index + 1);
				img = Image.open(dataset+ "\\" +file)
				img = np.array(img)
				plt.imshow(img)
				plt.axis('off')
			plt.show()

	def accuracy(self, query, groups, results):
		queryID = query[query.rfind("\\") + 1:]



def main():
    acc=KmeansCLustering("index.csv")
    groups=acc.clusters("dataset")
    print(groups[0][0])
    #acc.view_cluster(10,groups,"dataset")
    """sse = []
    list_k = list(range(3, 50))

    for k in list_k:
    	km = KMeans(n_clusters=k, random_state=22, n_jobs=-1)
    	km.fit(groups)

    	sse.append(km.inertia_)

	# Plot sse against k
    plt.figure(figsize=(6, 6))
    plt.plot(list_k, sse)
    plt.xlabel(r'Number of clusters *k*')
    plt.ylabel('Sum of squared distance')
    plt.show()"""
if __name__ == "__main__":
    main()