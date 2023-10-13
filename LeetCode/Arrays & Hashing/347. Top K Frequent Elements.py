"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
Constraints:

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
"""


from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    nums_checked = set()
    nums_count = {}
    for num in nums:
        if num in nums_checked:
            continue
        nums_count[num] = nums.count(num)
        nums_checked.add(num)

    sorted_nums = dict(sorted(nums_count.items(), key=lambda x: x[1], reverse=True))
    return list(sorted_nums.keys())[:k]

if __name__ == '__main__':
    nums = [4,1,-1,2,-1,2,3]
    k = 2
    print(topKFrequent(nums, k))
