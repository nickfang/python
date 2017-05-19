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

	# makes class work with the print() function
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

# create a function that will return the node that contains the value that is passed in.
# return the path of nodes it took to get to that node
def findNodeWithPath(node, k):
	# if node == None:
	# 	return []
	retValue = []
	if node.value == k:
		return [node]
	else:
		# if there's no children, this shouldn't run
		for itr in node.children:
			retValue = findNodeWithPath(itr, k)
			if len(retValue) > 0:
				return [node] + retValue
		return retValue

# run functions
for i in range(8)[1:]:
	if findNode(a, i).value == i:
		print("Node with value {:d} found".format(i))
	else:
		print("NODE NOT FOUND!!")

for i in range(8)[1:]:
	print(i, ": ", end="")
	for itr in findNodeWithPath(a, i):
		print(itr.value, end=" ")
		# if itr != None:
		# 	print(itr, end=" ")
	print()
