"""

Given an array of integers, where all elements but one occur twice, find the unique element.

Example:  a = [1,2,3,4,3,2,1]

The unique element is 4.

"""


# O(n) time | O(n) space
def lonelyinteger(a):
    a_distribution = {}
    for value in a:
        if value in a_distribution:
            a_distribution[value] += 1
        else:
            a_distribution[value] = 1

    return min(a_distribution, key=a_distribution.get)
