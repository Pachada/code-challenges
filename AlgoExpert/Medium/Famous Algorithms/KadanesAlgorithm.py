"""
Kadane's Algorithm | AlgoExpert
Write a function that takes in a non-empty array of integers and returns 
the maximum sum that can be obtained by summing up all of the integers in a 
non-empty subarray of the input array. A subarray must only contain adjacent numbers 
(numbers next to each other in the input array).

Sample Input
array = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
Sample Output
19 // [1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1]
"""

# O(n) time | O(1) space
def kadanesAlgorithm(array: list):
    """
    Calculates the maximum sum of a subarray within the given array using Kadane's algorithm.
    The algorithm iterates through the array and updates each element to be the maximum sum of a subarray ending at that position.
    It returns the maximum sum found.

    Args:
        array (List[int]): The input array of integers.

    Returns:
        int: The maximum sum of a subarray within the given array.
    """
    for i in range(1, len(array)):
        array[i] = max(array[i-1] + array[i], array[i])  # Update each element to be the maximum sum of a subarray ending at that position.

    return max(array)  # Return the maximum sum found within the array.



if __name__ == '__main__':
    array = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
    print(kadanesAlgorithm(array))