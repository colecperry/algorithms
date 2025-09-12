# 21. Merge Two Sorted Lists

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Ex. 1

# 1 -> 2 -> 4

# 1 -> 3 -> 4

# 1 -> 1 -> 2 -> 3 -> 4 -> 4

# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:
# Input: list1 = [], list2 = []
# Output: []

# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]

# How to Solve (Recursive)
    # Base Cases:
    # Both lists are empty -> Return empty list (None)
    # One list is empty -> Return the other list

    # Recursive Cases:
    # We recursively call the function until we hit the base case
    # We pick list1 or list2 as our winner based on which value is smaller
    # Then we connect it to the merged result of the remaining problem
    # Return the list to the prev callstack (used to attach the node's .next to)

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Base cases
        if not list1 and not list2: # Both lists are empty 
            return None # Return an empty linked list (None)
        
        if not list1: # If only one list is empty
            return list2 # Return the other list

        if not list2:
            return list1
        
        # Recursive cases
        if list1.val <= list2.val: # If list1's node is smaller
            list1.next = self.mergeTwoLists(list1.next, list2) # Connect list's .next to the merged result of the remaining problem
            return list1 # Return the merged list back to the prev callstack
        else: # If list2's node is smaller
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
        


sol = Solution()

list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4) # [1, 2, 4]

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4) # [1, 3, 4]

print(sol.mergeTwoLists(list1, list2)) # [1,1,2,3,4,4]

list3 = None
list4 = None
print(sol.mergeTwoLists(list3, list4)) # []

list5 = None
list6 = ListNode(0)
print(sol.mergeTwoLists(list5, list6)) # [0]



