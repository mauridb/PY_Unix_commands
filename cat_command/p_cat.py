import os
import sys


PARAMS = sys.argv
PARAMS.pop(0) # remove script from list param

param_file = PARAMS[-1] # take the last

# check if is file and if exists
if os.path.isfile(param_file):
	with open(param_file, 'r') as read_file:
		for line in read_file:
			print(line, end='')