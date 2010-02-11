#!/usr/bin/python

import os
import sys

try:
	os.system('konqueror man:' + sys.argv[1] )
except IndexError:
	print "args please!"

