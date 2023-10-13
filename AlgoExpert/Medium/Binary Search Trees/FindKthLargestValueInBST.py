"""
Find Kth Largest Value In BST
Write a function that takes in a Binary Search Tree (BST) and a positive integer k 
and returns the kth largest integer contained in the BST.

You can assume that there will only be integer values in the BST and that k is less than or equal to 
the number of nodes in the tree.

Also, for the purpose of this question, duplicate integers will be treated as distinct values. 
In other words, the second largest value in a BST containing values {5, 7, 7} will be 7—not 5.

Each BST node has an integer value, a left child node, and a right child node. 
A node is said to be a valid BST node if and only if it satisfies the BST property: 
its value is strictly greater than the values of every node to its left; 
its value is less than or equal to the values of every node to its right; 
and its children nodes are either valid BST nodes themselves or None / null.

Sample Input
tree =   15
       /     \
      5      20
    /   \   /   \
   2     5 17   22
 /   \         
1     3       
k = 3
Sample Output
17
"""

# O(h + k) time | O(h) space - where h is the height of the tree and k is the input parameter
def findKthLargestValueInBst(tree, k):
    count = 1
    stack = []
    curr = tree
    while stack or curr:
        if curr is not None:
            stack.append(curr)
            curr = curr.right
        elif stack:
            curr = stack.pop()
            if count == k:
                return curr.value
            
            count += 1
            curr = curr.left
            
    
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def __repr__(self) -> str:
        return f"{self.value}"

if __name__ == '__main__':
    root = BST(15)
    root.left = BST(5)
    root.left.left = BST(2)
    root.left.left.left = BST(1)
    root.left.left.right = BST(3)
    root.left.right = BST(5)
    root.right = BST(20)
    root.right.right = BST(22)
    root.right.left = BST(17)
    k = 3
    print(findKthLargestValueInBst(root, k))
    assert findKthLargestValueInBst(root, k) == 17


