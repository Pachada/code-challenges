"""
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix  is shown below:

1 2 3
4 5 6
9 8 9  
The left-to-right diagonal =  1+5+9=15. The right to left diagonal = 3+5+9=17 . 
Their absolute difference is |15-17| = 2.
"""


# O(n) time | O(1) space
def diagonalDifference(arr):
    left_sum, right_sum = 0,0
    j = len(arr)-1
    for i in range(len(arr)):
        left_sum += arr[i][i]
        right_sum += arr[i][j]
        j -= 1
    
    return abs(left_sum - right_sum)