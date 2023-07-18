"""
Monotonic Array | AlgoExpert
Write a function that takes in an array of integers and returns a boolean representing whether the array is monotonic.

An array is said to be monotonic if its elements, from left to right, are entirely non-increasing or entirely non-decreasing.

Non-increasing elements aren't necessarily exclusively decreasing; they simply don't increase.
Similarly, non-decreasing elements aren't necessarily exclusively increasing; they simply don't decrease.

Note that empty arrays and arrays of one element are monotonic.

Sample Input
array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
Sample Output
true
"""


from typing import List


# O(n) time | O(1) space
def isMonotonic(array:List[int]) -> bool:
    if len(array) < 2: # Note that empty arrays and arrays of one element are monotonic.
        return True

    increasing = None
    decreasing = None
    for i in range(1, len(array)): # O(n)
        if array[i] < array[i-1]:
            decreasing = True
        elif array[i] > array[i-1]:
            increasing = True

        if increasing and decreasing:
            return False

    return True
        
if __name__ == "__main__":
    array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
    print(isMonotonic(array))