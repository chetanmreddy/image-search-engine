# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 11:48:53 2017

@author: chetan
"""

import argparse
import cv2
 

 
# load the image and convert it to grayscale
image = cv2.imread('input.jpeg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
# initialize the list of threshold methods
methods = [
	("THRESH_BINARY", cv2.THRESH_BINARY),
	("THRESH_BINARY_INV", cv2.THRESH_BINARY_INV),
	("THRESH_TRUNC", cv2.THRESH_TRUNC),
	("THRESH_TOZERO", cv2.THRESH_TOZERO),
	("THRESH_TOZERO_INV", cv2.THRESH_TOZERO_INV)]
 
# loop over the threshold methods
for (threshName, threshMethod) in methods:
	# threshold the image and show it
	(T, thresh) = cv2.threshold(gray,200, 255, threshMethod)
	cv2.imshow(threshName, thresh)
	cv2.waitKey(0)
