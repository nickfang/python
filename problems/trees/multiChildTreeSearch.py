class Node():
	def __init__(self, value):
		self.value = value
		self.children = []

	def _printNodes(self, node):
		print(", " + str(node.value), end="")
		if node.children != []:
			for itr in node.children:
				node._printNodes(itr)
			return

	def printTree(self):
		print(self.value, end="")
		for itr in self.children:
			self._printNodes(itr)
		print("")

	def __str__(self):
		return str(self.value)

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)
g = Node(4)
h = Node(7)

a.children.append(b)
a.children.append(c)
a.children.append(d)
c.children.append(e)
c.children.append(f)
d.children.append(h)
e.children.append(g)

a.printTree()

# create a function that will return the node that contains the value that is passed in.
# return the path of nodes it took to get to that node

def findNode(node, k):
	if node == None:
		return
	if node.value == k:
		return node
	else:
		for itr in node.children:
			retValue = findNode(itr, k)
			if retValue != None and retValue.value == k:
				return retValue

#TODO: finish this problem.  for some reason, 2 works, but 3 does not.
def findNodeWithPath(node, k):
	if node == None:
		return []
	if node.value == k:
		return [node]
	else:
		for itr in node.children:
			retValue = findNodeWithPath(itr, k)
			if retValue == []:
				return []
			elif retValue[0].value == k:
				return [retValue] + [node]
			else:
				return retvalue + [node]

for i in range(8)[1:]:
	print("Value of node found: ", findNode(a, i))
	for itr in findNodeWithPath(a, i):
		if itr != None:
			print(itr, end=" ")

	print("")