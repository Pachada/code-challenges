"""
Find Three Largest Numbers | AlgoExpert
Write a function that takes in an array of at least three integers and, without sorting the input array, 
returns a sorted array of the three largest integers in the input array.

The function should return duplicate integers if necessary; for example, it should return [10, 10, 12] 
for an input array of [10, 5, 9, 10, 12].

Sample Input
array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
Sample Output
[18, 141, 541]
"""


# O(n) time | O(1) space
from typing import List


def findThreeLargestNumbers(array: List[int]):
    largest_num, second_largest, third_largest = [float("-inf")] * 3
    for value in array:
        if value > largest_num:
            largest_num, second_largest, third_largest = value, largest_num, second_largest
        elif value > second_largest:
            second_largest, third_largest = value, second_largest
        elif value > third_largest:
            third_largest = value

    return [third_largest, second_largest, largest_num]


if __name__ == "__main__":
    array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
    print(findThreeLargestNumbers(array))
