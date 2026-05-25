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
        - TC: O(n + m) -> iterate through both lists once
        - SC: O(1) -> no new nodes created, just relinking existing ones
        """
        dummy = ListNode(-1) # dummy head so we don't have to handle first node as special case
        curr = dummy # pointer to build the merged list

        while list1 and list2:
            if list1.val < list2.val: # list1 has smaller value
                curr.next = list1 # attach list1 node
                list1 = list1.next # advance list1
            else: # list2 has smaller or equal value
                curr.next = list2 # attach list2 node
                list2 = list2.next # advance list2
            curr = curr.next # advance merged list pointer

        # attach remaining nodes from whichever list isn't exhausted
        if list1: # if nodes left in list 1
            curr.next = list1 # attach rest of nodes
        elif list2: # if nodes left in list 2
            curr.next = list2

        return dummy.next # dummy.next is the real head
    
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

test = Solution.mergeTwoLists(list1, list2)

print(test)