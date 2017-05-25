class Node(object):
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class Deque(object):
	def __init__(self):
		self.items = []

	def addFront(self, item):
		self.items.append(item)

	def removeBack(self):
		return self.items.pop(0)

# print tree is a specific order.
# 0 - pre order
# 1 - in order
# 2 - post order
def printTree(head, order=0):
	_printTree(head, order)
	print()

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


#               0
#        1              2
#   3       4       5       6
# 7   8   9  10  11  12  13  14

#                               1
#               1                               2
#       3               4               5               6
#   7       8       9      10      11      12      13      14
#15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30


# print out the tree in tree form
# if a node is None, a * is printed so it is easier to see the shape of the tree
# ever node is traversed twice so O(2n)
# while this was fun to do, it gets unwieldy if you have more than 6 levels
def displayTree(head):
	treeStats = _getHeightandMaxLen(head)
	if treeStats[0] > 6:
		print("displayTree() does not work well when a tree has a height greater than 6.  Displaying the first 6 levels of the tree")
		treeStats[0] = 6
	# print(treeStats)
	# output by units of length
	# the longest output would be the lowest level = 2^<height> * 2 - 1
	# make an array of this size for each level and figure out where each value goes.
	# print out spaces of length: print("".center(length," "), end="")
	# values in width of length: print(str(node.value).center(length," "), end="")
	outputLen = (2 ** (treeStats[0] - 1) * 2) * treeStats[1]
	# print(outputLen)
	tempNodeList = Deque()
	tempNodeList.addFront(head)
	for level in range(treeStats[0]):
		printWidth = outputLen // (2 ** level)
		# print(printWidth)
		for x in range(2 ** level):
			node = tempNodeList.removeBack()
			if node == None:
				# if the current node is None, print a * so the shape of the tree is easier to see
				print("*".center(printWidth, " "), end = "")
			else:
				print(str(node.value).center(printWidth, " "), end="")

			# fill the front of the deque with the next set of nodes to go through
			if level < treeStats[0] - 1:
				if (node == None):
					tempNodeList.addFront(None)
					tempNodeList.addFront(None)
					continue

				if (node.left == None):
					tempNodeList.addFront(None)
				else:
					tempNodeList.addFront(node.left)
				if (node.right == None):
					tempNodeList.addFront(None)
				else:
					tempNodeList.addFront(node.right)

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


