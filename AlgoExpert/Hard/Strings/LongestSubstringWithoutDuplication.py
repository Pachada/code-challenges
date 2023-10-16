"""
Longest Substring Without Duplication | AlgoExpert
Write a function that takes in a string and returns its longest substring without duplicate characters.

You can assume that there will only be one longest substring without duplication.

Sample Input
string = "clementisacap"
Sample Output
"mentisac"
"""

# Sliding Windos 
# O(n) time | O()
def longestSubstringWithoutDuplication(string):
    char_idx_map = {}
    start_idx = 0
    max_len = 0
    longest = [0,1]
    for end_idx, char in enumerate(string):
        if char in char_idx_map:
            start_idx = max(start_idx, char_idx_map[char]+1)
        
        if end_idx - start_idx > max_len:
            max_len = end_idx - start_idx
            longest = [start_idx, end_idx+1]
        
        char_idx_map[char] = end_idx
    
    return string[longest[0]: longest[1]]
            
            
        
string = "clementisacap"
print(longestSubstringWithoutDuplication(string))