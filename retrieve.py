from colordescriptor import ColorDescriptor
from retriever import Retriever
import argparse
import cv2
from PIL import Image
import numpy as np
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required = True,
	help = "Path to where the computed index will be stored")
ap.add_argument("-q", "--query", required = True,
	help = "Path to the query image")
ap.add_argument("-r", "--result_path", required = True,
	help = "Path to the result path")
args = vars(ap.parse_args())
# initialize the image descriptor
cd = ColorDescriptor()
# load the query image and describe it
query = Image.open(args["query"])
features = cd.describe(query)
# perform the search
retriever = Retriever(args["index"])
results = retriever.retrieve(features)
# display the query
que = cv2.imread(args["query"])
cv2.imshow('Query',que)
# loop over the results
#resultimg=[]
for i,(score, resultID) in enumerate(results):
	# load the result image and display it
    result = cv2.imread(args["result_path"] + "\\" + resultID)
    #resultimg.append(result)
    winname="Result {}".format(i+1)
    cv2.imshow(winname, result)
    if i<3:
    	cv2.moveWindow(winname,i*385, 0)
    elif i<6:
    	cv2.moveWindow(winname, (i-3) * 385, 285)
    elif i<9:
    	cv2.moveWindow(winname, (i-6) * 385,0 )
    else :
    	cv2.moveWindow(winname, (i-9) * 385, 285)
    cv2.waitKey(0)