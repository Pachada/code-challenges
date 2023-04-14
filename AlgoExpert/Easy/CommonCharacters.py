"""
Common Characters | AlgoExpert
Write a function that takes in a non-empty list of non-empty strings and returns a 
list of characters that are common to all strings in the list, ignoring multiplicity.

Note that the strings are not guaranteed to only contain alphanumeric characters. 
The list you return can be in any order.

Sample Input
strings = ["abc", "bcd", "cbaccd"]
Sample Output
["b", "c"] // The characters could be ordered differently.

"""
def commonCharacters(strings):
    common = set(strings[0])
    
    for string in strings[1:]:
        common &= set(string)
        
    return list(common)
    
    
value = ["aa", "aa"]
print(commonCharacters(value))