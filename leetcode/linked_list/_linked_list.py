"""
=================================================================
LINKED LIST COMPLETE GUIDE
=================================================================

WHAT IS A LINKED LIST?
----------------------
A linked list is a linear data structure where elements (nodes) are connected via pointers
rather than stored in contiguous memory. Each node contains data and a reference to the
next node.

Structure:
- Each node has: value (data) + next pointer
- Head points to first node
- Last node points to None
- Sequential access only (no random access)

Example Singly Linked List:
    head → [1|●] → [2|●] → [3|●] → None

    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val      # Data
            self.next = next    # Pointer to next node

Types:
- Singly Linked: One pointer (next) per node
- Doubly Linked: Two pointers (prev, next) per node
- Circular: Last node points back to head

When to use Linked Lists:
- Frequent insertions/deletions at beginning: O(1)
- Unknown or dynamic size
- Don't need random access
- Implementing stacks, queues, hash table chaining

When NOT to use Linked Lists:
- Need random access by index: O(n) vs array's O(1)
- Memory overhead concerns (pointers take space)
- Cache performance matters (non-contiguous memory)
- Need frequent access to middle elements

Common linked list problem types:
- Reversal and reordering
- Cycle detection and removal
- Merging and splitting
- In-place modifications
- Fast/slow pointer techniques
- Partitioning and rearranging

LINKED LIST CORE TEMPLATES
===========================
"""

from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ================================================================
# TRAVERSAL TEMPLATE
# ================================================================
def traverse_template(head):
    """
    Basic linked list traversal

    TC: O(n) - visit each node once
    SC: O(1) - only one pointer

    WHEN TO USE:
    - Need to visit every node
    - Search for value
    - Count nodes
    - Print list
    """
    current = head

    while current:
        # Process current node
        print(current.val)
        current = current.next

# ================================================================
# DUMMY HEAD TECHNIQUE
# ================================================================
def dummy_head_template(head):
    """
    Dummy head technique to simplify edge cases

    TC: Same as without dummy (usually O(n))
    SC: O(1) - one extra node

    WHEN TO USE:
    - Modifying or deleting head node
    - Building new list
    - Merging lists
    - Any operation where head might change

    KEY INSIGHT:
    - Create dummy node before head
    - Perform all operations normally
    - Return dummy.next (actual head)
    - Eliminates special cases for empty list or head deletion
    """
    dummy = ListNode(0)  # Placeholder node
    dummy.next = head
    current = dummy

    # Perform operations
    while current.next:
        # Can safely access/modify current.next
        current = current.next

    return dummy.next  # Return actual head

def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]:  # LC 203
    """
    Application: Remove all nodes with value val. Uses look-ahead traversal —
    curr sits one behind the target so it can skip with curr.next = curr.next.next.
    Dummy head handles the case where head itself needs removal.

    Example:
        Input: head = [1,2,6,3,4,5,6], val = 6
        Output: [1,2,3,4,5]

    - TC: O(n) - single pass
    - SC: O(1)
    """
    dummy = ListNode(0, head)
    curr = dummy

    while curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next  # Skip the node
        else:
            curr = curr.next

    return dummy.next

# Example trace (removeElements, val=6):
# dummy → 1 → 2 → 6 → 3 → 4 → 5 → 6
#
# curr=dummy: curr.next.val=1, advance → curr=1
# curr=1:     curr.next.val=2, advance → curr=2
# curr=2:     curr.next.val=6, skip → curr.next=3
# curr=2:     curr.next.val=3, advance → curr=3
# curr=3:     curr.next.val=4, advance → curr=4
# curr=4:     curr.next.val=5, advance → curr=5
# curr=5:     curr.next.val=6, skip → curr.next=None
# curr.next is None — stop
#
# Output: [1,2,3,4,5]

"""
COMPLEXITY QUICK REFERENCE
==========================

Linked List Operations:
Operation       | Time    | Space | Notes
----------------|---------|-------|-------------------------
Access by index | O(n)    | O(1)  | Must traverse from head
Prepend         | O(1)    | O(1)  | Just update head
Append          | O(n)    | O(1)  | Traverse to end (O(1) with tail pointer)
Insert at index | O(n)    | O(1)  | Traverse to index
Delete by index | O(n)    | O(1)  | Traverse to index
Search          | O(n)    | O(1)  | Linear scan
Reverse         | O(n)    | O(1)  | One pass, in-place


====================
LINKED LIST PATTERNS
====================
"""

"""
================================================================
PATTERN 1: REVERSAL
PATTERN EXPLANATION: Reverse the direction of next pointers using three pointers: save next before breaking the link, point current backward, advance all three. For sublist reversal, walk to the node just before the start position, then repeatedly pull the next node to the front of the reversed section.

Applications: Reverse entire list, reverse between positions m and n, palindrome check,
reverse in k-groups.
================================================================
"""

class ReversalPattern:
    """
    Problem: Given head of singly linked list, reverse the list and return reversed head.

    Example:
        Input:  [1,2,3,4,5]
        Output: [5,4,3,2,1]

    Steps (Full Reversal - LC 206):
    1. Initialize prev=None, current=head
    2. While current exists:
       a. Save next: next_node = current.next
       b. Reverse link: current.next = prev
       c. Advance prev: prev = current
       d. Advance current: current = next_node
    3. Return prev (new head)
    """
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:  # LC 206
        """
        - TC: O(n) - visit each node exactly once
        - SC: O(1) - only three pointer variables
        """
        prev = None
        current = head

        while current:
            next_node = current.next   # Save next before breaking link
            current.next = prev        # Reverse link
            prev = current             # Advance prev
            current = next_node        # Advance current

        return prev  # New head
    
    # Example trace (reverseList):
    # Original: 1 → 2 → 3 → 4 → 5
    #
    # prev=None, curr=1: save 2, reverse 1→None, prev=1, curr=2
    # prev=1,    curr=2: save 3, reverse 2→1,    prev=2, curr=3
    # prev=2,    curr=3: save 4, reverse 3→2,    prev=3, curr=4
    # prev=3,    curr=4: save 5, reverse 4→3,    prev=4, curr=5
    # prev=4,    curr=5: save None, reverse 5→4, prev=5, curr=None
    #
    # Output: [5,4,3,2,1]

    # Application 2: Reverse Sublist
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:  # LC 92
        """
        Reverse nodes from position left to right (1-indexed).

        Example 1:
        Input: head = [1,2,3,4,5], left = 2, right = 4
        Output: [1,4,3,2,5]

        Strategy: Walk prev to node just before left, then repeatedly pull the node after
        curr to the front of the reversed section — no separate reverse pass needed.

        - TC: O(n), SC: O(1)
        """
        dummy = ListNode(0, head)
        prev = dummy

        for _ in range(left - 1):    # Walk prev to node just before left
            prev = prev.next

        curr = prev.next             # First node of sublist

        for _ in range(right - left):
            next_node = curr.next        # Save next node
            curr.next = next_node.next   # Detach next_node
            next_node.next = prev.next   # next_node points to current front
            prev.next = next_node        # prev points to new front

        return dummy.next

    # Example trace (reverseBetween, left=2, right=4):
    # dummy → 1 → 2 → 3 → 4 → 5
    # prev=node(1), curr=node(2)
    #
    # Iteration 1: pull node(3) to front
    #   curr.next = node(4)           list: 1 → 2 → 4 → 5
    #   next_node(3).next = node(2)        3 → 2 → 4 → 5
    #   prev.next = node(3)           list: 1 → 3 → 2 → 4 → 5
    #
    # Iteration 2: pull node(4) to front
    #   curr.next = node(5)           list: 1 → 3 → 2 → 5
    #   next_node(4).next = node(3)        4 → 3 → 2 → 5
    #   prev.next = node(4)           list: 1 → 4 → 3 → 2 → 5
    #
    # Output: [1,4,3,2,5]

sol = ReversalPattern()
test_head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print("Reversed:", sol.reverseList(test_head))  # 5→4→3→2→1

sol2 = ReversalPattern()
test_head2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print("Sublist reversed:", sol2.reverseBetween(test_head2, 2, 4))  # 1→4→3→2→5

"""
================================================================
PATTERN 2: FAST/SLOW POINTERS
PATTERN EXPLANATION: Two pointers moving at different speeds or with a fixed gap.
Three core applications of the same technique:
1. Find Middle: fast moves 2x — when fast ends, slow is at middle
2. Cycle Detection: if fast ever equals slow, a cycle exists
3. Nth from End: advance fast n steps, then move both — when fast ends, slow is at target

Applications: Find middle, detect cycle, nth from end, palindrome check.
================================================================
"""

class FastSlowPattern:
    """
    Problem: Given head of linked list, return the middle node. If two middles, return second.

    Example:
        Input: [1,2,3,4,5]  Output: node(3)
        Input: [1,2,3,4]    Output: node(3)  <- second middle

    Steps:
    1. slow = head, fast = head.next
    2. While fast and fast.next exist:
       a. slow = slow.next  (1 step)
       b. fast = fast.next.next  (2 steps)
    3. Return slow
    """
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:  # LC 876
        """
        - TC: O(n) - fast visits at most n nodes
        - SC: O(1) - only two pointer variables
        """
        slow = head
        fast = head # Start fast at head for it to travel further (second middle)

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
    
    # Example trace (middleNode):
    # List: 1 → 2 → 3 → 4 → 5
    #
    # slow=1, fast=2
    # Step 1: slow=2, fast=4
    # Step 2: slow=3, fast.next=None — stop
    # Output: node(3)

    # Application 2: Cycle Detection
    def hasCycle(self, head: Optional[ListNode]) -> bool:  # LC 141
        """
        Detect if linked list has a cycle.

        - TC: O(n), SC: O(1)
        """
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  # Pointers met — cycle exists
                return True

        return False  # Fast reached end — no cycle
    
    # Example trace (hasCycle):
    # List: 3 → 2 → 0 → -4 → (back to 2)
    #
    # Step 1: slow=2, fast=0
    # Step 2: slow=0, fast=2
    # Step 3: slow=-4, fast=-4 <- meet! cycle exists
    # Output: True

    # Application 3: Remove Nth from End
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:  # LC 19
        """
        Remove nth node from end using a fixed gap between fast and slow.

        Example 1:
        Input: head = [1,2,3,4,5], n = 2
        Output: [1,2,3,5]

        Strategy: Advance fast n+1steps ahead, then move both until fast ends. Slow lands on the node before the target — delete with slow.next = slow.next.next.

        - TC: O(n), SC: O(1)
        """
        dummy = ListNode(0, head)
        slow = dummy  # dummy gives free +1 offset so gap ends up n+1, not n
        fast = head

        for _ in range(n):  # gap = n+1; slow stops 1 BEFORE target (required for deletion)
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next  # slow is 1 before target — remove target by skipping it

        return dummy.next

    # Example trace (removeNthFromEnd, n=2):
    # dummy → 1 → 2 → 3 → 4 → 5
    # slow=dummy, fast=head(1) → after loop: fast=node(3), gap=n+1=3
    # Move together: slow=1,fast=4 → slow=2,fast=5 → slow=3,fast=None
    # slow.next = slow.next.next → removes node(4) → [1,2,3,5]

sol = FastSlowPattern()
test_head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print("Middle:", sol.middleNode(test_head).val)  # 3

sol2 = FastSlowPattern()
test_head2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print("Remove 2nd from end:", sol2.removeNthFromEnd(test_head2, 2))  # 1→2→3→5

"""
================================================================
PATTERN 3: MERGE SORTED LISTS
PATTERN EXPLANATION: Combine two sorted linked lists into one sorted list. Use a dummy head to eliminate edge cases, compare the front node of each list, attach the smaller one, and advance that list's pointer. When one list is exhausted, attach the remainder of the other. Reuses existing nodes — no new nodes created.

Applications: Merge two sorted lists, merge k sorted lists (extend with heap), sort list.
================================================================
"""

class MergePattern:
    """
    Problem: Merge two sorted linked lists into one sorted list by splicing nodes together.

    Example:
        Input: list1 = [1,2,4], list2 = [1,3,4]
        Output: [1,1,2,3,4,4]

    Steps:
    1. Create dummy node, current = dummy for the merged list
    2. While both lists have nodes:
       a. Compare list1.val and list2.val
       b. Attach the smaller node to current.next
       c. Advance the chosen list's pointer
       d. Advance current: current = current.next
    3. Attach remaining nodes from whichever list isn't empty
    4. Return dummy.next
    """
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:  # LC 21
        """
        - TC: O(n + m) - visit each node from both lists exactly once
        - SC: O(1) - reuse existing nodes, dummy head doesn't count
        """
        dummy = ListNode(0) # Dummy head for merged list
        current = dummy # Pointer to build merged list

        while list1 and list2: # list1 and list2 are just pointers to the current node in each list
            if list1.val <= list2.val:
                current.next = list1  # link node
                list1 = list1.next    # advance pointer
            else:
                current.next = list2  
                list2 = list2.next    
            current = current.next # move current pointer forward

        current.next = list1 if list1 else list2  # Attach remaining

        return dummy.next

# Example trace:
# list1 = 1 → 2 → 4
# list2 = 1 → 3 → 4
#
# Compare 1,1 (equal): attach list1's 1 → result=[1],       list1=2→4
# Compare 2,1:         attach list2's 1 → result=[1,1],     list2=3→4
# Compare 2,3:         attach list1's 2 → result=[1,1,2],   list1=4
# Compare 4,3:         attach list2's 3 → result=[1,1,2,3], list2=4
# Compare 4,4 (equal): attach list1's 4 → result=[1,1,2,3,4], list1=None
# list1 exhausted, attach remaining list2 → result=[1,1,2,3,4,4]
#
# Output: [1,1,2,3,4,4]

sol = MergePattern()
l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
print("Merged:", sol.mergeTwoLists(l1, l2))  # 1→1→2→3→4→4

"""
================================================================
PATTERN 4: TWO-LIST SPLIT AND RECONNECT
PATTERN EXPLANATION: Split the list into two sublists based on a condition (value or index), build each sublist with its own dummy head, then reconnect them at the end. Single traversal, no new nodes — just redirect existing next pointers. Always terminate the second sublist before connecting to avoid cycles.

Applications: Partition by value (LC 86), separate odd/even indices (LC 328), split by any condition.
================================================================
"""

class SplitReconnectPattern:
    """
    Problem: Partition list so all nodes < x come before nodes >= x. Preserve relative order.

    Example:
        Input: head = [1,4,3,2,5,2], x = 3
        Output: [1,2,2,4,3,5]

    Steps:
    1. Create dummy heads: less_dummy (< x), greater_dummy (>= x)
    2. Traverse list, appending each node to the appropriate sublist
    3. Terminate greater: greater.next = None  (prevents cycle)
    4. Connect: less.next = greater_dummy.next
    5. Return less_dummy.next
    """
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:  # LC 86
        """
        - TC: O(n) - single pass
        - SC: O(1) - reuse existing nodes, only two dummy nodes added
        """
        less_dummy = ListNode(0) # Dummy head for less-than-x list
        greater_dummy = ListNode(0) # Dummy head for greater-or-equal-x list
        less = less_dummy # Pointers
        greater = greater_dummy

        current = head # Traverse original list

        while current:
            if current.val < x: # If curr's val is less than x
                less.next = current # Attach to less list
                less = less.next # Move less pointer forward
            else:
                greater.next = current
                greater = greater.next
            current = current.next

        greater.next = None              # Terminate greater list (avoid cycle)
        less.next = greater_dummy.next   # Connect less → greater

        return less_dummy.next

# Example trace (partition, x=3):
# 1 → 4 → 3 → 2 → 5 → 2
#
# Visit 1: < 3  → less=[1]
# Visit 4: >= 3 → greater=[4]
# Visit 3: >= 3 → greater=[4,3]
# Visit 2: < 3  → less=[1,2]
# Visit 5: >= 3 → greater=[4,3,5]
# Visit 2: < 3  → less=[1,2,2]
#
# Connect: [1,2,2] → [4,3,5]
# Output: [1,2,2,4,3,5]


sol = SplitReconnectPattern()
test_head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
print("Partitioned:", sol.partition(test_head, 3))  # 1→2→2→4→3→5



