# Implement a binary search tree and write functions to insert, delete and search for elements.


class Node:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self.insertT(self.root, key)

    def insertT(self, node, key):
        if key > node.key:
            if node.right is None:
                node.right = Node(key)
            else:
                self.insertT(node.right, key)
        elif key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self.insertT(node.left, key)

    def deleteT(self):
        self.root = None

    def printTree(self, node=None):
        if node is None:
            node = self.root
        if node is not None:
            if node.left is not None:
                self.printTree(node.left)
            print(node.key)
            if node.right is not None:
                self.printTree(node.right)


tree = Tree()
tree.insert(10)
tree.insert(12)
tree.insert(2)
tree.insert(11)
tree.insert(5)
tree.printTree()
tree.deleteT()
print("\nTree after deleting all nodes:")
tree.printTree()
