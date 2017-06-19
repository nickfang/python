graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E']) }

def searchDF(graph, start, end, path=[]):
	path = path + [start]
	if start == end:
		return path
	if start not in graph.keys():
		return []
	for node in graph[start]:
		if node not in path:
			newPath = searchDF(graph, node, end, path)
			if newPath:
				return newPath
	return None

print(searchDF(graph, 'A', 'F'))
