#! /usr/bin/python

from fileinput import input

def reachable(nexthops):
	nexthops = list(nexthops)
	nodes = len(nexthops)
	for i in range(nodes):
		for node, nexthop in enumerate(nexthops):
			if nexthop is not None and nexthop != nodes:
				nexthops[node] = nexthops[nexthop]
	return len([n for n in nexthops if n == nodes])

def tryint(x):
	try:
		return int(x)
	except ValueError:
		return None

for line in input():
	entries = [tryint(x) for x in line.split(',')]
	print "{0},{1}".format(entries[0], reachable(entries[1:]))
