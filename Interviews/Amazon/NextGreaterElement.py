"""
Given an array, print the Next Greater Element (NGE) for every element. 
The Next greater Element for an element x is the first greater element on the right side of x in array. 
Elements for which no greater element exist, consider next greater element as -1.

Array  [4, 5, 2, 25]

    Element       NGE
          4      -->   5
          5      -->   25
          2      -->   25
          25     -->   -1
"""

# O(n) time | O(n) space
def print_NGE(array: list[int]):
    stack = []
    for num in array:
        while stack and stack[-1] < num:
            print(f"{stack.pop()} --> {num}")
        
        stack.append(num)
    
    while stack:
        print(f"{stack.pop()} --> -1")
        
if __name__ == "__main__":
    array = [4, 5, 2, 25]
    print_NGE(array)