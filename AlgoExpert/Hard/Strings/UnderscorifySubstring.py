"""
Underscorify Substring | AlgoExpert
Write a function that takes in two strings: a main string and a potential substring of the main string. 
The function should return a version of the main string with every instance of the substring in it wrapped between underscores.

If two or more instances of the substring in the main string overlap each other or sit side by side, 
the underscores relevant to these substrings should only appear on the far left of the leftmost 
substring and on the far right of the rightmost substring. 
If the main string doesn't contain the other string at all, the function should return the main string intact.

Sample Input
string = "testthis is a testtest to see if testestest it works"
substring = "test"
Sample Output
"_test_this is a _testtest_ to see if _testestest_ it works"
"""
# O(n * m) time where n is the len if the main_string and m is the len of the substring
# O(n) space 
def underscorify_substring(main_string: str, substring):
    positions = []
    # Step 1: Find Occurrences
    start_idx = 0
    while start_idx < len(main_string):
        current_pos = main_string.find(substring, start_idx)
        if current_pos != -1:
            positions.append([current_pos, current_pos + len(substring)])
            start_idx = current_pos + 1
        else:
            break
    
    # Step 2: Merge Ranges
    merge_ranges = []
    for start, end in positions:
        if not merge_ranges or start > merge_ranges[-1][1]:
            merge_ranges.append([start, end])
        else:
            merge_ranges[-1] = [merge_ranges[-1][0], max(merge_ranges[-1][1], end)]
    

    # Step 3: Insert Underscores
    last_pos = 0
    result = []
    for start, end in merge_ranges:
        result.append(main_string[last_pos:start])
        result.append("_")
        result.append(main_string[start:end])
        result.append("_")
        last_pos = end
    
    result.append(main_string[last_pos:])
    
    return "".join(result)
        
    

# Sample Input
main_string = "testthis is a testtest to see if testestest it works"
substring = "test"
print(underscorify_substring(main_string, substring))  # Output should match the sample output
