import TreeBin as Tree

# build tree
a = Tree.Node(3)
a.left = Tree.Node(2)
a.right = Tree.Node(4)
a.right.right = Tree.Node(5)



def getHeight(root):
	if root == None:
		return 0
	lHeight = getHeight(root.left)
	rHeight = getHeight(root.right)
	return ( 1 + max(lHeight, rHeight) )


def getBalanceFactor(root):
	if root == None:
		return 0
	print("Node:", root.value, "| BF:", getHeight(root.left) - getHeight(root.right))
	getBalanceFactor(root.left)
	getBalanceFactor(root.right)


def insert(root, val):
	tempNode = root
	while tempNode != None:
		if val > tempNode.value:
			if tempNode.right == None:
				tempNode.right = Tree.Node(val)
				break
			else:
				tempNode = tempNode.right
		else:
			if tempNode.left == None:
				tempNode.left = Tree.Node(val)
				break
			else:
				tempNode = tempNode.left
	# rotate nodes to balance the tree
	tempNode = root
	bf = getBalanceFactor(tempNode)
	if (bf > 1):




insert(a, 6)
Tree.displayTree(a)

getBalanceFactor(a)