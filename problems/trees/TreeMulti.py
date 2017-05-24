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

