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
  -a, --all			Print any command installed on the system.
"""

def parseArguments():
	try:
		opts, args = getopt.getopt(sys.argv[1:], "hva", ["help", "version", "please", "all"])
	except getopt.GetoptError as err:
		print(err)
		sys.exit(1)

	global arguments
	arguments = {
		'random': False,
		'all': False,
	}

	for arg, val in opts:
		if arg in ("-h", "--help"):
			print(helpMsg)
			sys.exit()
		elif arg in ("-v", "--version"):
			print("tldrOfTheDay 0.1")
			sys.exit()
		elif arg == "--please":
			arguments['random'] = True
		elif arg in ("-a", '--all'):
			arguments['all'] = True

def readTldr():
	tldrList = list()
	for r, d, f in os.walk(os.path.join(os.getenv("HOME"), '.tldr/cache/pages/')):
		for file in f:
			tldrList.append(file.rstrip(file[-3:]))
	return tldrList
			
def readBin():		
	binList = list()
	for path in os.getenv("PATH").split(":"):
		for r, d, f in os.walk(path):
			for file in f:
				binList.append(file)
	return binList

def readHistory(binList):
	file = open(os.path.join(os.getenv("HOME"), '.zhistory'), "r", encoding='utf8', errors='ignore')
	
	historyList = list()
	
	while True:
		line = file.readline()
		if not line:
			break
		
		if not line.startswith(":"):
			continue
		
		if line.startswith("./", 15):
			continue

		if line.startswith("sudo", 15) or line.startswith("doas", 15):
			historyList.append((line[15:].split()[1]))
		else:
			historyList.append((line[15:].split()[0]))
		
	file.close()
	historyList = list(set(historyList) & set(binList))
	
	historyList.sort()
	
	return historyList

def getCommandOfTheDay(tldrList, commandList):
	undocumentedList = list(set(commandList) - set(tldrList))
	undocumentedList.sort()

	if not arguments['random']:
		random.seed(int(time.time() / (60*60*24)))

	print(len(undocumentedList))
	print(undocumentedList[random.randint(0, len(undocumentedList))])

def main():
	parseArguments()
	tldrList = readTldr()
	binList = readBin()
	historyList = readHistory(binList)
	if arguments['all']:
		getCommandOfTheDay(tldrList, binList)
	else:
		getCommandOfTheDay(tldrList, historyList)

if __name__ == "__main__":
	main()
