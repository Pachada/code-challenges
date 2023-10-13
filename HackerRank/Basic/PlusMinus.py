"""
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
Print the decimal value of each fraction on a new line with  places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, 
though answers with absolute error of up to  are acceptable.

Example
arr = [1,1,0,-1,-1]

There are  elements, two positive, two negative and one zero. Results are printed as:

0.400000
0.400000
0.200000
"""


def plusMinus(arr):
    distribution = {1: 0, -1: 0, 0: 0}
    for value in arr:
        if value == 0:
            distribution[0] += 1
        elif value > 0:
            distribution[1] += 1
        else:  # Negative 
            distribution[-1] += 1

    n = len(arr)
    for value in distribution.values():
        print("{:.6f}".format(value/n))
        
        

if __name__ == '__main__':
    arr = [1,1,0,-1,-1]
    plusMinus(arr)