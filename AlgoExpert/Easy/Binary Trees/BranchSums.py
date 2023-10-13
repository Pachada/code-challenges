"""
Write a function that takes in a Binary Tree and returns a list of its branch sums ordered from 
leftmost branch sum to rightmost branch sum.

A branch sum is the sum of all values in a Binary Tree branch. A Binary Tree branch is a path 
of nodes in a tree that starts at the root node and ends at any leaf node.

Each BinaryTree node has an integer value, a left child node, and a right child node. 
Children nodes can either be BinaryTree nodes themselves or None / null.

Sample Input
tree =     1
        /     \
       2       3
     /   \    /  \
    4     5  6    7
  /   \  /
 8    9 10
Sample Output
[15, 16, 18, 10, 11]
// 15 == 1 + 2 + 4 + 8
// 16 == 1 + 2 + 4 + 9
// 18 == 1 + 2 + 5 + 10
// 10 == 1 + 3 + 6
// 11 == 1 + 3 + 7
"""

from typing import List

# This is the class of the input root.


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# O(n) time | O(n) space
def branchSumHelper(node: BinaryTree, current_branch_sum: int, sums: List[int] = None) -> List[int]:
    if sums is None:
        sums = []

    if node is None:
        return

    current_branch_sum += node.value

    if not node.left and not node.right:
        sums.append(current_branch_sum)

    branchSumHelper(node.left, current_branch_sum, sums)
    branchSumHelper(node.right, current_branch_sum, sums)

    return sums


def branchSums(root: BinaryTree) -> List[int]:
    return branchSumHelper(root, 0)
