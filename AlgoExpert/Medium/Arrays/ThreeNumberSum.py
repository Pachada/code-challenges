"""
Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. 
The function should find all triplets in the array that sum up to the target sum and return a two-dimensional array of all these triplets. 
The numbers in each triplet should be ordered in ascending order, and the triplets themselves should be ordered in ascending order 
with respect to the numbers they hold.

If no three numbers sum up to the target sum, the function should return an empty array.

Sample Input
array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0
Sample Output
[[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]

"""

from typing import List

# ---------------------- memory O(N), time O(N**3) -------------------------


def threeNumberSum_threeLoops(array: List[int], targetSum: int):
    result = []
    checked = set()
    for i, value in enumerate(array):
        for j, value1 in enumerate(array):
            if i == j:
                continue
            for k, value2 in enumerate(array):
                if k in [i, j]:
                    continue
                if value + value1 + value2 == targetSum:
                    values_for_target_sum = tuple(
                        sorted([value, value1, value2]))
                    if values_for_target_sum in checked:
                        continue
                    result.append(list(values_for_target_sum))
                    checked.add(values_for_target_sum)

    return sorted(result)


# ---------------------- memory O(N), time O(N**2) -------------------------

def threeNumberSum_twoLoops_hash(array: List[int], targetSum: int):
    result = []
    checked = set()
    values = set(array)
    for i, value in enumerate(array):
        for j, value1 in enumerate(array):
            if i == j:
                continue
            reminder = targetSum - value - value1
            if reminder in values and reminder not in (value, value1):
                three_number_sum = tuple(sorted([value, value1, reminder]))
                if three_number_sum in checked:
                    continue
                checked.add(three_number_sum)
                result.append(list(three_number_sum))

    return sorted(result)

# ---------------------- memory O(N), time O(N**2) -------------------------


def threeNumberSum_twoPointers(array: List[int], targetSum: int):
    array.sort()  # O(n log n)
    result = []  # memory O(N)
    for i, value in enumerate(array):
        left_pointer = i+1
        rigth_pointer = len(array) - 1
        while rigth_pointer > left_pointer:
            cumulative_sum = value + array[left_pointer] + array[rigth_pointer]
            if cumulative_sum == targetSum:
                result.append([value, array[left_pointer], array[rigth_pointer]])
                # We move the two pointers
                left_pointer += 1
                rigth_pointer -= 1
            elif cumulative_sum < targetSum:
                # We move the left_pointer to the rigth because the number is guaranteed to be higher
                left_pointer += 1
            elif cumulative_sum > targetSum:
                # We move the right_pointer to the left because the number is guaranteed to be lower
                rigth_pointer -= 1

    return result


if __name__ == '__main__':
    array = [12, 3, 1, 2, -6, 5, -8, 6]
    targetSum = 0
    print(threeNumberSum_threeLoops(array, targetSum))
    print(threeNumberSum_twoLoops_hash(array, targetSum))
    print(threeNumberSum_twoPointers(array, targetSum))
