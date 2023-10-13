"""
You're given a 2D array of integers matrix. Write a function that returns the transpose of the matrix.

The transpose of a matrix is a flipped version of the original matrix across its main diagonal (which runs from top-left to bottom-right); 
it switches the row and column indices of the original matrix.

You can assume the input matrix always has at least 1 value; however its width and height are not necessarily the same.

Sample Input #1
matrix = [
  [1, 2],
]
Sample Output # 1
[
  [1],
  [2]
]
Sample Input #2
matrix = [
  [1, 2],
  [3, 4],
  [5, 6]
]
Sample Output #2
[
  [1, 3, 5],
  [2, 4, 6]
]
Sample Input #3
matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
Sample Output #3
[
  [1, 4, 7],
  [2, 5, 8],
  [3, 6, 9]
]
"""


def transposeMatrix_Python(matrix):
    return [list(row) for row in zip(*matrix)]


# O(nm )time | O(nm) space where n is the number of rows and m is the number of columns
def transposeMatrix(matrix) -> list[list[int]]:
    result = [[] for _ in range(len(matrix[0]))] 
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result[j].insert(i,matrix[i][j])
    
    return result

matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

print(transposeMatrix(matrix))

