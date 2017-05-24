import TreeBin as Tree

# Implement a function to check if a tree is balanced.  For the purposes of this question, a balanced tree is defined to be a tree such that no two leaf nodes differ in distance from the root by more than one.


balancedTree = Tree.createBalancedTree(15)
print(Tree.displayTree(balancedTree))
unbalancedTree = Tree.createUnbalancedTree(15)

print("pre order")
Tree.printTree(balancedTree,0)
print("in order")
Tree.printTree(balancedTree,1)
print("post order")
Tree.printTree(balancedTree,2)

Tree.printTree(unbalancedTree)

