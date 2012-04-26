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

def converged(nexthops):
	stretches = map(lambda x: stretch(x, nexthops), range(len(nexthops)))
	return stretches == [1.0] * len(nexthops)

def tryint(x):
	try:
		return int(x)
	except ValueError:
		return None

def mapnodes(f, nexthops):
	return map(lambda node: f(node, nexthops), range(len(nexthops)))
