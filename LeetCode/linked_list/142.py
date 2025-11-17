# LC 142 - Linked List Cycle II

# Topics: Hash Table, Linked List, Two Pointers

# Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

# Do not modify the linked list.

# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the second node.

# Example 2:
# Input: head = [1,2], pos = 0
# Output: tail connects to node index 0
# Explanation: There is a cycle in the linked list, where tail connects to the first node.

# Example 3:
# Input: head = [1], pos = -1
# Output: no cycle
# Explanation: There is no cycle in the linked list.

class ListNode(object):
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Solution:
    """
    TC: O(n) - two passes through list
    SC: O(1) - only two pointers
    """
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = head # create slow and fast ptrs
        
        # Phase 1: Detect if cycle exists
        while fast and fast.next:
            slow = slow.next  # Move 1 step
            fast = fast.next.next  # Move 2 steps
            
            if slow == fast:  # They met - cycle exists!
                break
        else:
            return None  # No cycle found
        
        # Phase 2: Find where cycle starts (the magic!)
        # Math fact: distance from head to cycle start = distance from meeting point to cycle start
        
        slow = head  # Reset slow to beginning, fast stays at meeting point
        
        while slow != fast: # Move both at same speed
            slow = slow.next  # Walking from head toward cycle start
            fast = fast.next  # Walking from meeting point toward cycle start
        
        return slow # They will meet exactly at cycle start

nodes = [ListNode(val) for val in [3, 2, 0, -4]]
for i in range(3): nodes[i].next = nodes[i+1]
nodes[3].next = nodes[1]  # Create cycle
head = nodes[0]

sol = Solution()
print(sol.detectCycle(head)) # pos = 1