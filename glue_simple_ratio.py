import Image
# import matplotlib.pyplot as plt
# import time
# import numpy
# from scipy.optimize import curve_fit

# initializing variables
resolution = 1 # every pixel
i = 0
j = 0
k = 0
under_ratio = 40
over_ratio = 1

# load image with under exposure
f_under = Image.open('under_ex.JPG')
x_max = f_under.size[0]
y_max = f_under.size[1]
image_under = f_under.load()

# load image with over_exposure
f_over = Image.open('over_ex.JPG')
x_max = f_over.size[0]
y_max = f_over.size[1]
image_over = f_over.load()

# loop through to try different ratios
for under_ratio in range(40,200,20):
	# create a new image
	f_combine = Image.new('RGB', (x_max, y_max))
	image_combine = f_combine.load()

	while i < x_max:
		while j < y_max:

			temp_arr = [0.0,0.0,0.0]

			for k in range(3):
				temp_arr[k] = (under_ratio/10*float(image_under[i,j][k]) + float(over_ratio*image_over[i,j][k]))/(under_ratio/10+over_ratio)
				temp_arr[k] = int(temp_arr[k])
				k += 1
			image_combine[i,j] = tuple(temp_arr)
			k = 0
			temp_arr = []

			j += resolution
		i += resolution
		j = 0 

	# save and show new combined image 
	# f_combine.show()
	f_combine.save('trials/combine_ratio_'+str(under_ratio)+'_1.jpg')
	i = 0
	j = 0
	k = 0

