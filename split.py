#! /usr/bin/python

from fileinput import input
from vbgp import converged, mapnodes, tryint
from os import rename

i = 0
out = None
start = None
for line in input():
	if out is None:
		out = open("/tmp/vnet-current-nexthops.log", "w")
	timestamp, rest = line.split(",", 1)
	timestamp = float(timestamp)
	if start is None:
		start = timestamp
	nexthops = [tryint(x) for x in rest.split(",")]
	out.write("{:06f},{}\n".format(timestamp - start, ",".join([n is not None and str(n) or "" for n in nexthops])))
	if converged(nexthops):
		out.close()
		out = None
		rename("/tmp/vnet-current-nexthops.log", "/tmp/vnet-run{:d}-nexthops.log".format(i))
		i += 1
		start = None
