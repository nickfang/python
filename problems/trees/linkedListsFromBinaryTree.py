import TreeBin as T


class Node(object):
	def __init__(self, value):
		self.value = value
		self.next = None

def linkedListFromBinaryTree(head):
	linkLists = []
	nodeList = []
	values = []
	nodeList.append(head)
	numNodes = 1
	numNextNodes = 0
	level = 0
	linkLists.append(None)
	while numNodes > 0:
		treeNode = nodeList.pop(0)
		values.append(Node(treeNode.value))

		if treeNode.left != None:
			nodeList.append(treeNode.left)
			numNextNodes += 1
		if treeNode.right != None:
			nodeList.append(treeNode.right)
			numNextNodes += 1
		numNodes -= 1
		if numNodes == 0:
			linkLists[level] = values[0]
			for x in range(1, len(values)):
				values[x-1].next = values[x]
			values = []
			numNodes, numNextNodes = numNextNodes, numNodes
			level += 1
			linkLists.append(None)
	return linkLists

def printList(head):
	tempNode = head
	while tempNode != None:
		print(tempNode.value, end=" ")
		tempNode = tempNode.next
	print()

a = T.createBST(20)
T.displayTree(a)
output = linkedListFromBinaryTree(a)
for itr in output:
	printList(itr)