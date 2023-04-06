"""
Write a function that takes in an array of integers and returns a sorted version of that array. 
Use the Selection Sort algorithm to sort the array.


Sample Input
array = [8, 5, 2, 9, 5, 6, 3]
Sample Output
[2, 3, 5, 5, 6, 8, 9]
"""


from typing import List

def selectionSort(array:List[int]) -> List[int]:
    i = 0
    while i < len(array):
        smallest_number_idx = i
        for j in range(i+1, len(array)):
            if array[j] < array[smallest_number_idx]:
                smallest_number_idx = j
        
        array[i], array[smallest_number_idx] = array[smallest_number_idx], array[i]
        i += 1
    
    return array


if __name__ == '__main__':
    array = [8, 5, 2, 9, 5, 6, 3]
    print(selectionSort(array))
        
                
