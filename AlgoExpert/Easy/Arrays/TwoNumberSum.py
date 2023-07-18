"""
Two Number Sum | AlgoExpert
Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. 
If any two numbers in the input array sum up to the target sum, the function should return them in an array, in any order. 
If no two numbers sum up to the target sum, the function should return an empty array.

Note that the target sum has to be obtained by summing two different integers in the array; 
you can't add a single integer to itself in order to obtain the target sum.

You can assume that there will be at most one pair of numbers summing up to the target sum.

Sample Input
array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10
Sample Output
[-1, 11] // the numbers could be in reverse order
"""

from typing import List

# ------------------------ Naive aproach, memory O(1), time O(n**2)------------------------------
def twoNumberSum_Naive(array: List[int], targetSum: int) -> List[int] | List:
    for i, value1 in enumerate(array):
        for j, value2 in enumerate(array):
            if i == j: continue
            if value1 + value2 == targetSum:
                return [value1, value2]
    
    return []

# ----------------------------- x + y = targetSum, find y, memory O(N), time O(N) ----------------------------------

def twoNumberSum_usingMath(array: List[int], targetSum: int) -> List[int] | List:
    numbers = set(array)
    for value in array:
        reminder = targetSum - value
        if reminder in numbers and reminder is not value:
            return [value, reminder]

    return []


if __name__ == "__main__":
    array1 = [3, 5, -4, 8, 11, 1, -1, 6]
    target1 = 10
    array2 = [-21, 301, 12, 4, 65, 56, 210, 356, 9, -47]
    target2 = 163
    print(twoNumberSum_Naive(array1, target1))
    print(twoNumberSum_Naive(array2, target2))
    
    print(twoNumberSum_usingMath(array1, target1))
    print(twoNumberSum_usingMath(array2, target2))