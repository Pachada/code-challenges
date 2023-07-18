"""
Palindrome Check | AlgoExpert
Write a function that takes in a non-empty string and that returns a boolean representing whether the string is a palindrome.

A palindrome is defined as a string that's written the same forward and backward. 
Note that single-character strings are palindromes.

Sample Input
string = "abcdcba"
Sample Output
true // it's written the same forward and backward

"""

# O(n/2) time | O(1) space
def isPalindrome(string: str) -> bool:
    left_idx, right_idx = 0, len(string)-1
    while left_idx < right_idx:
        if string[left_idx] != string[right_idx]:
            return False
        left_idx += 1
        right_idx -= 1
    
    return True


if __name__ == "__main__":
    string = "abcdcba"
    print(isPalindrome(string))