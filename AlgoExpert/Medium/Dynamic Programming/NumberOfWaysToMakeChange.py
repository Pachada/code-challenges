"""
Number Of Ways To Make Change
Given an array of distinct positive integers representing coin denominations and a single non-negative integer n 
representing a target amount of money, 
write a function that returns the number of ways to make change for that target amount using the given coin denominations.

Note that an unlimited amount of coins is at your disposal.

Sample Input
n = 6
denoms = [1, 5]
Sample Output
2 // 1x1 + 1x5 and 6x1
"""

# if denom <= amount: ways[amount] += ways[amount-denom]

# O(dn) where d is the number of denominations | O(n) space where n is the target amount of money
def numberOfWaysToMakeChange(n, denoms):
    ways = [1] + [0] * n # n space
    for denom in denoms: # d * n time 
        for i in range(denom, len(ways)):
            if denom <= i:
                ways[i] += ways[i-denom]
    
    return ways[n]



if __name__ == '__main__':
    n = 10
    denoms = [1,5,10,25]
    print(numberOfWaysToMakeChange(n, denoms))        
