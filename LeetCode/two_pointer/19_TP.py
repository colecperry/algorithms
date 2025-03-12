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

# How to solve: (Optimal)
    # Use a left pointer (first node) and a right pointer ("n" spaces right of the left pointer)
    # Iterate moving both pointers forward one until right pointer gets to the end of the list
        # Once the right pointer hits null, we know that the left pointer will be on the node we want to delete (n nodes from the end)



class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head) # Create dummy node with it's next set to head
        left = dummy # Create left pointer starting at the dummy node
        right = head  # Set right pointer to the head

        for _ in range(n): # Move right pointer to starting spot
            right = right.next

        while right: # Move left and right pointers to correct spot
            left = left.next
            right = right.next
        left.next = left.next.next # Delete the node

        return dummy.next
        
        

# Helper function to print linked list (for verification)
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next

# Manually creating Example 1: [1,2,3,4]
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
