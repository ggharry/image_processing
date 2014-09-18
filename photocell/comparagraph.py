import Image
import matplotlib.pyplot as plt
import time
import numpy
from scipy.optimize import curve_fit

resolution = 25

start = time.time()

f = Image.open('q/5.JPG')

# find file pixel size
x_max = f.size[0]
y_max = f.size[1]
i = 0
j = 0
count = 0

# load image
image = f.load()

q = []

while i < x_max:
	while j < y_max:
		q.append(image[i,j][1])
		j += resolution
	i = i + resolution
	j = 0 

f = Image.open('q/6.JPG')

# find file pixel size
x_max = f.size[0]
y_max = f.size[1]
i = 0
j = 0
count = 0

# load image
image = f.load()

q2_red = []
q2_blue = []
q2_green = []

while i < x_max:
	while j < y_max:
		q2_red.append(image[i,j][0])
		q2_blue.append(image[i,j][1])
		q2_green.append(image[i,j][2])

		j += resolution
	i = i + resolution
	j = 0 

def fit_func(x, a, b):
    return a*x**b

p_red = curve_fit(fit_func, q, q2_red)
p_blue = curve_fit(fit_func, q, q2_blue)
p_green = curve_fit(fit_func, q, q2_green)

p_red = p_red[0]
p_blue = p_blue[0]
p_green = p_green[0]

# p_red = numpy.polyfit(q,q2_red,3)
# p_blue = numpy.polyfit(q,q2_blue,3)
# p_green = numpy.polyfit(q,q2_green,3)

print p_red
print p_blue
print p_green
print "\n"

plt.scatter(q,q2_red,c="gray")
plt.scatter(q,q2_blue,c="gray")
plt.scatter(q,q2_green,c="gray")

x = numpy.linspace(0,220,1000) 
plt.plot(x,p_red[0]*x**p_red[1],'r-')
plt.plot(x,p_blue[0]*x**p_blue[1],'b-')
plt.plot(x,p_green[0]*x**p_green[1],'g-')

plt.xlim(xmin=0, xmax=255)
plt.ylim(ymin=0, ymax=255)
plt.xlabel("RGB pixels with exposure level q0")
plt.ylabel("RGB pixels with exposure level 2 x q0")

end = time.time()

print end - start
print "\n"

plt.show()


