import numpy as np
import csv
import glob
from colordescriptor import ColorDescriptor
from retriever import Retriever
from accuracy import KmeansCLustering
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.cluster import KMeans
class Accuracy:
	def __init__(self, indexPath):
		# store our index path
		self.indexPath = indexPath

	def in_list(self,c, classes):
		for i, sublist in enumerate(classes):
			if c in sublist:
				return i
		return -1
	def in_group(self,c,classes):
		for i in range(len(classes)):
			for j in range(len(classes[i])):
				if c==classes[i][j]:
					return i
		return -1
	def calc(self, dataset):
		images = []
		for imagePath in glob.glob(dataset + "\\*.jpg"):
			imageID = imagePath[imagePath.rfind("\\") + 1:]
			images.append(imageID)
		cluster =[]
		cluster1=[]
		cluster2= []
		cluster3 = []
		cluster4 = []
		cluster5 = []
		cluster6 = []
		cluster7 = []
		cluster8 = []
		cluster9 = []
		cluster10 = []
		for img in images:
			imageID = img[:img.rfind(".")]
			#print(imageID)
			if int(imageID)<101:
				cluster1.append(img)
			elif int(imageID)<200:
				cluster2.append(img)
			elif int(imageID)<300:
				cluster3.append(img)
			elif int(imageID) < 400:
				cluster4.append(img)
			elif int(imageID)<500:
				cluster5.append(img)
			elif int(imageID)<600:
				cluster6.append(img)
			elif int(imageID)<700:
				cluster7.append(img)
			elif int(imageID)<800:
				cluster8.append(img)
			elif int(imageID)<900:
				cluster9.append(img)
			else:
				cluster10.append(img)
		cluster.append(cluster1)
		cluster.append(cluster2)
		cluster.append(cluster3)
		cluster.append(cluster4)
		cluster.append(cluster5)
		cluster.append(cluster6)
		cluster.append(cluster7)
		cluster.append(cluster8)
		cluster.append(cluster9)
		cluster.append(cluster10)
		km=KmeansCLustering("index.csv")
		clus=km.clusters("dataset")
		output = open("accuracy2", "w")
		for img in images:
			clusno=self.in_group(img,clus)
			cd = ColorDescriptor()
			query = Image.open(dataset + "\\"+img)
			features = cd.describe(query)
			retriever = Retriever(self.indexPath)
			results = retriever.retrieve(features)
			c=0
			for result in results:
				if self.in_group(result[1],clus)==clusno:
					c=c+1
			print(c)
			output.write("%s,%s\n" % (img, c/10.0))
		output.close()
		return cluster


def main():
	acc=Accuracy("index.csv")
	print(acc.calc("dataset")[0][0])
if __name__ == "__main__":
    main()