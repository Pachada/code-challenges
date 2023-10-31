"""
Number Of Ways To Traverse Graph
You're given two positive integers representing the width and height of a grid-shaped, rectangular graph. 
Write a function that returns the number of ways to reach the bottom right corner of the graph when starting at 
the top left corner. Each move you take must either go down or right. In other words, you can never move up or left in the graph.

For example, given the graph illustrated below, with width = 2 and height = 3, 
there are three ways to reach the bottom right corner when starting at the top left corner:

 _ _
|_|_|
|_|_|
|_|_|
Down, Down, Right
Right, Down, Down
Down, Right, Down
Note: you may assume that width * height >= 2. In other words, the graph will never be a 1x1 grid.

Sample Input
width = 4
height = 3
Sample Output
10

Hint 2
The number of ways to reach any position in the graph is equal to the number of ways 
to reach the position directly above it plus the number of ways to reach the position directly to its left. 
This is because you can only travel down and right.
"""

# O(nm) time | O(nm) space where n is the width of the graph and m is the height 
def numberOfWaysToTraverseGraph(width, height):
    # Solution using Dynamic Programming
    dp = [[0 for _ in range(width)] for _ in range(height)]

    # Initialize all of the corner values to 1 becasue there is only one way to reach the position
    for i in range(width):
        dp[0][i] = 1
    
    for j in range(height):
        dp[j][0] = 1
    
    # Fill the rest of the graph by adding the ways to reach the position from its left and above     
    for i in range(1, width):
        for j in range(1, height):
            dp[j][i] = dp[j -1][i] + dp[j][i-1]
    
    return dp[-1][-1] 
    

if __name__ == '__main__':
    width = 4
    height = 3
    print(numberOfWaysToTraverseGraph(width, height))