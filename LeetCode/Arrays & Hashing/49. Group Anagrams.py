"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""


from collections import defaultdict
from typing import List

# -------------------------- MY SOLUTION ------------------------
# IT WORKS BUT IS REALLY SLOW

def isAnagram(s: str, t: str) -> bool:
        return sorted(s)==sorted(t)

def groupAnagrams(strs: List[str]) -> List[List[str]]:
        anagrams_lists = []
        anagrams_checked = set()
        for i,value in enumerate(strs):
            if value in anagrams_checked:
                continue
            anagram_list = [value]
            for j, value_ in enumerate(strs):
                if i == j:
                    continue
                if isAnagram(value, value_):
                    anagram_list.append(value_)
                    anagrams_checked.add(value_)
            anagrams_lists.append(anagram_list)
        return anagrams_lists


# -------------------------------- Best solution -------------------------------

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    res = defaultdict(list)
    
    for s in strs:
        sorted_s = "".join(sorted(s))
        
        res[sorted_s].append(s)
    
    return list(res.values())
                    
                

if __name__ == '__main__':
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(groupAnagrams(strs))
    strs = ["",""]
    print(groupAnagrams(strs))
    
    