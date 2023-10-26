"""
Symmetrical Tree | AlgoExpert
Write a function that takes in a Binary Tree and returns if that tree is symmetrical. 
A tree is symmetrical if the left and right subtrees are mirror images of each other.

Each BinaryTree node has an integer value, a left child node, and a right child node. 
Children nodes can either be BinaryTree nodes themselves or None / null.

Sample Input
tree =    1
       /     \
      2       2
    /   \   /   \
   3     4 4     3
 /   \          /  \
5     6        6    5
Sample Output
True
"""

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def symmetricalTree(tree):
    return check_nodes_are_symmetrical(tree.left, tree.right)

# O(n) time where n is the number of nodes | O(n) space
def check_nodes_are_symmetrical(tree1, tree2):
    if not tree1 and not tree2:
        return True

    if not tree1 or not tree2 or tree1.value != tree2.value:
        return False

    return (check_nodes_are_symmetrical(tree1.left, tree2.right) and
            check_nodes_are_symmetrical(tree1.right, tree2.left))


if __name__ == "__main__":
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.left.left = BinaryTree(3)
    root.left.left.left = BinaryTree(5)
    root.left.left.right = BinaryTree(6)
    root.left.right = BinaryTree(4)
    root.right = BinaryTree(2)
    root.right.right = BinaryTree(3)
    root.right.right.right = BinaryTree(5)
    root.right.right.left = BinaryTree(6)
    root.right.left = BinaryTree(4)
    print(symmetricalTree(root))

    
    