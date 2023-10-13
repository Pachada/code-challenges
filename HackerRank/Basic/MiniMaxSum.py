"""
Given five positive integers, find the minimum and maximum values that can be calculated by 
summing exactly four of the five integers. Then print the respective minimum and maximum values as a 
single line of two space-separated long integers.

Example

arr = [1,3,5,7,9]

The minimum sum is 1+3+5+7 = 16 and the maximum sum is  3+5+7+9=24. The function prints

16 24
"""


# O(n) time | O(1) space
def miniMaxSum(arr):
    min_arr_value = min(arr)
    max_arr_value = max(arr)
    arr_sum = sum(arr)
    print(arr_sum - max_arr_value, arr_sum - min_arr_value)


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
