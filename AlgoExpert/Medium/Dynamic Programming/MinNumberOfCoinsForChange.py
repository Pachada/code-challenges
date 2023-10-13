"""
Min Number Of Coins For Change
Given an array of positive integers representing coin denominations and a 
single non-negative integer n representing a target amount of money, 
write a function that returns the smallest number of coins needed to make change 
for (to sum up to) that target amount using the given coin denominations.

Note that you have access to an unlimited amount of coins. In other words, 
if the denominations are [1, 5, 10], you have access to an unlimited amount of 1s, 5s, and 10s.

If it's impossible to make change for the target amount, return -1.

Sample Input
n = 7
denoms = [1, 5, 10]
Sample Output
3 // 2x1 + 1x5
"""

# if denom <= amount: 
#   diff = ways[amount - denom]
#   ways[amount] = min(ways[amount], (1 + ways[diff]))

# O(dn) Time where d is the number of denoms and n is the target amount | O(n) space
def minNumberOfCoinsForChange(n, denoms):
    ways = [0] + [float("inf")]* n # O(n) space
    for denom in denoms: # d * n
        for i in range(denom, len(ways)):
            diff = i - denom
            ways[i] = min(ways[i], (1 + ways[diff]))
    
    return -1 if ways[n] == float("inf") else ways[n]


if __name__ == "__main__":
    n = 3
    denoms = [2, 1]
    print(minNumberOfCoinsForChange(n, denoms))
