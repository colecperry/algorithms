# 203. Remove Linked List Elements

# Topics: Linked List, Recursion

# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

# Ex. 1

# Original
    #      
    # 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6

# After
    # 1 -> 2 -> 3 -> 4 -> 5

# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]

# Example 2:
# Input: head = [], val = 1
# Output: []

# Example 3:
# Input: head = [7,7,7,7], val = 7
# Output: []

# How to Solve (Recursive):
    # 1. Think of each function call as making ONE decision: "keep or remove current node?"
    # 2. Base case: if head is None, return None (end of list)
    # 3. If current node should be removed: skip it, return cleaned rest
    # 4. If current node should be kept: connect it to cleaned rest, return it

    # KEY INSIGHT: We recursively call the function until we hit the base case, and as we unravel the recursive stack, we either
        # Keep the node (node.val != val) -> attach this current node to cleaned rest of the list and return it to the prev callstack
        # Skip the node (node.val == val) -> and return the cleaned list (not including this current node) to the prev callstack

        # We basically build the list by going deep into recursion and using the return values to build the LL from the bottom up

    # TIME COMPLEXITY: O(n) - visit each node exactly once
    # SPACE COMPLEXITY: O(n) - recursion stack depth equals list length
    #                          (in worst case, we make n recursive calls)


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElementsRecursive(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Base case: if we've reached the end, return None
        if not head:
            return None
        
        # Get the clean version of everything after this node
        cleanRest = self.removeElementsRecursive(head.next, val)
        
        # Now decide what to return to the prev callstack
        if head.val == val:  # Skip this node 
            return cleanRest  # Return the clean list (w/o this curr node)
        else:
            head.next = cleanRest  # Keep this node, attach it to clean rest
            return head # Return the head (cleaned list with head attached)
        
    # How to Solve (Iterative):
        # 1. First clean up the head: keep removing head nodes until you find a keeper
        # 2. Use two pointers: prev (last good node) and current (node being examined)
        # 3. When you find a bad node: bridge over it by connecting prev to current's next
        # 4. When you find a good node: advance both pointers forward
        
        # KEY INSIGHT: We "bridge over" bad nodes by updating the previous node's next 
        # pointer to skip the bad node entirely. The bad node becomes unreachable and 
        # gets garbage collected automatically - we don't need to manually clean its connections.
        
        # STEP-BY-STEP:
        # - Handle head case separately (could be multiple bad heads in a row)
        # - Maintain prev pointer to always point to last confirmed good node
        # - When removing: only advance current, leave prev pointing to same good node
        # - When keeping: advance both pointers together
        # - Garbage collector cleans up unreachable removed nodes
        
        # TIME COMPLEXITY: O(n) - visit each node exactly once
        # SPACE COMPLEXITY: O(1) - only use two pointers, no extra space needed
        
    def removeElementsIterative(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Step 1: Remove bad head nodes - keep moving head forward until we find a node worth keeping (or reach end)
        while head and head.val == val:
            head = head.next
        
        # Edge case: if entire list was removed
        if head is None:
            return None
        
        # Step 2: Remove bad nodes from the rest of the list -> start current from second node
        prev = head # keep prev pointer for removing
        current = head.next 
        
        while current:
            if current.val == val: # Remove this bad node by bridging over it
                prev.next = current.next # Connect prev to current's next node
                current = current.next # Move to examine the next node
                # no need to move prev forward because we removed that node
                
            else: # This is a good node - keep it and advance both pointers
                prev = current 
                current = current.next
        
        return head



ex1 = ListNode(1, (ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))))
ex2 = None
ex3 = ListNode(7,
                     ListNode(7,
                              ListNode(7,
                                       ListNode(7))))

ex4 = ListNode(1,
                     ListNode(6,
                              ListNode(2)))


sol = Solution()
print(sol.removeElementsRecursive(ex1, 6))
print(sol.removeElementsIterative(ex2, 1))
print(sol.removeElementsIterative(ex3, 7))

print(sol.removeElementsIterative(ex4, 6))

