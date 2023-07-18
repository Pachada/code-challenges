"""
Move Element To End | AlgoExpert
You're given an array of integers and an integer. Write a function that moves all instances of that integer 
in the array to the end of the array and returns the array.

The function should perform this in place (i.e., it should mutate the input array) and doesn't need to maintain the order of the other integers.

Sample Input
array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2
Sample Output
[1, 3, 4, 2, 2, 2, 2, 2] // the numbers 1, 3, and 4 could be ordered differently
"""


from typing import List


# O(n) time | O(1) complexity
def moveElementToEnd(array:List[int], toMove:int) -> List[int]:
    left_pointer = 0
    rigth_pointer = len(array)-1
    while left_pointer < rigth_pointer:
        while array[left_pointer] != toMove and left_pointer < rigth_pointer:
            left_pointer += 1
        while array[rigth_pointer] == toMove and rigth_pointer > left_pointer:
            rigth_pointer -= 1
        
        array[left_pointer], array[rigth_pointer] = array[rigth_pointer], array[left_pointer]
    
    return array


if __name__ == "__main__":
    array = [2, 1, 2, 2, 2, 3, 4, 2]
    toMove = 2
    print(moveElementToEnd(array, toMove))

            
