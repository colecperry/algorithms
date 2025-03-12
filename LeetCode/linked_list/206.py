# 206. Reverse Linked List

# Given the head of a singly linked list, reverse the list, and return the reversed list.

# How to solve
    # Use two pointer approach - Use a pre and current pointer: current to the head and set pre to None (one node before the head)
    # Iterate through the linked list
        # Save the current node's next pointer to a variable (because when we reverse it we will break the .next link from current, we need a way to move current ptr forward)
        # Point current's .next backwards to pre to reverse the LL
        # Move pre to current's place
        # Move current to the variable we saved before
    # Return the head (pre ends on the last node which is the new head)


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

    def reverseListIterative(self, head):
        pre = None # Two pointers: Point pre at None (before the first node in the list)
        current = self.head # Point current to the head

        while current: # Loop until current becomes None
            after = current.next # Create a variable to save current's next node (so we can move it forward since we break the link by pointing it backwards)
            current.next = pre # Point the .next backwards
            pre = current # Move pre forward
            current = after # Move current forward

        return pre # Return pre because it ends on the last node (current was set to None)
    
    

