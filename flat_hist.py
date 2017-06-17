# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 11:41:18 2017

@author: chetan
"""
from matplotlib import pyplot as plt
import numpy as np
import cv2

# grab the image channels, initialize the tuple of colors,
# the figure and the flattened feature vector

image = cv2.imread('input.jpeg')
cv2.imshow("image", image)
chans = cv2.split(image)
colors = ("b", "g", "r")
plt.figure()
plt.title("'Flattened' Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
features = []
 
# loop over the image channels
for (chan, color) in zip(chans, colors):
	# create a histogram for the current channel and
	# concatenate the resulting histograms for each
	# channel
	hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
	features.extend(hist)
 
	# plot the histogram
	plt.plot(hist, color = color)
	plt.xlim([0, 256])
 
# here we are simply showing the dimensionality of the
# flattened color histogram 256 bins for each channel
# x 3 channels = 768 total values -- in practice, we would
# normally not use 256 bins for each channel, a choice
# between 32-96 bins are normally used, but this tends
# to be application dependent
print ("flattened feature vector size: %d" % (np.array(features).flatten().shape))