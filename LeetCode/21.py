# 21. Merge Two Sorted Lists

# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list.
# The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:
# Input: list1 = [], list2 = []
# Output: []

# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]

class ListNode(object):
    def init(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(-1) # Create a dummy node with the value of -1
        current = dummy # Assign to a variable called current for the pointer to iterate through out list

        while list1 and list2: # While there is still another "next" value in both lists
            if list1.val <= list2.val: # Compare the value of the current loop on each linked list
                current.next = list1 # Connect the dummy variables to the node in list1 if it is smaller
                list1 = list1.next # Take the node from the old list 1, delete it, and reassign the node to the new list
            else:
                current.next = list2 # If the value of the second list is greater, assign the dummy variable ".next" to the first node in list2
                list2 = list2.next # Take the node from the old list 2, delete it, and reassign the node to the new list
            current = current.next # Stepping current along through the new list of nodes 
        if list1: # If list1 still exists, assign the .next 
            current.next = list1
        elif list2:
            current.next = list2
        return dummy.next
    
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

test = Solution.mergeTwoLists(list1, list2)

print(test)