# 19. Remove Nth Node From End of List

# Topics: Linked List, Two Pointer

# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Example 1:
# Input: head = [1,2,3,4,5], n = 2 -> n = 2 means the second node from the end of the list
# Output: [1,2,3,5]

# Example 2:
# Input: head = [1], n = 1
# Output: []

# Example 3:
# Input: head = [1,2], n = 1
# Output: [1]

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        if head.next == None:
            return None
        fast = head
        slow = head
        for _ in range(n):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = fast.next

        return head

# Helper function to print linked list (for verification)
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next

# Manually creating Example 1: [1,2,3,4,5]
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
solution = Solution()
solution.removeNthFromEnd(head1, 2)
print_linked_list(head1)  # Expected Output: 1 -> 2 -> 3 -> 5

head2 = ListNode(1)
solution.removeNthFromEnd(head2, 1)
print_linked_list(head2)   # Expected Output: []

head3 = ListNode(1, (ListNode(2, None)))
solution.removeNthFromEnd(head3, 1)
print_linked_list(head3)   # Expected Output: 1