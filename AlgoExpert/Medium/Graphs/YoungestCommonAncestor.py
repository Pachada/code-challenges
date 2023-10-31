"""
Youngest Common Ancestor | AlgoExpert
You're given three inputs, all of which are instances of an AncestralTree class that have an ancestor 
property pointing to their youngest ancestor. The first input is the top ancestor in an ancestral tree 
(i.e., the only instance that has no ancestor--its ancestor property points to None / null), and the other two inputs are descendants in the ancestral tree.

Write a function that returns the youngest common ancestor to the two descendants.

Note that a descendant is considered its own ancestor. So in the simple ancestral tree below, 
the youngest common ancestor to nodes A and B is node A.

// The youngest common ancestor to nodes A and B is node A.
  A
 /
B
Sample Input
// The nodes are from the ancestral tree below.
topAncestor = node A
descendantOne = node E
descendantTwo = node I
          A
       /     \
      B       C
    /   \   /   \
   D     E F     G
 /   \
H     I
Sample Output
node B
"""


class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

    def __repr__(self) -> str:
        return f"{self.name}"

    def addDescendants(self, *descendants):
        for descendant in descendants:
            descendant.ancestor = self


def new_trees():
    ancestralTrees = {}
    for letter in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        ancestralTrees[letter] = AncestralTree(letter)
    return ancestralTrees



# Function to find the depth of a descendant node from the top ancestor
def find_depth(current_node, top_ancestor):
    depth = 0
    while current_node != top_ancestor:
        current_node = current_node.ancestor
        depth += 1
    return depth

# O(d) time where d is the max depth | O(1) space
def getYoungestCommonAncestor(topAncestor: AncestralTree, descendantOne: AncestralTree, descendantTwo: AncestralTree):
    # Find the depth of each descendant from the top ancestor
    depth_one = find_depth(descendantOne, topAncestor)
    depth_two = find_depth(descendantTwo, topAncestor)

    # Equalize the depths of the two descendants
    # If one descendant is deeper, move it up until both are at the same depth
    while depth_one > depth_two:
        descendantOne = descendantOne.ancestor
        depth_one -= 1
    while depth_two > depth_one:
        descendantTwo = descendantTwo.ancestor
        depth_two -= 1

    # Find the common ancestor by moving both descendants up the tree
    # until they meet at the common ancestor
    while descendantOne != descendantTwo:
        descendantOne = descendantOne.ancestor
        descendantTwo = descendantTwo.ancestor

    return descendantOne  # Return the youngest common ancestor


if __name__ == "__main__":
    trees = new_trees()
    trees["A"].addDescendants(trees["B"], trees["C"])
    trees["B"].addDescendants(trees["D"], trees["E"])
    trees["D"].addDescendants(trees["H"], trees["I"])
    trees["C"].addDescendants(trees["F"], trees["G"])

    yca = getYoungestCommonAncestor(trees["A"], trees["E"], trees["I"])
    print(yca)
