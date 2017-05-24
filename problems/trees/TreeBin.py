class Node(object):
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

# creates a tree with the number of nodes is the value of size where ever node is the left chile of the previous node
def createUnbalancedTree(size):
	nodeList = [ Node(x) for x in range(size) ]
	for x in range(size-1):
		nodeList[x].left = nodeList[x+1]
	return nodeList[0]

# TODO: create a more random unbalanced tree.  Maybe randomly add a node on the right, left or both

# creates a balanced tree with the number of nodes is the value of size
def createBalancedTree(size):
	nodeList = []
	offset = 1
	# I need the array index to start at one for the math to work out so I'm actually creating a list that is size+1
	nodeList = [ Node(x-1) for x in range(size+offset) ]
	for x in range(offset, size+offset):
		if nodeList[x].left == None and x * 2 <= size:
			nodeList[x].left = nodeList[x*2]
		if nodeList[x].right == None and (x * 2 + 1) <= size:
			nodeList[x].right = nodeList[x * 2 + 1]
	# return the head of the balanced tree
	return nodeList[1]


def _printTree(head, order):
	if head != None:
		if order == 0:
			print(head.value, end=" ")
			_printTree(head.left, 0)
			_printTree(head.right, 0)
		if order == 1:
			_printTree(head.left, 1)
			print(head.value, end=" ")
			_printTree(head.right, 1)
		if order == 2:
			_printTree(head.left, 2)
			_printTree(head.right, 2)
			print(head.value, end=" ")

# print tree is a specific order.
# 0 - pre order
# 1 - in order
# 2 - post order
def printTree(head, order=0):
	_printTree(head, order)
	print()



# figure out the height of the tree and the length of the longest node.value
# return an array [<height>, <length of node.value>]
# has to be a sub function since recursion is used to get this information
def _getHeightandMaxLen(node):
	if node == None:
		return [0,0]
	lReturn = _getHeightandMaxLen(node.left)
	rReturn = _getHeightandMaxLen(node.right)
	maxLen = max(lReturn[1], rReturn[1], len(str(node.value)))
	# print(str(node.value).center(4," "))
	return [1 + max(lReturn[0], rReturn[0]), maxLen]


def _printValue(value, length):
	print(str(value).center(length," "), end="")

#           0
#     1           2
#   3   4      5     6
# 7   8   9  10 11 12 13 14

# print out the tree in tree form
def displayTree(head):
	treeStats = _getHeightandMaxLen(head)
	# output by units of length
	# the longest output would be the lowest level = 2^<height> * 2 - 1
	# make an array of this size for each level and figure out where each value goes.
	# print out spaces of length: print("".center(length," "), end="")
	# values in width of length: print(str(node.value).center(length," "), end="")
	outputLen = 2 ** treeStats[0] * 2 - 1
	for x in range(treeStats[0]):
		outputBuffer = [None for x in range(outputLen)]
		if x == 0:
			outputBuffer[outputLen // 2] = str(head.value).center(2, " ")
		print(outputBuffer)


	print(outputLen//2)
	return treeStats
