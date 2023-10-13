"""
Max Subset Sum No Adjacent
Write a function that takes in an array of positive integers and returns the maximum sum of non-adjacent elements in the array.

If the input array is empty, the function should return 0.

Sample Input
array = [75, 105, 120, 75, 90, 135]
Sample Output
330 // 75 + 120 + 135

"""

"""# O(n) time | O(1) space 
def maxSubsetSumNoAdjacent(array):
    current_max, previous_max = 0, 0
    for value in array:
        previous_max, current_max = current_max, max(current_max, max(current_max, previous_max + value))
    
    return current_max
"""
# O(n) time | O(n) space 
def maxSubsetSumNoAdjacent(array):
    if not array:
        return 0
    max_sums = []
    for i, value in enumerate(array):
        # Base cases
        if i == 0:
            max_sums.append(value)
        elif i == 1:
            max_sums.append(max(array[0], value))
        else:
            # We applied the formula:
            # max_sums[i] = max(max_sums[i-1], max_sums[i-2] + value)
            max_sums.append(max(max_sums[i-1], (max_sums[i-2] + value)))
    
    return max_sums[-1]

if __name__ == "__main__":
    array = [75, 105, 120, 75, 90, 135]
    print(maxSubsetSumNoAdjacent(array))