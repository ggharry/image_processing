#!/usr/local/bin/python

import numpy as np
from numpy import *
import cv2
from sys import argv

def cement(image0, image1):
	#height = len(image0)
	#width = len(image0[0])
	#assert image0 is not None and image1 is not None
	#assert len(image1) == height and len(image1[0]) == width
	#image = []
	
	image0 = array(image0,np.float) ** 2
	image1 = array(image1,np.float) ** 2
	image = sqrt(image0 + image1)

	

#	for i in range(0,height):
#		new_i = []
#		for j in range(0,width):
#			new_j = np.array(image0[i][j],np.float)**2 + np.array(image1[i][j],np.float)**2
#			new_j = np.sqrt(new_j)
#			for bit in range(0,len(new_j)):
#				if new_j[bit] > 255.0:
#					new_j[bit] == 255.0
#			new_i.append(new_j)
#		image.append(new_i)
	
#	image = np.array(image, dtype=np.uint8)
	return array(image,dtype=np.uint8)
if __name__ == '__main__':
	i = cement(cv2.imread(argv[1]),cv2.imread(argv[2]))

	cv2.imwrite(argv[3], i)
