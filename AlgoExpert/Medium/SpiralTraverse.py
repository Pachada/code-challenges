"""
Spiral Traverse | AlgoExpert
Write a function that takes in an n x m two-dimensional array (that can be square-shaped when n == m) 
and returns a one-dimensional array of all the array's elements in spiral order.

Spiral order starts at the top left corner of the two-dimensional array, goes to the right, 
and proceeds in a spiral pattern all the way until every element has been visited.

Sample Input
array = [
  [1,   2,  3, 4],
  [12, 13, 14, 5],
  [11, 16, 15, 6],
  [10,  9,  8, 7],
]
Sample Output
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
"""

from typing import List


# O(nxm) time | O(nxm) space 
def spiralTraverse(array: List[List[int]]):
    res = []
    starting_row, starting_column = 0, 0
    ending_row, ending_column = len(array), len(array[0])
    while starting_row < ending_row and starting_column < ending_column:
        # rigth
        res.extend(
            array[starting_row][column]
            for column in range(starting_column, ending_column)
        )
        starting_row += 1

        # down
        res.extend(
            array[row][ending_column-1]
            for row in range(starting_row, ending_row)
        )
        ending_column -= 1

        if starting_row >= ending_row or starting_column >= ending_column:
            break

        # left
        res.extend(
            array[ending_row-1][column]
            for column in reversed(range(starting_column, ending_column))
        )
        ending_row -= 1

        # up
        res.extend(
            array[row][starting_column]
            for row in reversed(range(starting_row, ending_row))
        )
        starting_column += 1

    return res


if __name__ == "__main__":
    array = [
        [1, 2, 3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10, 9, 8, 7]
    ]
    print(spiralTraverse(array))

    array = [
        [1, 2, 3],
        [12, 13, 4],
        [11, 14, 5],
        [10, 15, 6],
        [9, 8, 7]
    ]
    print(spiralTraverse(array))
