#! /usr/bin/python

from datetime import datetime
from sys import stdin, argv
import re

timestamp_format = "Timestamp: %a %b %d %H:%M:%S %Y %f us "
microseconds_format = re.compile("(\d+) us")
update_format = re.compile("(Deleted )?192\.168\.0\.0/16.*via 10.0.0.(\d+)")

def reachable(nexthops):
	nexthops = list(nexthops)
	nodes = len(nexthops)
	for i in range(nodes):
		for node, nexthop in enumerate(nexthops):
			if nexthop is not None and nexthop != nodes:
				nexthops[node] = nexthops[nexthop]
	return len([n for n in nexthops if n == nodes])

updates = []
nodes = 0
for filename in argv[1:]:
	t = None
	with open(filename) as log:
		for line in log:
			try:
				t = datetime.strptime(line, timestamp_format)
				m = microseconds_format.search(line)
				if m is None:
					print "Bad microseconds."
					continue
				t = t.replace(microsecond=int(m.group(1)))
				continue
			except ValueError:
				pass

			m = update_format.match(line)
			if m is None:
				continue

			if m.group(1) is not None:
				nexthop = None
			else:
				nexthop = int(m.group(2)) - 1

			updates.append((t, nodes, nexthop))
	nodes += 1

updates.sort()
start = updates[0][0]

nexthops = [None] * nodes
print ",".join(["Elapsed microseconds", "Connected nodes"] + ["Nexthop {0}".format(n) for n in range(nodes)])
for t, node, nexthop in updates:
	nexthops[node] = nexthop
	r = t - start
	print ",".join([str(int(r.seconds * 1e6 + r.microseconds)), str(reachable(nexthops))] +  [n is not None and str(n) or " " for n in nexthops])
	#print ",".join([str(r.total_seconds()), str(reachable(nexthops))] +  [n is not None and str(n) or " " for n in nexthops])

