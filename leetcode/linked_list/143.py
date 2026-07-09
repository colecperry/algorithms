# 143. Reorder List

# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

# Ex. 1
# Input: head = [1,2,3,4]
# Output: [1,4,2,3]

# Ex. 2
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]

# How to Solve (with extra space):
    # Convert the linked list to an array
    # Start two pointers - one at the end of the array at one at the beginning
    # Add the element at the first pointer, move it right, add the element at the second pointer, move it left until they meet with a while loop
    # Loop through the array and rebuild the linked list

# How to Solve (without extra space):
    # Break the list in half (slow and fast pointers)
    # Reverse the second linked list (so we can start adding these nodes one at a time for the final LL)
    # Rebuild the lists in correct order
        # Create pointers at the beginning of each list
        # Within a while loop:
            # Save node's after each pointer (so we can move them forward after we break the link)
            # Connect first node in first list to first node in second list
            # Connect first node in second list to second node in first list
            # Move pointers forward

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reorderList(self, head):
        slow, fast = head, head.next
        while fast and fast.next: # Get the middle node
            slow = slow.next
            fast = fast.next.next
        current = slow.next # Get beginning node of second half list
        slow.next = None # Break the linked list

        # Reverse second list
        pre = None
        while current:
            after = current.next # Save the node after current
            current.next = pre # Reverse the link
            pre = current # Move pre pointer forward
            current = after # Move current pointer forward (using saved node)
        
        # Rebuild the lists
        first = head # Two pointers (one for each list)
        second = pre
        while second: # We know second could be shorter
            temp1, temp2 = first.next, second.next # Save the node after pointers in both lists
            first.next = second # Connect node in first list to node in second list
            second.next = temp1 # Connect node in second list to next node in first list
            first, second = temp1, temp2 # Move pointers over
        
        return head
    

# Helper function to print linked list (for verification)
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next


# Manually creating Example 1: [1,2,3,4]
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
solution = Solution()
solution.reorderList(head1)
print_linked_list(head1)  # Expected Output: 1 -> 4 -> 2 -> 3

# Manually creating Example 2: [1,2,3,4,5]
head2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
solution.reorderList(head2)
print_linked_list(head2)  # Expected Output: 1 -> 5 -> 2 -> 4 -> 3