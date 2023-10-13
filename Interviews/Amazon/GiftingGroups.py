"""
You have a matrix where each row corresponds to a subscriber, and each column corresponds to a book. 
If a subscriber is gifted a book by another subscriber, the matrix has a 1 in the corresponding cell; 
otherwise, it has a 0. Find the number of distinct groups of subscribers that can be formed where a group 
consists of a subscriber and all subscribers who have gifted a book to them.

Input:

M: A matrix of size n x n, where M[i][j] is 1 if subscriber i is gifted a book by subscriber j and 0 otherwise.
Output:

Return an integer representing the number of distinct groups.
"""


# O(n**2) time | O(n) space
def find_groups(related: list[str]):
    n = len(related)
    seen = set()
    
    def dfs(i):
        if i in seen:
            return
        seen.add(i)
        
        for j in range(n):
            if related[i][j] == "1":
                dfs(j)
    
    group_count = 0
    for i in range(n):
        if i in seen:
            continue
        
        dfs(i)
        group_count += 1
    
    return group_count


if __name__ == "__main__":
    related = ["1100", "1110", "0110", "0001"]
    print(find_groups(related))
        