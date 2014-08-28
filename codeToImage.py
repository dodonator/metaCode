import numpy as np 
import random as r 
from scipy import misc
import matplotlib.pyplot as plt
import math
import os

def getColor(char):
	r = char
	g = char*char%256
	b = char*char*char%256
	return [r,g,b]

filename = os.getcwd() + '/codeToImage.py'
filename = '/media/dodo/M3NT0R/Privat/Projekte/ticTacToe/tic5.py'
f1 = open(filename,'r')
content = f1.read()
f1.close()

content = content.replace('\t','    ')
content = content.split('\n')
maximum = []
image = []
for element in content:
	maximum.append(len(element))
	image.append([])
maximum = max(maximum)

for i in range(len(content)):
	content[i] = content[i] + (maximum - len(content[i]))*' '

for i in range(len(content)):
	tmp = []
	for char in content[i]:
		tmp.append(getColor(ord(char)))
	image[i] = tmp

image = misc.toimage(image)
misc.imsave('test.png',image)
