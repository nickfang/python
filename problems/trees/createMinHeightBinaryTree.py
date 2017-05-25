# given a sorted array, create a binary tree with minimal height

import TreeBin as T

def createBST(size):
	values = [x for x in range(size)]
	return addNode(values, 0, size-1)

def addNode(values, start, end):
	if (end < start):
		return None
	mid = (start + end) // 2
	tempNode = T.Node(values[mid])
	tempNode.left = addNode(values, start, mid - 1)
	tempNode.right = addNode(values, mid + 1, end)
	return tempNode


size = 32
T.displayTree(createBST(size))