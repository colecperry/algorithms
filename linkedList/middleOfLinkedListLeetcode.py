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
class Solution(object):
    def middleNode(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
