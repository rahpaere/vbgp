#! /usr/bin/python

from math import isinf, isnan
from fileinput import input

for line in input():
	timestamp, rest = line.split(",", 1)
	stretches = [float(x) for x in rest.split(",")]
	connected = len([x for x in stretches if x == 1.0])
	print "{},{:d}".format(timestamp, connected)
