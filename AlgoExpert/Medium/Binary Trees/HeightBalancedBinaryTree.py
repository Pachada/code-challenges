"""
Height Balanced Binary Tree | AlgoExpert
You're given the root node of a Binary Tree. Write a function that returns true if this Binary Tree 
is height balanced and false if it isn't.

A Binary Tree is height balanced if for each node in the tree, 
the difference between the height of its left subtree and the height of its right subtree is at most 1.

Each BinaryTree node has an integer value, a left child node, and a right child node. 
Children nodes can either be BinaryTree nodes themselves or None / null.

Sample Input
tree = 1
     /   \
    2     3
  /   \     \
 4     5     6
     /   \
    7     8
Sample Output
true
"""


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def heightBalancedBinaryTree(tree):
    # Returns (is_balanced, height)
    def helper(tree):
        if not tree:
            return (True, 0)
        
        left_is_balanced, left_height = helper(tree.left)
        right_is_balanced, right_height = helper(tree.right)
        is_balanced = left_is_balanced and right_is_balanced and abs(left_height - right_height) <= 1
        
        return (is_balanced, max(left_height, right_height) + 1)
    
    return helper(tree)[0]
    