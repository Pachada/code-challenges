"""
Insertion Sort | AlgoExpert
Write a function that takes in an array of integers and returns a sorted version of that array. 
Use the Insertion Sort algorithm to sort the array.

If you're unfamiliar with Insertion Sort, we recommend watching the Conceptual Overview section 
of this question's video explanation before starting to code.

Sample Input
array = [8, 5, 2, 9, 5, 6, 3]
Sample Output
[2, 3, 5, 5, 6, 8, 9]
"""


from typing import List

# O(n**2) time | O(1) space
def insertionSort(array: List[int])-> List[int]:
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1

    return array


if __name__ == '__main__':
    array = [8, 5, 2, 9, 5, 6, 3]
    print(insertionSort(array))
