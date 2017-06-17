# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 20:15:34 2017

@author: chetan
"""

# import the necessary packages
from matplotlib import pyplot as plt
import numpy as np
import cv2
 

 
# load the image and show it
image = cv2.imread('input.jpeg')
cv2.imshow("image", image)


# convert the image to grayscale and create a histogram
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])