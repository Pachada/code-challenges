"""
Zero Sum Subarray | AlgoExpert
You're given a list of integers nums. Write a function that returns a boolean representing whether 
there exists a zero-sum subarray of nums.

A zero-sum subarray is any subarray where all of the values add up to zero. 
A subarray is any contiguous section of the array. 
For the purposes of this problem, a subarray can be as small as one element and as long as the original array.

Sample Input
nums = [-5, -5, 2, 3, -2]
Sample Output
True // The subarray [-5, 2, 3] has a sum of 0

"""

# O(n) time | O(n) space
def zeroSumSubarray(nums):
    seen_values = {0}
    current_sum = 0
    for value in nums:
        current_sum += value
        if current_sum in seen_values:
            return True
        
        seen_values.add(current_sum)
    
    return False


if __name__ == "__main__":
    nums = [-5, -5, 2, 3, -2]
    print(zeroSumSubarray(nums))
            
