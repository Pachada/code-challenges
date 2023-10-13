"""
First Non-Repeating Character | AlgoExpert
Write a function that takes in a string of lowercase English-alphabet letters and returns the index of the string's first non-repeating character.

The first non-repeating character is the first character in a string that occurs only once.

If the input string doesn't have any non-repeating characters, your function should return -1.

Sample Input
string = "abcdcaf"
Sample Output
1 // The first non-repeating character is "b" and is found at index 1.

"""


# O(n) time where n is the length of the string | O(1) space for there are max 26 letters in the english alphabet
from collections import Counter
def firstNonRepeatingCharacter(string:str):
    character_count = Counter(string)
    return next((idx for idx, char in enumerate(string) if character_count[char] == 1), -1)


if __name__ == "__main__":
    string = "abcdcaf"
    print(firstNonRepeatingCharacter(string))
