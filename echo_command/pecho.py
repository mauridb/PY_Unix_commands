import os
import sys

PARAMS = sys.argv
PARAMS.pop(0) # remove python script in position 0


# check if params is string need to stay between between quotation marks
if len(PARAMS) > 1:
	print(" ".join(PARAMS))
else:
	print(PARAMS[0])
