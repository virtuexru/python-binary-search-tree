"""
Python Binary Search Tree
* requirements: Python 3.x

A binary search tree or ordered binary tree is a node-based binary tree data structure which has the following properties:
 - The left subtree of a node contains only nodes with keys less than the node’s key.
 - The right subtree of a node contains only nodes with keys greater than the node’s key.
 - Both the left and right subtrees must also be binary search trees.
"""

class Node:
	def __init__(self, root):
		self.root = root

		self.left = None
		self.right = None

		self.counter = 0

	def insert(self, nodeValue):
		"""
		Inserts new node node
		"""
		if nodeValue < self.root:
			if self.left is None:
				self.left = Node(nodeValue)
			else:
				self.left.insert(nodeValue)
		else:
			if self.right is None:
				self.right = Node(nodeValue)
			else:
				self.right.insert(nodeValue)

	def search(self, needle, parent=None):
		"""
		Searches for a node and returns it if found,
		along with it's parent
		"""
		if needle < self.root:
			if self.left is None:
				return None, None
			return self.left.search(needle, self)
		elif needle > self.root:
			if self.right is None:
				return None, None
			return self.right.search(needle, self)
		else:
			return self, parent

	def lookupDepth(self, depth=1):
		"""
		Recursive function to get the depth of tree
		"""
		if self.left is None:
			return depth
		else:
			return self.left.lookupDepth(depth + 1)

		if self.right is None:
			return depth
		else:
			return self.right.lookupDepth(depth + 1)

	def viewNodes(self):
		"""
		Generator to get the nodes data
		"""
		stack = []
		node = self

		while stack or node:
			if node:
				stack.append(node)
				node = node.left
			else:
				node = stack.pop()
				yield node.root
				node = node.right

	def __repr__(self):
		return "NodeTree({!r})".format(self.root)

"""
Example usage
"""

root = Node(8)
print(root)

for i in [3, 10, 1, 6, 4, 7, 14, 13]:
	root.insert(i)

node, parent = root.search(6)
print(node, parent)

print('*' * 20)

print(root.lookupDepth())

for d in root.viewNodes():
	print(d)

print('*' * 20)

tree = Node(10)

for i in [5, 7, 15, 4, 13, 17]:
	tree.insert(i)

for d in tree.viewNodes():
	print(d)