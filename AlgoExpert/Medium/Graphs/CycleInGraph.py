"""
Cycle In Graph | AlgoExpert
You're given a list of edges representing an unweighted, directed graph with at least one node. 
Write a function that returns a boolean representing whether the given graph contains a cycle.

For the purpose of this question, a cycle is defined as any number of vertices, 
including just one vertex, that are connected in a closed chain. 
A cycle can also be defined as a chain of at least one vertex in which the first vertex is the same as the last.

The given list is what's called an adjacency list, and it represents a graph. 
The number of vertices in the graph is equal to the length of edges, 
where each index i in edges contains vertex i's outbound edges, in no particular order. 
Each individual edge is represented by a positive integer that denotes an index (a destination vertex) 
in the list that this vertex is connected to. Note that these edges are directed, 
meaning that you can only travel from a particular vertex to its destination, 
not the other way around (unless the destination vertex itself has an outbound edge to the original vertex).

Also note that this graph may contain self-loops. A self-loop is an edge that has the same destination and origin; 
in other words, it's an edge that connects a vertex to itself. For the purpose of this question, a self-loop is considered a cycle.


Sample Input
edges = [
  [1, 3],
  [2, 3, 4],
  [0],
  [],
  [2, 5],
  [],
]
Sample Output
true 
// There are multiple cycles in this graph: 
// 1) 0 -> 1 -> 2 -> 0
// 2) 0 -> 1 -> 4 -> 2 -> 0
// 3) 1 -> 2 -> 0 -> 1
// These are just 3 examples; there are more.
"""

# O(v+e) time | O(v) space
def cycleInGraph(graph):
    # Helper function for DFS
    def dfs(vertex, visited, recursionStack):
        visited[vertex] = True  # Mark the current node as visited
        recursionStack[vertex] = True  # Add the current node to the recursion stack

        # Recur for all the vertices adjacent to this vertex
        for neighbour in graph[vertex]:
            # If the neighbour hasn't been visited, recursively visit it
            if not visited[neighbour]:
                if dfs(neighbour, visited, recursionStack):
                    return True
            # If the neighbour is in the recursion stack, there's a cycle
            elif recursionStack[neighbour]:
                return True

        # Remove the vertex from the recursion stack as we backtrack
        recursionStack[vertex] = False
        return False

    # Initialize visited and recursion stack arrays
    visited = [False] * len(graph)
    recursionStack = [False] * len(graph)

    # Check for cycle in different DFS trees
    for node in range(len(graph)):
        # If not visited, start DFS from this node
        if not visited[node] and dfs(node, visited, recursionStack):
            return True  # Cycle found
    return False  # No cycle found

if __name__ == '__main__':
    edges = [
        [1, 3],
        [2, 3, 4],
        [0],
        [],
        [2, 5],
        [],
    ]
    print(cycleInGraph(edges))  # Expected Output: True


