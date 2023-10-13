"""
Longest Peak | AlgoExpert
Write a function that takes in an array of integers and returns the length of the longest peak in the array.

A peak is defined as adjacent integers in the array that are strictly increasing until they reach a tip 
(the highest value in the peak), at which point they become strictly decreasing. 
At least three integers are required to form a peak.

For example, the integers 1, 4, 10, 2 form a peak, but the integers 4, 0, 10 don't 
and neither do the integers 1, 2, 2, 0. Similarly, the integers 1, 2, 3 don't form a peak 
because there aren't any strictly decreasing integers after the 3.

Sample Input
array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
Sample Output
6 // 0, 10, 6, 5, -1, -3
"""


from typing import List

# O(n) time | O(1) space
def longestPeak(array: List[int]):
    longest_peak = 0
    for i in range(1, len(array)-1):
        if array[i] > array[i-1] and array[i] > array[i+1]:
            peak_length = 3  # A peak is formed by at least 3 values
            #left
            for j in range(i-1, 0, -1):
                if array[j] <= array[j - 1]:
                    break
                peak_length += 1
            # rigth
            for k in range(i+1, len(array)-1):
                if array[k + 1] >= array[k]:
                    break
                peak_length += 1

            longest_peak = max(peak_length, longest_peak)

    return longest_peak


if __name__ == "__main__":
    array = [1, 1, 3, 2, 1]
    print(longestPeak(array))
    array2 = [5, 4, 3, 2, 1, 2, 10, 12, -3, 5, 6, 7, 10]
    print(longestPeak(array2))
