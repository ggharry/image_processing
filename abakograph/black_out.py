import Image
import matplotlib.pyplot as plt
import time
import numpy

# define constants
resolution = 1
brightness = 160
i = 0
j = 0
count = 0

# open an image file
f = Image.open('DSC_0085.jpg')
image = f.load()

# find file pixel width and length
x_max = f.size[0]
y_max = f.size[1]

# create a new image
f_new = Image.new('RGBA', (x_max, y_max))
new_image = f_new.load()

# loop through all the pixels
while i < x_max:
	while j < y_max:
		if image[i,j] > (brightness,brightness,brightness):
			new_image[i,j] = image[i,j]

		j += resolution
	i = i + resolution
	j = 0 

# show new modified image 
f_new.show()

