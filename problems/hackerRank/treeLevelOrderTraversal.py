#!/bin/python3

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)

a.right = b
b.right = e
e.left = c
e.right = f
c.right = d


def levelOrder(root):
    output = ""
    queue = []
    queue.append(root)
    while len(queue) > 0:
        tempNode = queue.pop(0)
        output += str(tempNode.data) + " "
        if tempNode.left:
            queue.append(tempNode.left)
        if tempNode.right:
            queue.append(tempNode.right)
    print(output.strip())

levelOrder(a)