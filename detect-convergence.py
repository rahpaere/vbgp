#! /usr/bin/python

from fileinput import input

def converged(nexthops):
	nexthops = list(nexthops)
	nodes = len(nexthops)
	if nexthops[0] != nodes or nexthops[1:] != [0] * (nodes - 1):
		return 0
	else:
		return nodes

def tryint(x):
	try:
		return int(x)
	except ValueError:
		return None

prev = True
for line in input():
	entries = [tryint(x) for x in line.split(',')]
	cur = converged(entries[1:])
	if prev != cur:
		print "{0},{1}".format(entries[0], cur)
	prev = cur
