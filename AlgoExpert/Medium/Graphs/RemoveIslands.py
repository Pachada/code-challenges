"""
Remove Islands | AlgoExpert
You're given a two-dimensional array (a matrix) of potentially unequal height and width containing only 0s and 1s. 
The matrix represents a two-toned image, where each 1 represents black and each 0 represents white. 
An island is defined as any number of 1s that are horizontally or vertically adjacent (but not diagonally adjacent) 
and that don't touch the border of the image. 
In other words, a group of horizontally or vertically adjacent 1s isn't an island if any of those 1s are in the first row, 
last row, first column, or last column of the input matrix.

Note that an island can twist. In other words, it doesn't have to be a straight vertical line or a straight horizontal line; 
it can be L-shaped, for example.

You can think of islands as patches of black that don't touch the border of the two-toned image.

Write a function that returns a modified version of the input matrix, where all of the islands are removed. 
You remove an island by replacing it with 0s.

Naturally, you're allowed to mutate the input matrix.

Sample Input
matrix = 
[
  [1, 0, 0, 0, 0, 0],
  [0, 1, 0, 1, 1, 1],
  [0, 0, 1, 0, 1, 0],
  [1, 1, 0, 0, 1, 0],
  [1, 0, 1, 1, 0, 0],
  [1, 0, 0, 0, 0, 1],
]
Sample Output
[
  [1, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 1, 1],
  [0, 0, 0, 0, 1, 0],
  [1, 1, 0, 0, 1, 0],
  [1, 0, 0, 0, 0, 0],
  [1, 0, 0, 0, 0, 1],
] 
// The islands that were removed can be clearly seen here:
// [
//   [ ,  ,  ,  ,  , ],
//   [ , 1,  ,  ,  , ],
//   [ ,  , 1,  ,  , ],
//   [ ,  ,  ,  ,  , ],
//   [ ,  , 1, 1,  , ],
//   [ ,  ,  ,  ,  , ], 
// ]
"""

# O(W*H) time | O(W*H) space for the DFS stack calls
def removeIslands(matrix):
    def dfs(x, y):
        # Check for out-of-bounds or if the cell is not 1
        if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]) or matrix[x][y] != 1:
            return
        # Mark the cell as part of a non-removable area
        matrix[x][y] = -1
        # Explore adjacent cells
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)

    # Mark all 1s connected to borders as non-removable
    for i in range(len(matrix)):
        for j in [0, len(matrix[0]) - 1]:  # Only left and right borders
            if matrix[i][j] == 1:
                dfs(i, j)
    for j in range(len(matrix[0])):
        for i in [0, len(matrix) - 1]:  # Only top and bottom borders
            if matrix[i][j] == 1:
                dfs(i, j)

    # Convert islands to 0s and revert non-removable area marks back to 1s
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                matrix[i][j] = 0  # Island cell
            elif matrix[i][j] == -1:
                matrix[i][j] = 1  # Non-removable cell

    return matrix


if __name__ == '__main__':
    matrix = [
        [1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1],
        [0, 0, 1, 0, 1, 0],
        [1, 1, 0, 0, 1, 0],
        [1, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 1],
    ]
print(removeIslands(matrix))
