import TreeBin as T

# Implement a function to check if a tree is balanced.  For the purposes of this question, a balanced tree is defined to be a tree such that no two leaf nodes differ in distance from the root by more than one.

# creates a tree with the number of nodes is the value of size where ever node is the left chile of the previous node
def createUnbalancedTree(size):
	nodeList = [ T.Node(x) for x in range(size) ]
	nodeList[0].right = T.Node(size)
	for x in range(size-1):
		nodeList[x].left = nodeList[x+1]
	return nodeList[0]

# TODO: create a more random unbalanced tree.  Maybe randomly add a node on the right, left or both
def createUnbalancedTree2(size):
	pass

# creates a balanced tree with the number of nodes is the value of size
# this tree is not in order.
# there is a better way to do this in createMinHeightBinaryTree.py
def createBalancedTree(size):
	nodeList = []
	offset = 1
	# I need the array index to start at one for the math to work out so I'm actually creating a list that is size+1
	nodeList = [ T.Node(x-1) for x in range(size+offset) ]
	for x in range(offset, size+offset):
		if nodeList[x].left == None and x * 2 <= size:
			nodeList[x].left = nodeList[x*2]
		if nodeList[x].right == None and (x * 2 + 1) <= size:
			nodeList[x].right = nodeList[x * 2 + 1]
	# return the head of the balanced tree
	return nodeList[1]

def isBalanced(head):
	nodes = []
	nodes.append(head)
	numNodes = 1
	numNextNodes = 0
	level = 0
	leafLevels = set()
	while numNodes > 0 and len(leafLevels) < 3:
		if nodes[0].left != None:
			nodes.append(nodes[0].left)
			numNextNodes += 1
		if nodes[0].right != None:
			nodes.append(nodes[0].right)
			numNextNodes += 1
		if nodes[0].left == nodes[0].right == None:
			leafLevels.add(level)
		nodes.pop(0)
		numNodes -= 1
		if numNodes == 0:
			numNodes, numNextNodes = numNextNodes, numNodes
			level += 1
	return max(leafLevels) - min(leafLevels) < 3

balancedTree = createBalancedTree(63)
T.displayTree(balancedTree)
unbalancedTree = createUnbalancedTree(6)
T.displayTree(unbalancedTree)

print(isBalanced(balancedTree))
print(isBalanced(unbalancedTree))