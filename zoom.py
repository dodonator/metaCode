import numpy as np 
import random as r 
from scipy import misc
import matplotlib.pyplot as plt
import math
import os

curDir = os.getcwd()

filename = curDir + '/test.png'
inputImage = misc.imread(filename)

faktor = int(raw_input('Zoomfaktor: '))

image = []
for row in inputImage:
	tmp = []
	for pixel in row:
		for i in xrange(faktor):
			tmp.append(pixel)
	for i in xrange(faktor):		
		image.append(tmp)

image = misc.toimage(image)
filename = curDir + '/testZ.png'
misc.imsave(filename,image)
	
