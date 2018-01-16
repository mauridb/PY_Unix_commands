import os
import sys


list_dir = os.listdir()
visible = []
for elem in list_dir:
	# check if first char is '.' match hidden elem and if it's a file or dir
	if elem[0] != '.' and os.path.isfile(elem):
		visible.append((elem, "FILE"))
	elif elem[0] != '.' and os.path.isdir(elem):
		visible.append((elem, "DIR"))
	else:
		# print('i am an hidden elem %s' % str(elem))
		pass


def pls(items):
	for elem in items:
		print("\t".join(elem), end="\n")

pls(visible)
