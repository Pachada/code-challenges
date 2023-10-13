"""
The median of a list of numbers is essentially its middle element after sorting. The same number of
elements occur after it as before. Given a list of numbers with an odd number of elements, find the median?
Example
ar = [5,3,1,2,4]
The sorted array arr = [1,2,3,4,5] . The middle element and the median is 3.

if n is odd: median(x) = (n+1)//2

if n is even: median(x)  = (x[n/2] + c[(n/2)+1])//2

"""

def findMedian(arr):  # sourcery skip: assign-if-exp
    arr.sort()
    n = len(arr)
    if n % 2 == 0:  # even
        median_pos = (arr[n/2] + arr[(n/2)+1])//2
    else:
        median_pos = (n+1)//2

    return arr[median_pos-1]
