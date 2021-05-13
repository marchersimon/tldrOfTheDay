import os
import random
import time

tldrList = list()
for r, d, f in os.walk(os.path.join(os.getenv("HOME"), '.tldr/cache/pages/')):
	for file in f:
		tldrList.append(file.rstrip(file[-3:]))
		
binList = list()
for path in os.getenv("PATH").split(":"):
	for r, d, f in os.walk(path):
		for file in f:
			binList.append(file)
			
undocumentedList = list(set(binList) - set(tldrList))
undocumentedList.sort()

random.seed(int(time.time() / (60*60*24)))
print(undocumentedList[random.randint(0, len(undocumentedList))])

