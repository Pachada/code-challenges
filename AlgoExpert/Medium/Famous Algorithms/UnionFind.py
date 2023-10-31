"""
Union Find | AlgoExpert
The union-find data structure is similar to a traditional set data structure in that it contains a collection of unique values. 
However, these values are spread out amongst a variety of distinct disjoint sets, 
meaning that no set can have duplicate values, and no two sets can contain the same value.

Write a UnionFind class that implements the union-find (also called a disjoint set) data structure. 
This class should support three methods:

createSet(value): Adds a given value in a new set containing only that value.
union(valueOne, valueTwo): Takes in two values and determines which sets they are in. If they are in different sets, 
the sets are combined into a single set. If either value is not in a set or they are in the same set, 
the function should have no effect.
find(value): Returns the "representative" value of the set for which a value belongs to. 
This can be any value in the set, but it should always be the same value, 
regardless of which value in the set find is passed. If the value is not in a set, the function should return null / None. 

Note that after a set is part of a union, its representative can potentially change.
You can assume createSet will never be called with the same value twice.

If you're unfamiliar with Union Find, we recommend watching the Conceptual Overview section of this question's video explanation 
before starting to code.

Sample Usage
createSet(5): null
createSet(10): null
find(5): 5
find(10): 10
union(5, 10): null
find(5): 5
find(10): 5
createSet(20): null
find(20): 20
union(20, 10): null
find(5): 5
find(10): 5
find(20): 5
"""


# Define a Union-Find data structure class
class UnionFind:
    # Initialize empty dictionaries for ranks and parents
    def __init__(self):
        self.ranks = {}
        self.parents = {}

    # Create a new set with the given value as its only element
    def createSet(self, value):
        self.ranks[value] = 0  # Initialize rank to 0
        self.parents[value] = value  # The parent of the value is itself

    # Find the representative of the set containing the given value
    def find(self, value):
        # If the value is not present, return None
        if value not in self.parents:
            return None
        
        # Path compression: update the parent pointer to the root of the set
        if value != self.parents[value]:
            self.parents[value] = self.find(self.parents[value])
        
        # Return the root of the set
        return self.parents[value]

    # Merge the sets containing valueOne and valueTwo
    def union(self, valueOne, valueTwo):
        # If either value is not present, return without doing anything
        if valueOne not in self.parents or valueTwo not in self.parents:
            return
        
        # Find the roots of the sets containing valueOne and valueTwo
        value_one_root = self.find(valueOne)
        value_two_root = self.find(valueTwo)

        # Union by rank: attach the smaller tree to the larger tree
        if self.ranks[value_one_root] < self.ranks[value_two_root]:
            self.parents[value_one_root] = value_two_root
        elif self.ranks[value_one_root] > self.ranks[value_two_root]:
            self.parents[value_two_root] = value_one_root
        else:
            # If ranks are equal, make one root and increment its rank
            self.parents[value_two_root] = value_one_root
            self.ranks[value_one_root] += 1


