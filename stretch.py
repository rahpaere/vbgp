#! /usr/bin/python

from fileinput import input
from vbgp import stretch, mapnodes, tryint

for line in input():
	timestamp, rest = line.split(",", 1)
	nexthops = [tryint(x) for x in rest.split(",")]
	stretches = mapnodes(stretch, nexthops)
	print "{},{}".format(timestamp, ",".join(map(str, stretches)))
