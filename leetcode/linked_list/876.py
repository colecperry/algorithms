# 876. Middle of the Linked List

# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

# Ex. 1

# 1 -> 2 -> 3 -> 4 -> 5

# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.

# Ex. 2

# 1 -> 2 -> 3 -> 4 -> 5 -> 6

# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        # While fast -> Stops fast pointer on even # lists
        # While fast.next -> Stops fast pointer on odd # lists
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
# Why we need "while fast and fast.next":
#
# Example 1: Odd length [1→2→3]
# Start: slow=1, fast=1
# Loop 1: slow=2, fast=3
# Check: fast=3 (exists ✓), fast.next=None (✗) → STOP
# Without fast.next check: we'd try fast.next.next = None.next → CRASH
#
# Example 2: Even length [1→2→3→4]
# Start: slow=1, fast=1
# Loop 1: slow=2, fast=3
# Loop 2: slow=3, fast=None
# Check: fast=None (✗) → STOP
# Without fast check: we'd try fast.next = None.next → CRASH
#
# TL;DR: "fast" protects even-length, "fast.next" protects odd-length

# Manually creating Example 1: [1,2,3,4,5], [1,2,3,4,5,6]
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
head2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, (ListNode(6, None)))))))
solution = Solution()
sol1 = solution.middleNode(head1)
print(sol1.val)
sol2 = solution.middleNode(head2)
print(sol2.val)
