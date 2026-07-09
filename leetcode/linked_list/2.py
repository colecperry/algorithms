# 2. Add Two Numbers

# Topics - Linked List, Math, Recursion

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# How to solve optimal (without storing integers):
# Iterate through both LL's
# Add both of the nodes together (from ex. 1 -> 2 + 5 = 7) including the carry (if there is one)
    # If adding two numbers results in a value >= 10, we have to add a carry -> (from ex 1. -> 6 + 4 = 10): store 0 carry 1
    # Edge case 1: If we get to a place where there is no node, assume it is zero -> In below example on last iteration, 0 + 3
        # ex.
        # 5 -> 6 -> 4
        # 2 -> 4 -> 3 -> 3

        # 7 -> 0 -> 8 -> 3

    # Edge case 2: If we get to a place where there is no nodes at all, but there is a carry: On last iteration, 8 + 7 = 5, but we have to carry the one 
        # ex.
        # 1 -> 8
        # 2 -> 7

        # 3 -> 5 -> 1



# Example 1: 
# 2 -> 4 -> 3
# 5 -> 6 -> 4

# 7 -> 0 -> 8
#
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807. -> Add the reverse of each LL and return as a LL reversed

# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3: 
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode() # Create a dummy node
        current = dummy # Create a pointer

        carry = 0 # Create carry variable that holds the carry for adding two nodes together
        while l1 or l2 or carry: # Loop while either l1 or l2 has have a digit or our carry is > 0 (edge case for edge case 2)
            val_1 = l1.val if l1 else 0 # Extract the value of l1 if there is one else set to zero
            val_2 = l2.val if l2 else 0

            val = val_1 + val_2 + carry # Compute the new digit
            carry = val // 10 # Update carry's value if val > 10:  15 // 10 = 1
            val = val % 10 # Get only the one's place for the value: 15 % 10 = 5, 5 % 10 = 5
            current.next = ListNode(val) # Add new node with val to the LL result

            current = current.next # Move pointer for LL result
            l1 = l1.next if l1 else None # Move list 1 pointer if we are on a node, if we reach end of list set to None
            l2 = l2.next if l2 else None

            return dummy.next # Return the LL we just created


    # How to solve with extra memory (storing integers)
    def addTwoNumbers2(self, l1, l2):
        def linked_list_to_int(node): # Helper function converts linked list to integer
            num, tens = 0, 1 # Keep track of integer and tens place
            while node:
                num += node.val * tens # Add the current integer to the (value of the node * current tens value)
                tens *= 10 # Increase tens by a factor of 10 each iteration
                node = node.next # Move node to next pointer
            return num

        # Convert linked lists to integers
        integer_res = linked_list_to_int(l1) + linked_list_to_int(l2) # Call the functions for each list and add them to get the int

        # Edge case: If the sum is 0, return a single-node list [0]
        if integer_res == 0:
            return ListNode(0)

        # Convert integer back to reversed linked list
        dummy = ListNode(0) # Create a dummy node
        current = dummy # Create a pointer
        while integer_res > 0: # Loo
            digit = integer_res % 10  # Get last digit of the integer
            current.next = ListNode(digit) # Create a node with that digit and add it to the LL
            current = current.next # Move the pointer
            integer_res = integer_res // 10 # Update the integer res by using floor division for next iteration -> 807 // 10 = 80 

        return dummy.next

# Helper function to print linked list (for verification)
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next

# Manually creating Example 1: [1,4,3,2,5,2]
head1 = ListNode(2, ListNode(4, ListNode(3, None)))
head2 = ListNode(5, ListNode(6, ListNode(4, None)))
solution = Solution()
new_head = solution.addTwoNumbers2(head1, head2)
print_linked_list(new_head) # Expected Output: 7 -> 0 -> 8

head1 = ListNode(0, None)
head2 = ListNode(0, None)
new_head = solution.addTwoNumbers2(head1, head2)
print_linked_list(new_head) # Expected Output: 0

head1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, None)))))))
head2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
new_head = solution.addTwoNumbers2(head1, head2)
print_linked_list(new_head) # Expected Output: 8 -> 9 -> 9 -> 9 -> 0 -> 0 -> 0 -> 1


