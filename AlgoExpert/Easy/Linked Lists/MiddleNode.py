"""
Middle Node | AlgoExpert
You're given a Linked List with at least one node. Write a function that returns the middle node of the Linked List. 
If there are two middle nodes (i.e. an even length list), your function should return the second of these nodes.

Each LinkedList node has an integer value as well as a next node pointing to the next node in the list or to None / null if it's the tail of the list.

Sample Input
linkedList = 2 -> 7 -> 3 -> 5
Sample Output
3 -> 5 // The middle could be 7 or 3,
// we return the second middle node

"""


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) time | O(1) space
def middleNode(linkedList:LinkedList) -> LinkedList:
    move_one_pointer = linkedList
    move_two_pointer = linkedList
    while move_two_pointer and move_two_pointer.next:
        move_one_pointer = move_one_pointer.next
        move_two_pointer = move_two_pointer.next.next
    
    return move_one_pointer



if __name__ == '__main__':
    linkedList = LinkedList(2)
    linkedList.next = LinkedList(7)
    linkedList.next.next = LinkedList(3)
    linkedList.next.next.next = LinkedList(5)
    print(middleNode(linkedList).value)
