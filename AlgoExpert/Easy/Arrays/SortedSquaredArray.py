"""
Write a function that takes in a non-empty array of integers that are sorted in ascending order 
and returns a new array of the same length with the squares of the original integers also sorted in ascending order.

Sample Input
array = [1, 2, 3, 5, 6, 8, 9]
Sample Output
[1, 4, 9, 25, 36, 64, 81]

"""


from typing import List


# ----------------------------- memory O(N), time O(N log N) ------------------------------
def sortedSquaredArray_Python(array:List[int]):
    return sorted([x**2 for x in array]) # sorted function takes on Avg O(N log N)



# ----------------------------- memory O(N), time O(N) ------------------------------
def sortedSquaredArray(array:List[int]):
    i = 0
    j = len(array)-1
    result = []
    while i <= j:
        if abs(array[i]) > abs(array[j]):
            result.insert(0, array[i]**2)
            i += 1
        else:
            result.insert(0, array[j]**2)
            j -= 1
    
    return result
             



if __name__ == '__main__':
    array = [1, 2, 3, 5, 6, 8, 9]
    print(sortedSquaredArray(array))