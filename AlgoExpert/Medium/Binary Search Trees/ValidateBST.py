"""
Validate BST | AlgoExpert
Write a function that takes in a potentially invalid Binary Search Tree (BST) and returns a boolean 
representing whether the BST is valid.

Each BST node has an integer value, a left child node, and a right child node. 
A node is said to be a valid BST node if and only if it satisfies the BST property: 
its value is strictly greater than the values of every node to its left; 
its value is less than or equal to the values of every node to its right; 
and its children nodes are either valid BST nodes themselves or None / null.

A BST is valid if and only if all of its nodes are valid BST nodes.

Sample Input
tree =   10
       /     \
      5      15
    /   \   /   \
   2     5 13   22
 /           \
1            14
Sample Output
true
"""
# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        # Initialize the Binary Search Tree (BST) with a value.
        # The left and right child nodes are set to None.
        self.value = value
        self.left = None
        self.right = None

# O(n) time where n is the number of nodes in the BST | o(d) space where d is the depth of the BST
def validateBst(tree, max_value=float("inf"), min_value=float("-inf")):
    # If the tree is empty, it is a valid BST.
    if tree is None:
        return True
    
    # If the value of the node is not within the valid range, it is not a valid BST.
    if tree.value >= max_value or tree.value < min_value:
        return False
    
    # Recursively validate the right and left subtrees.
    # For the right subtree, the minimum value is updated to the current node's value.
    # For the left subtree, the maximum value is updated to the current node's value.
    return validateBst(tree.right, max_value, tree.value) and validateBst(tree.left, tree.value, min_value)


    
    

if __name__ == "__main__":
    root = BST(10)
    root.left = BST(5)
    root.left.left = BST(2)
    root.left.left.left = BST(1)
    root.left.right = BST(5)
    root.right = BST(15)
    root.right.left = BST(13)
    root.right.left.right = BST(14)
    root.right.right = BST(22)
    print(validateBst(root))
    
    
    
    
