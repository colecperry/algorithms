# 92 - Reverse Linked List II

# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

# How to solve (High level): Reverse LL between L and R, and then reconnect L and R to the head and tail nodes

# Phase 1:
# Create a dummy node that points at the head (helps with the edge case where L is the first node in the list, if L is the first node in the list and we need to return the head, it will have moved, so the dummy node will always point at the correct head)
# Set pre pointer to the dummy node, and a current pointer to the head
# Iterate pre and curr until the current node reaches the left node (equal to L - 1)

# Phase 2:
# Set prev pointer to None (so we can set current to none on first iteration)
# Now iterate until we have reversed the inner list (L - R + 1) times
    # Save current's next pointer (so we can move it forward)
    # Reverse pointer (set curr.next to prev)
    # Move pointers forward (prev to curr and curr to saved pointer)

# Phase 3: Reconnect the inner reversed list to the node's before and after L and R
    # Point left node's next at pointer after R
    # Point left node's Prev pointer (leftPrev) to the R node
    # Return dummy.next


# Example 1: 
# 1 -> 2 -> 3 -> 4 -> 5

# 1 -> 4 -> 3 -> 2 -> 5

# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]

# Example 2:
# Input: head = [5], left = 1, right = 1
# Output: [5]

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
        def reverseBetween(self, head, left, right):
            dummy = ListNode(0, head) # Create dummy ptr
            leftPrev, curr = dummy, head # Create pointers
            for _ in range(left - 1): # Iterate until left
                leftPrev, curr = curr, curr.next # Move ptrs
            
            prev = None # Start prev pointer at none
            for _ in range(right - left + 1):
                after = curr.next # Save pointer after curr
                curr.next = prev # Reverse pointer
                prev, curr = curr, after # Move ptrs forward
            
            leftPrev.next.next = curr # Point left node to node after R
            leftPrev.next = prev # point left node's prev to the R node

            return dummy.next
        
        # Helper function to print linked list (for verification)
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next

my_solution = Solution()
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
head2 = ListNode(5, None)
new_head_1 = my_solution.reverseBetween(head1, 2, 4)
new_head_2 = my_solution.reverseBetween(head2, 1, 1)

print_linked_list(new_head_1)
print_linked_list(new_head_2)

