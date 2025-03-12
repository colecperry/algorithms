# 876. Middle of the Linked List

# How to solve (without using the length attribute)
    # Use the two pointer approach
    # One pointer (slow) moves one node at a time,
    # The other pointer (fast) moves two nodes at a time
    # When the fast pointer reaches the end of the list, the slow pointer should be in the middle
    # For an even number of nodes, return the second half of the middle

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
        

    def find_middle_node(self):
        slow = self.head # Set 2 pointers, slow and fast to the head
        fast = self.head
        # We must include "while fast" because if fast gets pointed outside the list, it will become None.
        # We cannot access "None.next" so we just check the node itself
        while fast and fast.next: # Check if there is a node, and then check if there's a next node 
            slow = slow.next # Advance the slow variable to the next node
            fast = fast.next.next # Advance the fast variable two nodes forward
        return slow





my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

print(my_linked_list.find_middle_node().value)



"""
    EXPECTED OUTPUT:
    ----------------
    3
    
"""

# LEETCODE SOLUTION

# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.
    # Note - Leetcode has test files that create the linked list for you. In the input they are showing you an
    # example as an array in the input, but the linked list is not really an array, it's just an example. You 
    # only pass in the first node (the head) into the function and are able to use the .val and .next attributes
    # in the ListNode constrcutor they commented out

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.

# Example 2:
# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

# class ListNode(object):
#     def init(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution(object):
#     def middleNode(self, head):
#         slow = head
#         fast = head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#         return slow