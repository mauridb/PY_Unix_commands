import os
import sys


PATH_FILE = sys.argv[1]
PATTERN = sys.argv[2]
SUBSTITUTE = sys.argv[3]

def get_readlines(f):
	with open(f, 'r') as f:
		return f.readlines()
def psed(path_file, pattern, substitute):
	"""
	Params
	- path_file: is the file you wanna modify
	- pattern: is the slice of word that you wanna change
	- substitute: is the replacement portion of text
	"""
	readlines = get_readlines(path_file)
	replace_lines = []
	for index, elem in enumerate(readlines):
		if index < len(readlines)-1:
			# trace elem by index
			replace_lines.append(elem[:-1].replace(pattern, substitute)+'\n')
		elif index == len(readlines)-1 and '\n' not in elem:
			# check last line
			replace_lines.append(elem.replace(pattern, substitute))
		new_text = "".join(replace_lines)
	print(new_text)

psed(PATH_FILE, PATTERN, SUBSTITUTE)
