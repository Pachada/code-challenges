"""
Reconstruct BST | AlgoExpert
The pre-order traversal of a Binary Tree is a traversal technique that starts at the tree's root node 
and visits nodes in the following order:

Current node
Left subtree
Right subtree
Given a non-empty array of integers representing the pre-order traversal of a Binary Search Tree (BST), 
write a function that creates the relevant BST and returns its root node.

The input array will contain the values of BST nodes in the order in which these nodes would be visited with a pre-order traversal.

Each BST node has an integer value, a left child node, and a right child node. 
A node is said to be a valid BST node if and only if it satisfies the BST property: 
its value is strictly greater than the values of every node to its left; 
its value is less than or equal to the values of every node to its right; 
and its children nodes are either valid BST nodes themselves or None / null.

Sample Input
preOrderTraversalValues = [10, 4, 2, 1, 5, 17, 19, 18]
Sample Output
        10 
      /    \
     4      17
   /   \      \
  2     5     19
 /           /
1           18 
"""

# This is an input class. Do not edit.


class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        # sourcery skip: extract-method, hoist-repeated-if-condition, inline-variable, replace-interpolation-with-fstring
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle
        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2
        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2
        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

# O(n) time | O(n) space 
def recursive_reconstructBst(preOrderTraversalValues):
    def helper(arr, start_idx, end_idx):
        if start_idx > end_idx:
            return

        root = BST(arr[start_idx])
        end_of_left_subtree = end_idx
        while end_of_left_subtree > start_idx and arr[end_of_left_subtree] >= root.value:
            end_of_left_subtree -= 1

        root.left = helper(arr, start_idx+1, end_of_left_subtree)
        root.right = helper(arr, end_of_left_subtree+1, end_idx)

        return root

    return helper(preOrderTraversalValues, 0, len(preOrderTraversalValues)-1)

# O(n) time | O(n) space 
def iterative_recursive_reconstructBST(preOrderTraversalValues):
    root = BST(preOrderTraversalValues.pop(0))
    left_values, right_values = [], []
    for value in preOrderTraversalValues:
        if value < root.value:
            left_values.append(value)
        else:
            right_values.append(value)
    
    if left_values:
        root.left = iterative_recursive_reconstructBST(left_values)
    if right_values:
        root.right = iterative_recursive_reconstructBST(right_values)
    
    return root

if __name__ == "__main__":
    preOrderTraversalValues = [10, 4, 2, 1, 5, 17, 19, 18]
    root = iterative_recursive_reconstructBST(preOrderTraversalValues)
    root.display()
    preOrderTraversalValues = [10, 4, 2, 1, 5, 17, 19, 18]
    root = recursive_reconstructBst(preOrderTraversalValues)
    root.display()
