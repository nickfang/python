# Implement a function to check if a tree is balanced.  For the purposes of this question, a balanced tree is defined to be a tree such that no two leaf nodes differ in distance from the root by more than one.

class Node(object):
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None


def createUnbalancedTree1(size):

	if size:
		temp = Node(size)
		size -= 1
		temp.left = createTree1(size)
		return temp
	return None

def createUnbalancedTree2(size):


def createBalancedTree(size):
	nodeList = []
	offset = 1
	# I need the array index to start at one for the math to work out so I'm actually creating a list that is size+1
	nodeList = [ Node(x) for x in range(size+offset) ]
	for x in range(offset, size+offset):
		if nodeList[x].left == None and x * 2 <= size:
			nodeList[x].left = nodeList[x*2]
		if nodeList[x].right == None and (x * 2 + 1) <= size:
			nodeList[x].right = nodeList[x * 2 + 1]
	# for x in range(offset, size+offset):
	# 	print(nodeList[x].value, end=", ")
	# 	if nodeList[x].left == None:
	# 		print("None", end=", ")
	# 	else:
	# 		print(nodeList[x].left.value, end=", ")
	# 	if nodeList[x].right == None:
	# 		print("None")
	# 	else:
	# 		print(nodeList[x].right.value)

	# return the head of the balanced tree
	return nodeList[1]

def printTree(head, order):
	if head != None:
		if order == 0:
			print(head.value, end=" ")
			printTree(head.left, 0)
			printTree(head.right, 0)
		if order == 1:
			printTree(head.left, 1)
			print(head.value, end=" ")
			printTree(head.right, 1)
		if order == 2:
			printTree(head.left, 2)
			printTree(head.right, 2)
			print(head.value, end=" ")


a = createTree1(5)

balancedTree = createBalancedTree(15)
print("pre order")
printTree(balancedTree,0)
print()
print("in order")
printTree(balancedTree,1)
print()
print("post order")
printTree(balancedTree,2)
print()

tempNode = a
while tempNode != None:
	print(tempNode.value)
	tempNode = tempNode.left
