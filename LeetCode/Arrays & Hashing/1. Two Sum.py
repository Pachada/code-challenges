from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    prevMap = {}  # val : index

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i
    return

if __name__ == "__main__":
    nums = [3,2,4]
    target = 6
    print(twoSum(nums, target))
    nums = [2,7,11,15]
    target = 9
    print(twoSum(nums, target))
    nums = [3,3]
    target = 6
    print(twoSum(nums, target))