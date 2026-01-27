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
        dummy = ListNode(0, head)  # Handles edge case of removing head
        slow, fast = dummy, dummy
        
        # Move fast n+1 ahead (so slow lands one BEFORE node to remove)
        for _ in range(n + 1):
            fast = fast.next
        
        # Move both until fast hits end
        # This code gets skipped if n==len(linked list)
        while fast:
            slow = slow.next
            fast = fast.next
        
        # Skip the nth node
        slow.next = slow.next.next
        
        return dummy.next
        
# Edge case where n == len(linked list)
# Fast gets to None, then second loop is skipped completely
# Then we point the slow (pointed at the dummy node) to the second node in the list

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
print_linked_list(head3)   # Expected Output: []

