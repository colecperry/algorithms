# This method should be able to detect if there is a cycle or loop present in the linked list

# How to Solve - Utilize Floyd's cycle finding algorithm (Tortise and Hare)
    # Create two pointers, slow and fast, both initially pointed at the head
    # Traverse the list, slow moving one step at a time, and fast moving two
    # If there is a loop in the list, the fast pointer will eventually meet the slow pointer and return True
    # If the fast pointer reaches the end of the list or encounters a None value, no loop in list, return False


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def has_loop(self):
        slow = self.head # Create two variables, slow and fast and point them to the head
        fast = self.head
        while fast and fast.next: # Check if there is a node, and then check if there's a next node 
            slow = slow.next # Advance the slow variable to the next node
            fast = fast.next.next # Advance the fast variable two nodes forward
            if slow == fast: # If "while fast and fast.next" keep returning True and does not exit, it has a loop
                return True # Return True
        return False # If the loop exits, return False

    
my_linked_list_1 = LinkedList(1)
my_linked_list_1.append(2)
my_linked_list_1.append(3)
my_linked_list_1.append(4)
my_linked_list_1.tail.next = my_linked_list_1.head
print(my_linked_list_1.has_loop() ) # Returns True




my_linked_list_2 = LinkedList(1)
my_linked_list_2.append(2)
my_linked_list_2.append(3)
my_linked_list_2.append(4)
print(my_linked_list_2.has_loop() ) # Returns False



"""
    EXPECTED OUTPUT:
    ----------------
    True
    False
    
"""

# LEETCODE SOLUTION

# Given head, the head of a linked list, determine if the linked list has a cycle in it. There is a cycle in a 
# linked list if there is some node in the list that can be reached again by continuously following the next 
# pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. 
# Note that pos is not passed as a parameter. Return true if there is a cycle in the linked list. Otherwise, 
# return false.

# Example 1: 
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

# Example 2: 
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

# Example 3: 
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# class Solution(object):
#     def hasCycle(self, head):
#         slow = head
#         fast = head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#             if slow == fast:
#                 return True
#         return False