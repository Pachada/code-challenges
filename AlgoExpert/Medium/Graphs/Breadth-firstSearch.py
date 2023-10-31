"""
Breadth-first Search | AlgoExpert
You're given a Node class that has a name and an array of optional children nodes. 
When put together, nodes form an acyclic tree-like structure.

Implement the breadthFirstSearch method on the Node class, which takes in an empty array, 
traverses the tree using the Breadth-first Search approach (specifically navigating the tree from left to right), 
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
["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
"""


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self
    
    # O(v+e) time where v is the number of nodes and e the number of edges
    # O(v) 
    def breadthFirstSearch(self, array):
        queue = [self]
        while queue:
            current_node = queue.pop(0)
            array.append(current_node.name)
            queue.extend(current_node.children)
        
        return array
    

if __name__ == "__main__":
    graph = Node("A")
    graph.addChild("B").addChild("C").addChild("D")
    graph.children[0].addChild("E").addChild("F")
    graph.children[2].addChild("G").addChild("H")
    graph.children[0].children[1].addChild("I").addChild("J")
    graph.children[2].children[0].addChild("K")
    print(graph.breadthFirstSearch([]))
    
            



        
