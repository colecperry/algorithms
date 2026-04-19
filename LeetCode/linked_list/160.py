from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    Problem: Find the node at which two singly linked lists intersect. Return None if none.

    Example:
        List A:      4 → 1 ↘
                              8 → 4 → 5
        List B:  5 → 6 → 1 ↗

        Output: node(8)

    Steps:
    1. Traverse list A, storing each node in a set
    2. Traverse list B — return the first node already in the set
    3. Return None if no intersection found
    """
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:  # LC 160
        """
        - TC: O(n + m) - one pass through each list
        - SC: O(n) - stores all nodes of list A
        """
        seen = set() # Store nodes of list A
        while headA:
            seen.add(headA) # Add all nodes of list A to the set
            headA = headA.next
        while headB:
            if headB in seen: # Check if any node of list B is in the set (i.e., in list A)
                return headB # Return the first intersecting node
            headB = headB.next
        return None # No intersection found

    # Follow-up: O(1) space two-pointer solution
    # Both pointers travel len_A + len_B total, so they sync up at the intersection.
    # If no intersection, both reach None simultaneously.
    #
    # def getIntersectionNode(self, headA, headB):
    #     a, b = headA, headB
    #     while a != b:
    #         a = a.next if a else headB
    #         b = b.next if b else headA
    #     return a


sol = Solution()
shared = ListNode(8, ListNode(4, ListNode(5)))
headA = ListNode(4, ListNode(1, shared))
headB = ListNode(5, ListNode(6, ListNode(1, shared)))
result = sol.getIntersectionNode(headA, headB)
print("Intersection node:", result.val if result else None)  # 8
