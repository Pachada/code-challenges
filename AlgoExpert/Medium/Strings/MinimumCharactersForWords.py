"""
Minimum Characters For Words | AlgoExpert
Write a function that takes in an array of words and returns the smallest array of characters needed 
to form all of the words. The characters don't need to be in any particular order.

For example, the characters ["y", "r", "o", "u"] are needed to form the words ["your", "you", "or", "yo"].

Note: the input words won't contain any spaces; however, they might contain punctuation and/or special characters.

Sample Input
words = ["this", "that", "did", "deed", "them!", "a"]
Sample Output
["t", "t", "h", "i", "s", "a", "d", "d", "e", "e", "m", "!"]
// The characters could be ordered differently.
"""
from collections import Counter

# O(n * l) time where n is the number of words and l is the len of the longest word
# O(c) space where c is the number of unique characters across all words
def minimumCharactersForWords(words):
    char_count = {}
    for word in words:
        word_char_count = Counter(word)
        for character, count in word_char_count.items():
            current_count = char_count.get(character, 0)
            if not current_count or current_count < count:
                char_count[character] = count
    
    result = []
    for character, count in char_count.items():
        result.extend([character]*count)
    
    return result
            
                
words = ["this", "that", "did", "deed", "them!", "a"]
print(minimumCharactersForWords(words))