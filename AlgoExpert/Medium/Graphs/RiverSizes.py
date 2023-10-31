"""
River Sizes | AlgoExpert
You're given a two-dimensional array (a matrix) of potentially unequal height and width containing only 0s and 1s. 
Each 0 represents land, and each 1 represents part of a river. 
A river consists of any number of 1s that are either horizontally or vertically adjacent (but not diagonally adjacent). 
The number of adjacent 1s forming a river determine its size.

Note that a river can twist. In other words, it doesn't have to be a straight vertical line or a straight horizontal line; 
it can be L-shaped, for example.

Write a function that returns an array of the sizes of all rivers represented in the input matrix. 
The sizes don't need to be in any particular order.

Sample Input
matrix = [
  [1, 0, 0, 1, 0],
  [1, 0, 1, 0, 0],
  [0, 0, 1, 0, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 1, 1, 0],
]
Sample Output
[1, 2, 2, 2, 5] // The numbers could be ordered differently.

// The rivers can be clearly seen here:
// [
//   [1,  ,  , 1,  ],
//   [1,  , 1,  ,  ],
//   [ ,  , 1,  , 1],
//   [1,  , 1,  , 1],
//   [1,  , 1, 1,  ],
// ]
"""


# Function to get the size of a "river" starting from a given cell (row, col) in the matrix
def get_river_size(row, col, matrix):
    # Base case: if out of bounds or cell value is not 1, return 0
    if row not in range(len(matrix)) or col not in range(len(matrix[0])) or matrix[row][col] != 1:
        return 0

    # Mark the current cell as visited by setting its value to -1
    matrix[row][col] = -1

    # Initialize the size of this "river"
    size = 0

    # Define possible directions to move (right, down, left, up)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Recursive call to visit all connected cells that are part of this "river"
    for dx, dy in directions:
        size += get_river_size(row + dx, col + dy, matrix)

    # Add 1 to the size for the current cell and return
    return 1 + size

# O(wh) time where w is the width of the matrix and h is the height
# O(wh) space 
def riverSizes(matrix: list[list[int]]):
    rows, cols = len(matrix), len(matrix[0])
    rivers_sizes = []  # List to store sizes of all found "rivers"

    # Iterate through each cell in the matrix
    for row in range(rows):
        for col in range(cols):
            # If a "river" is found (cell value is 1)
            if matrix[row][col] == 1:
                # Get its size using DFS and append to the list
                size = get_river_size(row, col, matrix)
                rivers_sizes.append(size)

    return rivers_sizes


if __name__ == '__main__':
    matrix = [
        [1, 0, 0, 1, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 0],
    ]

    print(riverSizes(matrix))



