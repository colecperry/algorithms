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

# Merge sort notes:
    # Divide - keep splitting the list in half until you can't split anymore (1 ele lists)
    # Conquer - merge pairs of small sorted lists into larger sorted lists, repeat until you have one fully sorted list

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head):
        # BASE CASE: If list is empty or has 1 node, it's already sorted
        if not head or not head.next:
            return head
        
        # DIVIDE PHASE: Split the list into two halves
        mid = self.getMid(head)  # Find the middle node
        right = mid.next         # Right half starts after mid
        mid.next = None          # Cut the list in two (left ends at mid)
        
        # CONQUER PHASE: Each call returns a SORTED version of that half
        # Trust that each call returns sorted version of list we gave it
        left = self.sortList(head)   # Returns sorted left half 
        right = self.sortList(right) # Returns sorted right half 
        
        # COMBINE PHASE: call merge() on the two sorted lists
        return self.merge(left, right) # return it's val
    
    def getMid(self, head):
        """Find middle node using slow/fast pointers"""
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next       # Moves 1 step
            fast = fast.next.next  # Moves 2 steps
        return slow  # When fast reaches end, slow is at middle
    
    def merge(self, list1, list2):
        """Merge two ALREADY SORTED lists into one sorted list"""
        dummy = tail = ListNode()  # dummy is the anchor, tail ptr moves
        
        # Compare and take smaller node each time
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1  # Attach list1's node
                list1 = list1.next # Move list1 forward
            else:
                tail.next = list2  # Attach list2's node
                list2 = list2.next # Move list2 forward
            tail = tail.next       # Move tail forward
        
        # Attach any remaining nodes (only one list can have leftovers)
        tail.next = list1 or list2 # without "if"/== before "or", "or" returns one of the original values
        
        return dummy.next  # Skip dummy, return actual merged list
    
    #         4 -> 2 -> 1 -> 3
    #                |
    #                v
    #         1 -> 2 -> 3 -> 4
    
    def print_list(self, head):
        while head:
            print(head.val)
            head = head.next

# Create LL manually
head_node = ListNode(4) # Create class
head_node.next = ListNode(2)
head_node.next.next = ListNode(1)
head_node.next.next.next = ListNode(3)

sol = Solution()
sorted_head = sol.sortList(head_node) # Sort the list and store it in variable sorted_head
head_node.print_list(sorted_head) # Print the list





