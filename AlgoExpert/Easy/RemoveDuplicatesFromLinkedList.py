"""
Remove Duplicates From Linked List
You're given the head of a Singly Linked List whose nodes are in sorted order with respect to their values. 
Write a function that returns a modified version of the Linked List that doesn't contain any nodes with duplicate values. 
The Linked List should be modified in place (i.e., you shouldn't create a brand new list), 
and the modified Linked List should still have its nodes sorted with respect to their values.

Each LinkedList node has an integer value as well as a next node pointing to the next node
in the list or to None / null if it's the tail of the list.

Sample Input
linkedList = 1 -> 1 -> 3 -> 4 -> 4 -> 4 -> 5 -> 6 -> 6 // the head node with value 1
Sample Output
1 -> 3 -> 4 -> 5 -> 6 // the head node with value 1
"""


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next:LinkedList = None
    
    def addMany(self, values):
            current = self
            while current.next is not None:
                current = current.next
            for value in values:
                current.next = LinkedList(value)
                current = current.next
            return self
    
    def __repr__(self) -> str:
        values = []
        current_node = self
        while current_node is not None: #O(n)
            values.append(f"{current_node.value}")
            if current_node.next:
                values.append(" -> ")
            current_node = current_node.next
        
        return "".join(values) #O(n)

# O(n) time | O(1) space
def removeDuplicatesFromLinkedList(linkedList:LinkedList):
    current_node = linkedList
    while current_node.next is not None:
        if current_node.value == current_node.next.value:
            current_node.next = current_node.next.next
            continue
        current_node = current_node.next
    
    return linkedList
    

if __name__ == "__main__":
    linked_list = LinkedList(1).addMany([1, 3, 4, 4, 4, 5, 6, 6])
    print(linked_list)
    print(removeDuplicatesFromLinkedList(linked_list))
    
    

            
        
