# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 11:43:58 2017

@author: chetan
"""

import cv2
import numpy as np

img=cv2.imread('input.jpeg')
cv2.imshow('img',img)
cv2.waitKey(0)