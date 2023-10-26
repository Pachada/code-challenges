"""
Levenshtein Distance | AlgoExpert
Write a function that takes in two strings and returns the minimum number of edit 
operations that need to be performed on the first string to obtain the second string.

There are three edit operations: insertion of a character, deletion of a character, and substitution of a character for another.

Sample Input
str1 = "abc"
str2 = "yabd"
Sample Output
2 // insert "y"; substitute "c" for "d"
"""

# O(nm) time where n and m are the len of str1 and str2 | O(nm) space 
def levenshtein_distance(str1, str2):
    # Initialize a 2D DP table with dimensions (len(str1) + 1) x (len(str2) + 1)
    dp = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
    
    # Initialize the first column, representing the number of deletions needed
    # to transform substrings of str1 into an empty string
    for i in range(len(str1) + 1):
        dp[i][0] = i
        
    # Initialize the first row, representing the number of deletions needed
    # to transform substrings of str2 into an empty string
    for j in range(len(str2) + 1):
        dp[0][j] = j
    
    # Fill in the rest of the table by considering the three possible edit operations:
    # insertion, deletion, and substitution
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            # If the current characters are equal, no new operation is needed.
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # Take the minimum of the three preceding values and add 1
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                
    # The last cell in the table contains the answer: the minimum number of edit operations
    return dp[-1][-1]


if __name__ == "__main__":
    str1 = "abc"
    str2 = "yabd"
    print(levenshtein_distance(str1, str2))

