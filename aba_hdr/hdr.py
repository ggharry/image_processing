#!/usr/local/bin/python

import numpy as np
import cv2
from sys import argv
import argparse
import matplotlib.pyplot as plt
import csv

k = float(argv[4]) # k = 2^(delta of ev)
image0 = np.array(cv2.imread(argv[1]),np.uint8)
image1 = np.array(cv2.imread(argv[2]),np.uint8)
image00 = np.array(cv2.imread(argv[1]),np.float)
image11 = np.array(cv2.imread(argv[2]),np.float)

# read existing response curve
reader = csv.reader(open('canon_d60.csv', "rU"))
mapping = []
for row in reader:    
    mapping.append(float(row[0]))

# certainty function
def certainty(image):
	return np.exp(-((6*image/255-3)**2))

# response function
def f(q):
	return np.log(q)

# inverse of response function
def f_inverse(fq):
	return mapping[fq]

# vectorize inverse of response function to be used in numpy
f_inv = np.vectorize(f_inverse)

# imagespace -> lightspace -> processing
out = (k*f_inv(image0)*certainty(image00)+f_inv(image1)*certainty(image11))/(certainty(image00)+certainty(image11))

# lightspace -> imagespace
out = f(out)

# normalization
out = (out-out.min())*(255)/(out.max()-out.min())

# display + save HDR image
cv2.imwrite(argv[3],out)
new_image = cv2.imread(argv[3])
cv2.imshow('',new_image)
cv2.waitKey()

## plotting
# x = np.linspace(0,255).astype('uint8')
# plt.plot(x,f_inv(x),'r-')
# plt.plot(x,f(x),'g-')
# plt.show() 