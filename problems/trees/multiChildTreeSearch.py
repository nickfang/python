import TreeMulti as Tree

a = Tree.Node(1)
b = Tree.Node(2)
c = Tree.Node(3)
d = Tree.Node(4)
e = Tree.Node(5)
f = Tree.Node(6)
g = Tree.Node(4)
h = Tree.Node(7)

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
