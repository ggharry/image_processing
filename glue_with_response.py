# include libraries
import Image
import math
import numpy
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import scipy

# define functions

# fit power function to comparagram
def fit_func(x, a, b):
    return a*x**b

# response function
def f(q,zeta):
	return math.exp(q**(-zeta))

# certainty function with gaussian distribution
def certainty(pixelvalue):
	return math.exp(-((6*float(pixelvalue)/255-3)**2))

# inverse of response function
def f_inv(fq,zeta):
	# log is e based
	return math.log1p(fq)**(1/(-zeta))

# initializing variables
resolution = 1 # every pixel
i = 0
j = 0
k = 0
q = []
q2_red = []
ev = 16

# load image with under exposure
f_under = Image.open('cave_dark.JPG')
x_max = f_under.size[0]
y_max = f_under.size[1]
image_under = f_under.load()

# load image with over_exposure
f_over = Image.open('cave_bright.JPG')
image_over = f_over.load()

# loop through two images to store all red-color pixels values into two different arrays
while i < x_max:
	while j < y_max:
		# use red color only
		q.append(image_under[i,j][0]+0.001)
		q2_red.append(image_over[i,j][0]+0.001)
		j += resolution
	i = i + resolution
	j = 0 

# reset variables
i = 0
j = 0

# generate comparagraph and find gamma of the power function 
p_red = curve_fit(fit_func, q, q2_red)[0]
gamma = p_red[1]
# find zeta for the response function. The shutter speed difference was a factor of 4, so k = 2
zeta = math.log(gamma) / math.log(ev)

# # create a new image for combining the two images
# f_combine = Image.new('RGB', (x_max, y_max))
# image_combine = f_combine.load()

# # loop through all pixels to generate a new HDR image
# while i < x_max:
# 	while j < y_max:
# 		# temp variable to store RGB values
# 		temp_arr = [0.0,0.0,0.0]

# 		for k in range(3):
# 			a = float(image_under[i,j][k])
# 			b = float(image_over[i,j][k])

# 			# convert to lightspace, weight using certainty function
# 			temp_arr[k] = (ev*f_inv(a,zeta)*certainty(a) + f_inv(b,zeta)*certainty(b))/(certainty(a)+certainty(b)+0.001)
# 			# temp_arr[k] = f(b,zeta)*certainty(b)

# 			# convert to imagespace
# 			temp_arr[k] = f(temp_arr[k],zeta)

# 			temp_arr[k] = int(temp_arr[k])

# 			k += 1

# 		# note: tuple is a special data structure used by python's library. It's similar to an array
# 		image_combine[i,j] = tuple(temp_arr)
# 		k = 0
# 		temp_arr = []

# 		j += 1
# 	i = i + 1
# 	j = 0 

# # reset variables
# i = 0
# j = 0

# # show new image
# f_combine.show()

# f_combine.save("asd2.JPG")

x = numpy.linspace(0,255,255) 
plt.scatter(q,q2_red,c="gray") # comparagram
# plt.plot(x,numpy.exp(x**(-zeta)),'b-') # response function
# plt.plot(x,numpy.log1p(x)**(1/(-zeta)),'g-') # inverse of response function 
# plt.plot(x,(-zeta*x**(-zeta-1))*(numpy.exp(x**(-zeta))),'r-') # derivative of respones function...but doesnt work
plt.plot(x,p_red[0]*x**gamma,'r-') #comparagraph
plt.ylabel("f_inv(q)")
plt.xlabel("q")
# plt.xlim(xmin=0, xmax=255)
# plt.ylim(ymin=0, ymax=255)

plt.show()
print gamma
print zeta