"""
Semordnilap | AlgoExpert
Write a function that takes in a list of unique strings and returns a list of semordnilap pairs.

A semordnilap pair is defined as a set of different strings where the reverse of one word is 
the same as the forward version of the other. 
For example the words "diaper" and "repaid" are a semordnilap pair, as are the words "palindromes" and "semordnilap".

The order of the returned pairs and the order of the strings within each pair does not matter.

Sample Input
words = ["diaper", "abc", "test", "cba", "repaid"]
Sample Output
[["diaper", "repaid"], ["abc", "cba"]]

"""

from typing import List


def semordnilap(words: List[str]):
    result = []
    seen = set()
    for word in words:
        seen.add(word)
        reversed_word = word[::-1]
        if reversed_word in seen and reversed_word != word:
            result.append([word, reversed_word])

    return result


if __name__ == "__main__":
    words = ["diaper", "abc", "test", "cba", "repaid"]
    print(semordnilap(words))
