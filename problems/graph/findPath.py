graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E']) }


def findPath(graph, start, end, path=[]):
	# NOTE: can't use append because then we would modify the path in the caller.  We need to create a new list.
	path = path + [start]
	# print(path)
	if start == end:
		return path
	if not start in graph.keys():
		return None
	for node in graph[start]:
		if node not in path:
			newpath = findPath(graph, node, end, path)
			if newpath:
				return newpath
	return None

def findAllPaths(graph, start, end, path=[]):
	path = path + [start]
	if start == end:
		return [path]
	if not start in graph.keys():
		return []
	paths = []
	for node in graph[start]:
		if node not in path:
			newpaths = findAllPaths(graph, node, end, path)
			for newpath in newpaths:
				paths.append(newpath)
	return paths

print(findPath(graph, "A", "E"))
print(findPath(graph, "A", "F"))

print(findAllPaths(graph, "B", "C"))
print(findAllPaths(graph, "A", "B"))

print(findAllPaths(graph, "Z", "A"))