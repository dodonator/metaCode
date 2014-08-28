import os
curDir = os.getcwd()
curDir = '/media/dodo/M3NT0R/Privat/Projekte/ticTacToe'
# curDir = '/media/dodo/M3NT0R/Privat/Projekte/RandomYouTubeLinkGenerator'

directory = os.listdir(curDir)
folder = []
for name in directory:
	if '.py' in name and '~' not in name:
		folder.append(name)


content = []
length = []
counter = 0
for filename in folder:
	filename = curDir + '/' + filename
	content.append([])
	f1 = open(filename,'r')
	c = f1.read()
	length.append(len(c))
	f1.close()
	for char in c:
		content[counter].append(ord(char))
	counter += 1


av = []
m = min(length)
l = len(length)
for i in range(m):
	tmp = 0
	for f in content:
		tmp += f[i]
	av.append(float(tmp)/float(l))

for i in range(len(av)):
	av[i] = int(round(av[i]))

text = ''
for i in range(len(av)):
	text += chr(av[i])
print text
