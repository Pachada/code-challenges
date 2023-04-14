"""
Generate Document | AlgoExpert
You're given a string of available characters and a string representing a document that you need to generate. 
Write a function that determines if you can generate the document using the available characters. 
If you can generate the document, your function should return true; otherwise, it should return false.

You're only able to generate the document if the frequency of unique characters in the characters 
string is greater than or equal to the frequency of unique characters in the document string. 
For example, if you're given characters = "abcabc" and document = "aabbccc" 
you cannot generate the document because you're missing one c.

The document that you need to create may contain any characters, 
including special characters, capital letters, numbers, and spaces.

Note: you can always generate the empty string ("").

Sample Input
characters = "Bste!hetsi ogEAxpelrt x "
document = "AlgoExpert is the Best!"
Sample Output
true

"""

from collections import defaultdict

# O(n) time
def count_chars(s):
    freq = defaultdict(int)
    for char in s:
        freq[char] += 1
    return dict(freq)

# O(n + m) time | O(n) space where n is the length of the chracters and m is the length of the document
def generateDocument(characters: str, document: str):
    characters_counts = count_chars(characters) # O(n)
    for char in document: #O(m)
        if character := characters_counts.get(char):
            characters_counts[char] -= 1
        else:
            return False
    
    return True

from collections import Counter
def generateDocument_oneLiner(characters: str, document: str):
    return Counter(document)-Counter(characters) == {}


if __name__ == "__main__":
    characters = "Bste!hetsi ogEAxpelrt x "
    document = "AlgoExpert is the Best!"
    print(generateDocument(characters, document))
        
