import os
import string

filename = os.getcwd() + '/text2.txt'
filename2 = os.getcwd() + '/text.txt'
trans = string.maketrans('fFkK','kKfF')

with open(filename,'r') as f1:
	with open(filename2,'w') as f2:
		for line in f1:
			f2.write(line.translate(trans))
