"""
Find the longest substring that do not contain a prohibited word

review = "GoodProductButScrapAfterWash" 
prohibitedWords = ["crap", "odpro"] 
"
"""



def find_longest_substring(review: str, prohibited_words: list[str]):
    review = review.lower()
    prohibited_words = [word.lower() for word in prohibited_words]
    
    longest_substring = ""
    max_len = 0
    
    start_idx, end_idx = 0, 0
    
    while end_idx <= len(review):
        current_substring = review[start_idx: end_idx]
        
        if any(word in current_substring for word in prohibited_words):
            start_idx += 1
        else:
            if end_idx - start_idx > max_len:
                max_len = end_idx - start_idx
                longest_substring = current_substring
            
            end_idx += 1
    
    print(longest_substring)
    return max_len


review = "GoodProductButScrapAfterWash" 
prohibited_words = ["crap", "odpro"] 

print(find_longest_substring(review, prohibited_words))