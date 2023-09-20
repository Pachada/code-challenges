"""
BST Construction | AlgoExpert
Write a BST class for a Binary Search Tree. The class should support:

Inserting values with the insert method.
Removing values with the remove method; this method should only remove the first instance of a given value.
Searching for values with the contains method.
Note that you can't remove values from a single-node tree. In other words, calling the remove method on a single-node tree should simply not do anything.

Each BST node has an integer value, a left child node, and a right child node. A node is said to be a valid BST node if and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left; its value is less than or equal to the values of every node to its right; and its children nodes are either valid BST nodes themselves or None / null.

Sample Usage
// Assume the following BST has already been created:
         10
       /     \
      5      15
    /   \   /   \
   2     5 13   22
 /           \
1            14

// All operations below are performed sequentially.
insert(12):   10
            /     \
           5      15
         /   \   /   \
        2     5 13   22
      /        /  \
     1        12  14

remove(10):   12
            /     \
           5      15
         /   \   /   \
        2     5 13   22
      /           \
     1            14

contains(15): true
"""

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):  # sourcery skip: merge-else-if-into-elif
        # Write your code here.
        # Do not edit the return statement of this method.
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BST(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BST(value)
        return self
            
    def contains(self, value):  # sourcery skip: assign-if-exp, reintroduce-else
        # Write your code here.
        if value < self.value:
            if self.left:
                return self.left.contains(value)
            return False
        elif value > self.value:
            if self.right:
                return self.right.contains(value)
            return False
        return True

    def remove(self, value):  # sourcery skip: merge-else-if-into-elif
        if not self:
            return self
        # Search the node to be deleted
        if value < self.value:
            if self.left:
                self.left = self.left.remove(value)
        elif value > self.value:
            if self.right:
                self.right = self.right.remove(value)
        else:
            # case 1: Node to be deleted is a Leaf Node
            if not self.right and not self.left:
                return None
            # case 2: Node to be deleted has only 1 child(either left or right)
            elif not self.left:
                self.value = self.right.value
                self.left = self.right.left
                self.right = self.right.right
                return self
            elif not self.right:
                self.value = self.left.value
                self.right = self.left.right
                self.left = self.left.left
                return self
            # case 3: Node to be deleted has both children
            else:
                successor = self.right.inOrderSuccessor()
                self.value = successor.value
                self.right = self.right.remove(successor.value)
                
        return self

    def inOrderSuccessor(self):
        while self.left:
            self = self.left
        return self

    
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

if __name__ == "__main__":
    root = BST(10)
    root.display()
    root.insert(5)
    root.display()
    root.insert(15)
    root.display()
    print("Removing 5")
    root.remove(5)
    root.display()
    print("Removing 15")
    root.remove(15)
    root.display()
    print("Removing 10")
    root.remove(10)
    root.display()