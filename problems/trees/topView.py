import TreeBin as Tree

tree = Tree.createBST(10)

Tree.displayTree(tree)


def traverse(root, traverseLeft):
	if root == None:
		return
	if traverseLeft:
		traverse(root.left, traverseLeft)
		print(root.value, end=" ")
	else:
		print(root.value, end=" ")
		traverse(root.right, traverseLeft)


def topView(root):
	if root == None:
		return
	traverse(root, True)
	traverse(root.right, False)

topView(tree)