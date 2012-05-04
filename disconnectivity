#! /usr/bin/python

from math import isinf, isnan
from fileinput import input

total = 0.0
prev = None
for line in input():
	timestamp, rest = line.split(",", 1)
	timestamp = float(timestamp)
	if prev is not None:
		total += (timestamp - prev) * disconnected
	stretches = [float(x) for x in rest.split(",")]
	disconnected = len([x for x in stretches if isnan(x) or isinf(x)])
	disconnected = float(disconnected) / float(len(stretches))
	prev = timestamp
print total
