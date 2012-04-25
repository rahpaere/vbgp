#! /usr/bin/python

from fileinput import input

def distance(node, nexthops, path=None):
	if path is None:
		path = list()
	if node is None:
		return float('nan')
	elif node in path:
		return float('inf')
	elif node == len(nexthops):
		if path[-1] == 1:
			return float(len(nexthops))
		else:
			return 0.0
	path.append(node)
	return 1.0 + distance(nexthops[node], nexthops, path)

def stretch(node, nexthops):
	if node == 0:
		return distance(node, nexthops) / 1.0
	else:
		return distance(node, nexthops) / 2.0

def tryint(x):
	try:
		return int(x)
	except ValueError:
		return None

for line in input():
	timestamp, rest = line.split(",", 1)
	nexthops = [tryint(x) for x in rest.split(",")]
	stretches = [str(stretch(node, nexthops)) for node in range(len(nexthops))]
	print "{},{}".format(timestamp, ",".join(stretches))
