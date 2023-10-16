"""
Reverse Words In String | AlgoExpert
Write a function that takes in a string of words separated by one or more whitespaces 
and returns a string that has these words in reverse order. 
For example, given the string "tim is great", your function should return "great is tim".

For this problem, a word can contain special characters, punctuation, and numbers. 
The words in the string will be separated by one or more whitespaces, and the reversed string 
must contain the same whitespaces as the original string. 
For example, given the string "whitespaces    4" you would be expected to return "4    whitespaces".

Note that you're not allowed to to use any built-in split or reverse methods/functions. 
However, you are allowed to use a built-in join method/function.

Also note that the input string isn't guaranteed to always contain words.

Sample Input
string = "AlgoExpert is the best!"
Sample Output
"best! the is AlgoExpert"
"""


# O(n) time | O(n) space
def reverseWordsInString(string):
    chars = list(string)
    
    def reverse(start, end):
        while start < end:
            chars[start], chars[end] = chars[end], chars[start]
            start += 1
            end -= 1
    
    reverse(0, len(chars)-1)
    
    start_idx = 0
    while start_idx < len(chars):
        if chars[start_idx] == " ":
            start_idx += 1
            continue
        
        end_idx = start_idx + 1
        while end_idx < len(chars) and chars[end_idx] != " ":
            end_idx += 1
        
        reverse(start_idx, end_idx - 1)
        start_idx = end_idx
    
    return "".join(chars)
            

     
string = "AlgoExpert is the best!"
print(reverseWordsInString(string))
