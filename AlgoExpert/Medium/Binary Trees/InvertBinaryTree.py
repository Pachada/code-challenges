"""
Invert Binary Tree | AlgoExpert
Write a function that takes in a Binary Tree and inverts it. In other words, the function should swap every left node in the tree for its corresponding right node.

Each BinaryTree node has an integer value, a left child node, and a right child node. Children nodes can either be BinaryTree nodes themselves or None / null.

Sample Input
tree =    1
       /     \
      2       3
    /   \   /   \
   4     5 6     7
 /   \
8     9
Sample Output
       1
    /     \
   3       2
 /   \   /   \
7     6 5     4
            /   \
           9     8
           
Sample Input
tree =   10
       /     \
      5      15
    /   \       \
   2     5       22
 /
1
"""


# O(n) time | O(n) space 
def invertBinaryTree(tree):
    if not tree:
        return
    
    invertBinaryTree(tree.left)
    tree.left, tree.right = tree.right, tree.left
    invertBinaryTree(tree.left)
    
    return tree


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

if __name__ == '__main__':
    root = BinaryTree(10)
    root.left = BinaryTree(5)
    root.left.left = BinaryTree(2)
    root.left.left.left = BinaryTree(1)
    root.left.right = BinaryTree(5)
    root.right = BinaryTree(15)
    root.right.right = BinaryTree(22)
    
    
    invertBinaryTree(root)