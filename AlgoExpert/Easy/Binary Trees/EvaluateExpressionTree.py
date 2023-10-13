"""
Evaluate Expression Tree | AlgoExpert
You're given a binary expression tree. Write a function to evaluate this tree mathematically and return a single resulting integer.

All leaf nodes in the tree represent operands, which will always be positive integers. 
All of the other nodes represent operators. There are 4 operators supported, each of which is represented by a negative integer:

-1: Addition operator, adding the left and right subtrees.
-2: Subtraction operator, subtracting the right subtree from the left subtree.
-3: Division operator, dividing the left subtree by the right subtree. If the result is a decimal, it should be rounded towards zero.
-4: Multiplication operator, multiplying the left and right subtrees.
You can assume the tree will always be a valid expression tree. Each operator also works as a grouping symbol, meaning the bottom of the tree is always evaluated first, regardless of the operator.

Sample Input
tree =    -1
        /     \
      -2       -3
     /   \    /  \
   -4     2  8    3
  /   \
 2     3
Sample Output
6 // (((2 * 3) - 2) + (8 / 3))

"""

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(n) number of nodes in the tree | O(h) space, h is the height of the BT 
def evaluateExpressionTree(tree: BinaryTree) -> int:
    # si es negativo es que es un operador
    # si es positivo es un operando
    if tree.value >= 0:
        return tree.value
    
    match tree.value:
        case -1:
            return evaluateExpressionTree(tree.left) + evaluateExpressionTree(tree.right)
        case -2:
            return evaluateExpressionTree(tree.left) - evaluateExpressionTree(tree.right)
        case -3:
            return int(evaluateExpressionTree(tree.left) / evaluateExpressionTree(tree.right))
        case -4:
            return evaluateExpressionTree(tree.left) * evaluateExpressionTree(tree.right)


if __name__ == "__main__":
    tree = BinaryTree(-3)
    tree.left = BinaryTree(9)
    tree.right = BinaryTree(-2)
    tree.right.left = BinaryTree(4)
    tree.right.right = BinaryTree(6)
    print(evaluateExpressionTree(tree))