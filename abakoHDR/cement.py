#!/usr/local/bin/python

import numpy as np
import cv2
from sys import argv

def cement_squares(image0, image1):
	image0 = np.array(image0,np.float) ** 2
	image1 = np.array(image1,np.float) ** 2
	image = np.sqrt((image0 + image1))
	image = np.clip(image,0,255)
	
	return np.array(image,dtype=np.uint8)

def cement_maxes(image0, image1):
	return cv2.max(image0, image1)

if __name__ == '__main__':
	i = cement_maxes(cv2.imread(argv[1]),cv2.imread(argv[2]))
	cv2.imwrite(argv[3], i)
