# Given the head of a singly linked list, reverse the list, and return the reversed list.
# Example 1:
    # Input: head = [1,2,3,4,5]
    # Output: [5,4,3,2,1]
# Example 2:
    # Input: head = [1,2]
    # Output: [2,1]
# Example 3:
    # Input: head = []
    # Output: []

class ListNode(object):
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = None

    def reverseList(self, head):
        current = self.head
        self.head = self.tail
        self.tail = current
        before = None
        after = current.next
        for _ in range(self.length):
            after = current.next
            current.next = before
            before = current
            current = after
        return head
    
    

