"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

"""

from typing import List
import math

# ------------------------- correct but O(N**2) complexity -----------------------------
def productExceptSelf(nums: List[int]) -> List[int]:
    result = []
    for i, _ in enumerate(nums):
        value = 1
        for j, num in enumerate(nums):
            if i == j:
                continue
            value *= num
        result.append(value)    
    
    return result


# ------------------------ O(N) time and O(1) Mermory solution --------------------------

def productExceptSelfBetter(nums: List[int]) -> List[int]:
    result = [1] * len(nums)
    
    prefix = 1
    for i in range(len(nums)):
        result[i] = prefix
        prefix *= nums[i]
    
    postfix = 1
    for i in range(len(nums)-1,-1,-1):
        result[i] *= postfix
        postfix *= nums[i]
    
    return result
        
        
        


if __name__ == '__main__':
    nums = [1,2,3,4]
    print(productExceptSelfBetter(nums))
    nums = [-1,1,0,-3,3]
    print(productExceptSelfBetter(nums))