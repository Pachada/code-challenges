"""
Smallest Subarray with a Given Sum
Problem Statement
Find the length of the smallest contiguous subarray whose sum is at least S.

Approach
Initialize window_start = 0, min_length = \text{float}('inf'), and window_sum = 0.
Loop through the array, adding each element to window_sum.
When window_sum is greater than or equal to S, update min_length and slide the window.
"""

# O(n) time | O(1) space
def smallest_subarray_with_given_sum(s, arr):
    window_start = 0
    min_length = float('inf')
    window_sum = 0
    
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        
        while window_sum >= s:
            min_length = min(min_length, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1
    
    return min_length if min_length != float('inf') else 0



print(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2]))  # Output: 2
print(smallest_subarray_with_given_sum(4, [1, 4, 4]))           # Output: 1
