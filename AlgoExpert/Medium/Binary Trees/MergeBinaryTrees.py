"""
Merge Binary Trees | AlgoExpert
Given two binary trees, merge them and return the resulting tree. 
If two nodes overlap during the merger then sum the values, otherwise use the existing node.

Note that your solution can either mutate the existing trees or return a new tree.

Sample Input
tree1 =   1
        /   \
       3     2
     /   \
    7     4

tree2 =   1
        /   \
       5     9
     /      / \
    2      7   6
Sample Output
output =  2
        /   \
      8      11
    /  \    /  \
  9     4  7    6
"""


# This is an input class. Do not edit.
class BinaryTree:
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


# O(n) time where n is the len of the smallest tree
# O(h) where h is the height of the smallest tree
def mergeBinaryTrees(tree1: BinaryTree, tree2: BinaryTree):
    if not tree1 and not tree2:
        return None
    
    if not tree1 or not tree2:
        return tree1 or tree2
    
    # Merge the nodes
    tree1.value += tree2.value
    tree1.left = mergeBinaryTrees(tree1.left, tree2.left)
    tree1.right = mergeBinaryTrees(tree1.right, tree2.right)
    
    return tree1


if __name__ == "__main__":
    tree1 = BinaryTree(1)
    tree1.right = BinaryTree(2)
    tree1.left = BinaryTree(3)
    tree1.left.left = BinaryTree(7)
    tree1.left.right = BinaryTree(4)

    tree2 = BinaryTree(1)
    tree2.left = BinaryTree(5)
    tree2.left.left = BinaryTree(2)
    tree2.right = BinaryTree(9)
    tree2.right.left = BinaryTree(7)
    tree2.right.right = BinaryTree(6)

    merge_tree = mergeBinaryTrees(tree1, tree2)

    merge_tree.display()
    

    
    