"""Implements a binary search tree: a type of tree that uses an ordering on the elements of some
collection to efficiently search for items in that collection (average-case O(log n) time)."""

from binarytree import Node, Tree


class BST_Node(Node):
    def add_Node(self, node):
        if
    #Comparison methods
    def compare_To(self, other):
        if self.content==other.content:
            return 0
        else if self.content > other.content:
            return 1
        return -1
    def updateFactor(self):
        self.balanceFactor= height(self.left) − height(self.right)
class BST_Tree(Tree):
    def add_Root(self, node):
        if self.root == None
            self.root = node
        if node.compare_To(self.root) == 1:
            node.left = self.root
            self.root = node
            return True
        else if node.compare_To(self.root) == -1:
            self.root = node.right
            self.root = node
            return True
        return False
    def add_Node(self, node):
        if node.compareTo(self.root) == 1:
