#! /usr/bin/python

from math import isinf, isnan
from fileinput import input

for line in input():
	timestamp, rest = line.split(",", 1)
	stretches = [float(x) for x in rest.split(",")]
	connected = len([x for x in stretches if not isnan(x) and not isinf(x)])
	print "{},{:d}".format(timestamp, connected)
