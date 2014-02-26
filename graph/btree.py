#!/usr/bin/env python

class Node(object):
    def __init__(self, val):
        self.val = val 
        self.left = None
        self.right = None
        self.height = None


class btree(object):
    def __init__(self):
        self.root = None

    def create(self, val):

        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
            while True:
                if val < current.val:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.val:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print node.val
            self.inorder(node.right)

    def preorder(self, node):
        if node is not None:
            print node.val
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print node.val
    
 
tree = btree()
from random import randint
arr = [randint(1, 100) for x in xrange(15)]
print "this is array", arr

for i in arr:
    tree.create(i)

print "Inorder traversal"
print tree.inorder(tree.root)

