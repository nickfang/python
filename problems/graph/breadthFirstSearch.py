graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E']) }

# breadth first traversal to see all the nodes that can be accessed by node start
def searchBF(graph, start):
	visited = dict()
	for index in graph.keys():
		visited[index] = False
	queue = [start]
	visited[start] = True
	while queue:
		node = queue.pop(0)
		for nextNode in graph[node]:
			if not visited[nextNode]:
				queue.append(nextNode)
				visited[nextNode] = True
	print(visited)

def searchBFPath(graph, start, end):
	queue = []
	queue.append([start])
	while queue:
		tempPath = queue.pop(0)
		lastNode = tempPath[-1]
		if lastNode == end:
			print("Valid Path: ", tempPath)
		for nextNode in graph[lastNode]:
			if nextNode not in tempPath:
				queue.append(tempPath + [nextNode])

searchBF(graph, 'A')
for node in sorted(graph.keys()):
	print("Searching from node 'A' to node '{0}'".format(node))
	searchBFPath(graph, 'A', node)
