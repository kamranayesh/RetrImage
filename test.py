import matplotlib.pyplot as plt
from PIL import Image
import cv2
img=Image.open('./0.jpg')
img=cv2.imread(img)
cv2.imshow('Hellow',img)
cv2.waitKey()