
from typing import List


def containsDuplicate(nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


nums = [1,1,1,3,3,4,3,2,4,2]

print(containsDuplicate(nums))