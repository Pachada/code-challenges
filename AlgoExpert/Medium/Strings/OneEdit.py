"""
One Edit | AlgoExpert
You're given two strings stringOne and stringTwo. Write a function that determines if these two strings 
can be made equal using only one edit.

There are 3 possible edits:

Replace: One character in one string is swapped for a different character.
Add: One character is added at any index in one string.
Remove: One character is removed at any index in one string.
Note that both strings will contain at least one character. If the strings are the same, your function should return true.

Sample Input
stringOne = "hello"
stringTwo = "hollo"
Sample Output
True // A single replace at index 1 of either string can make the strings equal
"""

# O(n) time | O(1) space
def oneEdit(stringOne, stringTwo):
    string_one_len = len(stringOne)
    string_two_len = len(stringTwo)
    diff_in_len = abs(string_one_len - string_two_len)
    if diff_in_len > 1:
        return False
    
    edit_made = False
    index_one = 0
    index_two = 0
    
    while index_one < string_one_len and index_two < string_two_len:
        if stringOne[index_one] != stringTwo[index_two]:
            if edit_made:
                return False
            edit_made = True
            if string_one_len > string_two_len:
                index_one += 1
            elif string_two_len > string_one_len:
                index_two += 1
            else:
                index_one += 1
                index_two += 1
        else:
            index_one += 1
            index_two += 1
    
    return True
            
    

stringOne = "ab"
stringTwo = "b"
print(oneEdit(stringOne, stringTwo))