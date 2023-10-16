"""
1. Maximum Subarray of Size K
Problem: Given an array of integers and a number K, 
find the maximum sum of a contiguous subarray of size K.

Algorithm:

Initialize variables window_start = 0 and max_sum = 0.
Loop through the array, keeping track of the sum of elements within the window.
Once the window size reaches K, update max_sum if the current window sum is greater.
Slide the window to the right by removing the leftmost element and adding the next one.

"""

# O(n) time | O(1) space
def max_subarray_of_size_k(k, arr):
    window_start = 0
    max_sum = float('-inf')
    window_sum = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        
        if window_end >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]
            window_start += 1

    return max_sum


print(max_subarray_of_size_k(3, [2, 1, 5, 1, 3, 2]))  # Output: 9
print(max_subarray_of_size_k(2, [2, 3, 4, 1, 5]))      # Output: 7
