#!/usr/local/bin/python

import numpy as np
import cv2
from sys import argv
import csv

def cement_squares(aba_image, hdr_image):
	aba_image = np.array(aba_image,np.float) ** 2
	hdr_image = np.array(hdr_image,np.float) ** 2
	hdr_aba = np.sqrt((aba_image + hdr_image))
	hdr_aba = np.clip(hdr_aba,0,255)
	
	return np.array(hdr_aba,dtype=np.uint8)

def cement_maxes(aba_image, hdr_image):
	return cv2.max(aba_image, hdr_image)

def hdr_cement(aba_image, hdr_image):
	# read existing response curve
	reader = csv.reader(open('canon_d60.csv', "rU"))
	mapping = []
	for row in reader:    
	    mapping.append(float(row[0]))

	# response function
	def f(q):
		return np.sqrt(q)
	# inverse of response function
	def f_inverse(fq):
		return mapping[fq]
	# vectorize inverse of response function to be used in numpy
	f_inv = np.vectorize(f_inverse)

	# aba_image =  (np.clip(np.clip(aba_image,60,250),0,255) - 60)*255

	new = cv2.max(aba_image, (hdr_image/2))

	return new


if __name__ == '__main__':
	i = hdr_cement(cv2.imread(argv[1]),cv2.imread(argv[2]))
	cv2.imwrite(argv[3], i)