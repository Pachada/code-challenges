"""
Find Successor | AlgoExpert
Write a function that takes in a Binary Tree (where nodes have an additional pointer to their parent node) 
as well as a node contained in that tree and returns the given node's successor.

A node's successor is the next node to be visited (immediately after the given node) 
when traversing its tree using the in-order tree-traversal technique. 
A node has no successor if it's the last node to be visited in the in-order traversal.

If a node has no successor, your function should return None / null.

Each BinaryTree node has an integer value, a parent node, a left child node, and a right child node. 
Children nodes can either be BinaryTree nodes themselves or None / null.

Sample Input
tree = 
              1
            /   \
           2     3
         /   \ 
        4     5
       /       
      6  
node = 5   
Sample Output
1
// This tree's in-order traversal order is:
// 6 -> 4 -> 2 -> 5 -> 1 -> 3 
// 1 comes immediately after 5.
"""

# This is an input class. Do not edit.


class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self) -> str:
        return f"{self.value}"


# O(h) time | O(1) space 
def findSuccessor(tree, node):
    """
    Pseudo
    1. if it has a right child, then traverse right and then keep going left, return leaf
    2. otherwise, repeatedly find parent until we find a "rightside" parent, where our subtree was its left child.
    3. if this also fails, return None
    """
    if node.right is not None:
        node = node.right
        while node.left is not None:
            node = node.left
        return node
    
    else:
        prev = node
        parent = node.parent
        while parent is not None:
            if parent.left == prev:
                return parent
            else:
                prev, parent = parent, parent.parent


if __name__ == '__main__':
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.left.parent = root
    root.right = BinaryTree(3)
    root.right.parent = root
    root.left.left = BinaryTree(4)
    root.left.left.parent = root.left
    root.left.right = BinaryTree(5)
    root.left.right.parent = root.left
    root.left.left.left = BinaryTree(6)
    root.left.left.left.parent = root.left.left
    node = root.left.right
    expected = root
    print(findSuccessor(root, root.left.right))
