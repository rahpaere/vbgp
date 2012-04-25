#! /usr/bin/python

from fileinput import input

updates = []
for line in input():
	entries = [x.strip() for x in line.split(',')]
	updates.append(entries)

if updates:
	prev = int(updates[0][0])
	for t, c in updates:
		if c != "0":
			print "{0},{1}".format(int(t) - prev, c)
		prev = int(t)
else:
	print "0,0"
