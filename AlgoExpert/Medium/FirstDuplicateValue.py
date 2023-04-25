"""
First Duplicate Value | AlgoExpert
Given an array of integers between 1 and n, inclusive, where n is the length of the array, 
write a function that returns the first integer that appears more than once (when the array is read from left to right).

In other words, out of all the integers that might occur more than once in the input array, 
your function should return the one whose first duplicate value has the minimum index.

If no integer appears more than once, your function should return -1.

Note that you're allowed to mutate the input array.

Sample Input #1
array = [2, 1, 5, 2, 3, 3, 4]
Sample Output #1
2 // 2 is the first integer that appears more than once.
// 3 also appears more than once, but the second 3 appears after the second 2.
Sample Input #2
array = [2, 1, 5, 3, 3, 2, 4]
Sample Output #2
3 // 3 is the first integer that appears more than once.
// 2 also appears more than once, but the second 2 appears after the second 3.
"""

"""
# O(n) time | O(n) space
def firstDuplicateValue(array):
    seen = set() # n space 
    for value in array: # n time
        if value in seen:
            return value
        else:
            seen.add(value)
    
    return -1
"""

# O(n) time | O(1) space 
def firstDuplicateValue(array):
    """
    Given an array of integers between 1 and n, inclusive, where n is the length of the array
    Note that you're allowed to mutate the input array.
    Map each value to its corresponding idx, if the value has already been seen, return that numnber
    """
    for i in range(len(array)):
        idx = abs(array[i]) -1 
        if array[idx] < 0:
            return abs(array[i]) 
        else:
            array[idx] *= -1
    
    return -1

if __name__ == "__main__":
    array = [2, 1, 5, 2, 3, 3, 4]
    print(firstDuplicateValue(array))

                

