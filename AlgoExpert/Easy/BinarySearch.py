"""
Binary Search | AlgoExpert
Write a function that takes in a sorted array of integers as well as a target integer. 
The function should use the Binary Search algorithm to determine if the target integer 
is contained in the array and should return its index if it is, otherwise -1.

Sample Input
array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target = 33
Sample Output
3
"""

from typing import List

# O(Log(n)) time | O(1) space 
def binarySearch(array: List[int], target: int):
    left_pointer, rigth_pointer = 0, len(array)-1
    while left_pointer <= rigth_pointer:
        middle_pointer = (left_pointer+rigth_pointer)//2
        value = array[middle_pointer]
        if value == target:
            return middle_pointer
        elif target > value:
            left_pointer = middle_pointer + 1
        elif target < value:
            rigth_pointer = middle_pointer - 1

    return -1


if __name__ == "__main__":
    array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
    target = 33
    print(binarySearch(array, target))
