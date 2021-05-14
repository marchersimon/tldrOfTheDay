#!/usr/bin/env python

import os
import sys
import getopt
import random
import time

helpMsg = """Usage: tldrOfTheDay [options]

Options:
  -h, --help		Display this help.
  -v, --version		Display version information.
      --please		Print a new random command, independent of time and day.
"""

randomCommand = False

try:
	opts, args = getopt.getopt(sys.argv[1:], "hv", ["help", "version", "please"])
except getopt.GetoptError as err:
	print(err)
	sys.exit(1)

for arg, val in opts:
	if arg in ("-h", "--help"):
		print(helpMsg)
		sys.exit()
	elif arg in ("-v", "--version"):
		print("tldrOfTheDay 0.1")
		sys.exit()
	elif arg == "--please":
		randomCommand = True

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

if not randomCommand:
	random.seed(int(time.time() / (60*60*24)))
	
print(undocumentedList[random.randint(0, len(undocumentedList))])
