"""
Group Anagrams | AlgoExpert
Write a function that takes in an array of strings and groups anagrams together.

Anagrams are strings made up of exactly the same letters, where order doesn't matter. 
For example, "cinema" and "iceman" are anagrams; similarly, "foo" and "ofo" are anagrams.

Your function should return a list of anagram groups in no particular order.

Sample Input
words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
Sample Output
[["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"], ["foo"]]
"""

from collections import defaultdict

# O(w nlogn) time, w is the len of strings and n is the len of the longest string
# O(wn) space 
def groupAnagrams(words):
    group_of_anagrams = defaultdict(list)
    for word in words:
        sorted_word = "".join(sorted(word))
        group_of_anagrams[sorted_word].append(word)
    
    return list(group_of_anagrams.values())


if __name__ == "__main__":
    words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
    print(groupAnagrams(words))
