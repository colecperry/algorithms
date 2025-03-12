# 148. Sort List

# Given the head of a linked list, return the list after sorting it in ascending order.

# Example 1:    
# Input: head = [4,2,1,3]
# Output: [1,2,3,4]

# Example 2:
# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]

# Example 3: 
# Input: head = []
# Output: []

# Can you sort the linked list in O(n log n) time complexity and O(1) memory

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def sortList(self, head):
        if head == None or head.next == None: # Base case -> If 1 or 0 nodes in the list
            return head
        # Split the list into two halves
        left = head # Set left to the head
        right = self.getMid(head) # Get middle node (middle left if even # of nodes)
        temp = right.next # Create temp node one to the right
        right.next = None # Seperate the two LL's
        right = temp # Set the right pointer to the beginning of the right list

        # Recursive calls - keeps splitting the two sides until the base cases are reached
        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left, right)
    
    def getMid(self, head): # Returns the middle node
        slow, fast = head, head.next # Two pointer
        while fast and fast.next: # While both pointers are in bounds
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge(self, list1, list2): # Merge is called with 
        tail = dummy = ListNode() # Create placeholder node at the beginning of the merged list & point to tail
        while list1 and list2: # While both lists are not empty
            if list1.val < list2.val: # If the value of list 1 is less than the value of list 2
                tail.next = list1 # Insert list1 node
                list1 = list1.next # Shift the pointer oveer
            else: #If the value of list 1 is greater than the value of list 2
                tail.next = list2 # Insert list2 node
                list2 = list2.next # Shift the pointer over
            tail = tail.next # Move the pointer over in the new LL so we can add at the end of the LL
        if list1: # If there are left over nodes in list1 (can only be left over nodes in one list)
            tail.next = list1 # Connect the rest of list1 to the tail
        if list2: # If there are left over nodes in list2
            tail.next = list2 # Connect the rest of list2 to the tail
        
        return dummy.next # Return the actual start of the merge list
    
    def print_list(self, head):
        while head:
            print(head.val)
            head = head.next




# Create LL manually
head_node = ListNode(4) # Create class
head_node.next = ListNode(2)
head_node.next.next = ListNode(1)
head_node.next.next.next = ListNode(3)

sorted_head = head_node.sortList(head_node) # Sort the list and store it in variable sorted_head
head_node.print_list(sorted_head) # Print the list





