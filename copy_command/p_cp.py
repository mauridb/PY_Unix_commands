import os
import sys
import shutil


# TODO:
#   - allow rename copyed file
def p_cp(filename, dest_path):
	"""
	Copy command in python!
		filename: name file you wanna copy
		dest_path: destination path passed as param
	"""
	srcfile = os.path.abspath(filename)
	# print(srcfile)
	if filename in os.listdir() and os.path.isfile(filename):
		if os.path.isdir(dest_path) == False:
			os.makedirs(dest_path) # create all dirs if not exist
		shutil.copy(srcfile, dest_path) # copy filename from to
		print('Succesfully copyed!')
	else:
		print(filename + ' does not exist!')

try:
	INPUT_FILE = sys.argv[1]
	DESTINATION_PATH_FILE = sys.argv[2]
	p_cp(INPUT_FILE, DESTINATION_PATH_FILE)
except Exception as e:
	print(e)