#! /usr/bin/python

from fileinput import input

prev = None
for line in input():
	t, values = line.split(',', 1)
	if prev is None:
		print "0,{}".format(values.strip())
	else:
		print "{:06f},{}".format(float(t) - float(prev), values.strip())
	prev = t
