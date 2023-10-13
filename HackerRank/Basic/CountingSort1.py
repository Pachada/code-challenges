"""
Given a list of integers, count and return the number of times each value appears as an array of integers.

arr = [1,1,3,2,1]

i	arr[i]	result
0	1	[0, 1, 0, 0]
1	1	[0, 2, 0, 0]
2	3	[0, 2, 0, 1]
3	2	[0, 2, 1, 1]
4	1	[0, 3, 1, 1]

The frequency array is [0,3,1,1]. These values can be used to create the sorted array as well: sorted = [1,1,1,2,3].

For this exercise, always return a frequency array with 100 elements. 
The example above shows only the first 4 elements, the remainder being zeros.
"""


#O(n) time | O(1) space 
def countingSort(arr):
    arr_frequency = [0]*100
    for value in arr:
        arr_frequency[value] += 1
    
    return arr_frequency