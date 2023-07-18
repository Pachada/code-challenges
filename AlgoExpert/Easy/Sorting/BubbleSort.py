"""
Bubble Sort | AlgoExpert
Write a function that takes in an array of integers and returns a sorted version of that array. 
Use the Bubble Sort algorithm to sort the array.


Sample Input
array = [8, 5, 2, 9, 5, 6, 3]
Sample Output
[2, 3, 5, 5, 6, 8, 9]
"""

from typing import List

# O(n**2) time | O(1) space
def bubbleSort(array: List[int]):
    swap_made = True
    counter = 0
    while swap_made:
        swap_made = False
        for i in range(len(array) - 1 - counter):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swap_made = True
        counter += 1
    return array


if __name__ == "__main__":
    array = [8, 5, 2, 9, 5, 6, 3]
    print(bubbleSort(array))
