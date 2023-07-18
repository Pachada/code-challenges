"""
You're given a Node class that has a name and an array of optional children nodes. 
When put together, nodes form an acyclic tree-like structure.

Implement the depthFirstSearch method on the Node class, which takes in an empty array, 
traverses the tree using the Depth-first Search approach (specifically navigating the tree from left to right), 
stores all of the nodes' names in the input array, and returns it.


Sample Input
graph = A
     /  |  \
    B   C   D
   / \     / \
  E   F   G   H
     / \   \
    I   J   K
Sample Output
["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"]
"""


from typing import List


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # O(v + e) time v = vertices, e = edges | O(v) space
    def depthFirstSearch(self, array:List):
        array.append(self.name)
        for node in self.children:
            node.depthFirstSearch(array)
        return array
