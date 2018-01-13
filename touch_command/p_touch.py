import os
import sys


PARAMS = sys.argv
PARAMS.pop(0) # remove script from param

def p_touch(files):
	for elem in files:
		open(str(elem), 'x') # x only for create

p_touch(PARAMS)
