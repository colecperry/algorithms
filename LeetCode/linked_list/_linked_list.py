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

# ================================================================
# REVERSE TEMPLATE
# ================================================================
def reverse_template(head):
    """
    Reverse linked list using three pointers
    
    TC: O(n) - visit each node once
    SC: O(1) for iterative, O(n) for recursive
    
    WHEN TO USE:
    - Reverse entire list
    - Reverse portion of list
    - Palindrome check
    - Reverse in groups
    
    KEY INSIGHT:
    - Save next before reversing pointer
    - Reverse current.next to point backward
    - Move all three pointers forward
    """
    prev = None
    current = head
    
    while current:
        next_node = current.next  # Save next node so we can move curr forward after reversing ptr
        current.next = prev       # Reverse pointer
        prev = current            # Move prev forward
        current = next_node       # Move current forward
    
    return prev  # New head

# ================================================================
# FAST/SLOW POINTERS TEMPLATE
# ================================================================
def fast_slow_template(head):
    """
    Fast/slow pointers for various applications
    
    TC: O(n) - fast visits at most 2n nodes
    SC: O(1) - only two pointers
    
    WHEN TO USE:
    - Find middle node
    - Detect cycle
    - Find nth from end
    - Check palindrome
    
    PATTERNS:
    - Middle: slow moves 1, fast moves 2, when fast ends slow is at middle
    - Cycle: if fast meets slow, cycle exists
    - Nth from end: create gap of n, move together
    """
    slow = head
    fast = head
    
    # For finding middle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow  # Middle node

# ================================================================
# TWO LIST MERGE TEMPLATE
# ================================================================
def merge_lists_template(list1, list2):
    """
    Merge two sorted lists
    
    TC: O(n + m) - visit all nodes from both lists
    SC: O(1) - reuse existing nodes
    
    WHEN TO USE:
    - Merge sorted lists
    - Combine two lists with ordering
    
    KEY INSIGHT:
    - Use dummy head to simplify
    - Compare heads, attach smaller
    - Attach remaining list at end
    """
    dummy = ListNode(0)
    current = dummy # Ptr for new LL
    
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1 # Attach smaller val to new LL
            list1 = list1.next # Move ptr forward after adding node for list1
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # Attach remaining
    if list1:
        current.next = list1
    elif list2:
        current.next = list2
    
    return dummy.next

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

Pattern Complexities:
1. Reversal: O(n) time, O(1) space iterative
2. Fast/Slow: O(n) time, O(1) space
3. Merge: O(n+m) time, O(1) space
4. In-Place Reorder: O(n) time, O(1) space
5. Partition: O(n) time, O(1) space

Why Linked Lists Are Different:
- No random access: Can't do array[i] in O(1)
- Sequential only: Must start from head
- Pointer manipulation: Core skill is updating next pointers correctly
- Edge cases: Empty list, single node, head deletion

Recursive vs Iterative:
- Iterative: O(1) space, harder to write sometimes
- Recursive: O(n) space (call stack), often more elegant
- For interviews: Know both approaches

Common Space Optimizations:
- Use dummy head instead of special cases
- Reverse in-place instead of creating new list
- Modify pointers instead of creating new nodes

When to Use Each Pattern:
1. Reversal: Reverse order, palindrome check
2. Fast/Slow: Cycle detection, middle, nth from end
3. Merge: Combine sorted lists, merge operations
4. In-Place Reorder: Complex rearrangements without extra space
5. Partition: Split by value, rearrange by condition
"""

"""
LINKED LIST PATTERNS
====================
"""

# ================================================================
# PATTERN 1: REVERSAL
# PATTERN EXPLANATION: Reverse the direction of all next pointers in the list. Use three
# pointers to safely reverse each link: save next node before breaking link, reverse current's
# pointer to point backward, then move all pointers forward. Can be done iteratively (O(1) space)
# or recursively (O(n) space for call stack).
#
# TYPICAL STEPS (Iterative):
# 1. Initialize prev=None, current=head
# 2. While current exists:
#    - Save next node: next_node = current.next
#    - Reverse link: current.next = prev
#    - Move prev forward: prev = current
#    - Move current forward: current = next_node
# 3. Return prev (new head)
#
# Applications: Reverse entire list, reverse portion, palindrome check, reverse in groups.
# ================================================================

class ReversalPattern:
    """
    Problem: Given head of singly linked list, reverse the list and return reversed head.
    
    TC: O(n) - visit each node exactly once
    SC: O(1) for iterative, O(n) for recursive (call stack)
    
    How it works (Iterative):
    1. Use three pointers: prev, current, next
    2. For each node, reverse its next pointer to point backward
    3. Must save next node before reversing link (or lose rest of list)
    4. Move all pointers forward and continue
    5. Return prev (becomes new head when current reaches None)
    
    Visual:
    Before: None ← prev  current → [1] → [2] → [3] → None
    After:  None ← [1] ← [2] ← [3] ← prev  current (None)
    """
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: # LC 206
        prev = None
        current = head
        
        while current:
            # Save next node before breaking link
            next_node = current.next
            
            # Reverse link
            current.next = prev
            
            # Move pointers forward
            prev = current
            current = next_node
        
        return prev  # New head

# Example:
# Original: 1 → 2 → 3 → 4 → 5 → None
#
# Step 1: prev=None, current=1
#   Save next=2, reverse: 1→None
#   Move: prev=1, current=2
#   Result so far: None←1  2→3→4→5
#
# Step 2: prev=1, current=2
#   Save next=3, reverse: 2→1
#   Move: prev=2, current=3
#   Result so far: None←1←2  3→4→5
#
# Step 3: prev=2, current=3
#   Save next=4, reverse: 3→2
#   Move: prev=3, current=4
#   Result so far: None←1←2←3  4→5
#
# Continue...
#
# Final: None ← 1 ← 2 ← 3 ← 4 ← 5 (prev points to 5)
# Output: [5,4,3,2,1]

sol = ReversalPattern()
test_head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
reversed_head = sol.reverseList(test_head)
print("Reversed list:", reversed_head)  # 5→4→3→2→1


# ================================================================
# PATTERN 2: FAST/SLOW POINTERS (MULTIPLE APPLICATIONS)
# PATTERN EXPLANATION: Use two pointers moving at different speeds or maintaining a fixed
# gap. Multiple applications of the same core technique:
#
# 1. Find Middle: fast moves 2x, when fast ends slow is at middle
# 2. Cycle Detection: if fast meets slow, cycle exists
# 3. Nth from End: create gap of n, move together until fast ends
#
# All use fast/slow concept but apply it differently. This is one of the most versatile
# linked list patterns.
#
# TYPICAL STEPS (Find Middle):
# 1. Initialize slow=head, fast=head.next
# 2. While fast and fast.next exist:
#    - Move slow one step
#    - Move fast two steps
# 3. When fast reaches end, slow is at middle
# 4. Return slow
#
# TYPICAL STEPS (Cycle Detection):
# 1. Initialize slow=head, fast=head
# 2. While fast and fast.next exist:
#    - Move slow one step, fast two steps
#    - If slow == fast, cycle detected
# 3. Return true if met, false if fast reached end
#
# TYPICAL STEPS (Nth from End):
# 1. Create dummy node pointing to head (simplifies edge cases like removing head)
# 2. Initialize slow = dummy, fast = head
# 3. Create gap of n nodes:
#       - Move fast forward n steps
#       - Slow stays at dummy
# 4. Move both pointers together until fast reaches end (None)
#       - When fast is None, slow is at node BEFORE the nth from end
# 5. Remove target: slow.next = slow.next.next
# 6. Return dummy.next
#
# Applications: Find middle, detect cycle, find cycle start, nth from end, palindrome check.
# ================================================================

class FastSlowPattern:
    """
    Problem: Given head of linked list, return the middle node. If two middle nodes,
    return the second middle node.
    
    TC: O(n) - fast pointer visits at most n nodes, slow visits n/2
    SC: O(1) - only two pointer variables
    
    How it works:
    1. Slow pointer moves 1 step at a time
    2. Fast pointer moves 2 steps at a time
    3. When fast reaches end (None), slow is at middle
    4. Return slow (middle node)
    
    Why it works:
    - Fast moves twice as fast as slow
    - When fast reaches end, slow is halfway
    - For even length: returns second middle (fast.next becomes None)
    - For odd length: returns exact middle
    """
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]: # LC 876
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next          # Move 1 step
            fast = fast.next.next     # Move 2 steps
        
        return slow  # Middle node
    
    # Application 2: Cycle Detection
    def hasCycle(self, head: Optional[ListNode]) -> bool: # LC 141
        """
        Detect if linked list has cycle
        
        TC: O(n), SC: O(1)
        """
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:  # Pointers met - cycle exists
                return True
        
        return False  # Fast reached end - no cycle
    
    # Application 3: Nth from End (with fixed gap)
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]: # LC 19
        """
        Remove nth node from end using gap technique
        
        TC: O(n), SC: O(1)
        
        Strategy: Create gap of n+1, move together
        """
        dummy = ListNode(0, head)  # Dummy head simplifies deletion
        slow = dummy
        fast = head
        
        # Create gap of n nodes
        for _ in range(n):
            fast = fast.next
        
        # Move both until fast reaches end
        # slow will be at node BEFORE target
        while fast:
            slow = slow.next
            fast = fast.next
        
        # Remove nth node from end
        slow.next = slow.next.next
        
        return dummy.next

# Example (Middle Node):
# List: 1 → 2 → 3 → 4 → 5
#
# Initial: slow=1, fast=1
# Step 1: slow=2, fast=3
# Step 2: slow=3, fast=5
# Step 3: fast.next=None, stop
# slow is at 3 (middle)
# Output: [3,4,5]
#
# Example (Cycle Detection):
# List: 3 → 2 → 0 → -4 ↩ (back to 2)
#
# Step 1: slow=3, fast=3
# Step 2: slow=2, fast=0
# Step 3: slow=0, fast=2
# Step 4: slow=-4, fast=-4  ← They meet!
# Output: True (cycle exists)

sol = FastSlowPattern()
test_head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
middle = sol.middleNode(test_head)
print("Middle node value:", middle.val)  # 3


# ================================================================
# PATTERN 3: MERGE SORTED LISTS
# PATTERN EXPLANATION: Combine two sorted linked lists into one sorted list. Use dummy
# head to simplify edge cases, then compare heads of both lists and attach smaller node.
# Continue until one list exhausted, then attach remaining list. Reuses existing nodes
# without creating new ones.
#
# TYPICAL STEPS:
# 1. Create dummy node (simplifies head management)
# 2. Initialize current pointer at dummy
# 3. While both lists have nodes:
#    - Compare current nodes from both lists
#    - Attach smaller node to result
#    - Move pointer of selected list
#    - Move current pointer forward
# 4. Attach remaining nodes from non-empty list
# 5. Return dummy.next (actual head)
#
# Applications: Merge two sorted lists, merge k sorted lists, sort list (merge sort).
# ================================================================

class MergePattern:
    """
    Problem: Merge two sorted linked lists into one sorted list by splicing together nodes.
    
    TC: O(n + m) - visit each node from both lists exactly once
    SC: O(1) - only reuse existing nodes, no new list created (dummy doesn't count)
    
    How it works:
    1. Use dummy head to avoid special cases for empty lists
    2. Compare values at current position of both lists
    3. Attach node with smaller value to result
    4. Move pointer of selected list forward
    5. When one list exhausted, attach remainder of other list
    6. Return dummy.next (skip dummy node)
    
    Why dummy head helps:
    - No special case for empty list1 or list2
    - No special case for which head to return
    - Simplifies pointer management
    """
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: # LC 21
        dummy = ListNode(0)  # Dummy eliminates edge cases
        current = dummy
        
        # Compare and attach smaller node
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Attach remaining nodes (at most one list is non-empty)
        current.next = list1 if list1 else list2
        
        return dummy.next

# Example:
# list1 = 1 → 2 → 4
# list2 = 1 → 3 → 4
#
# dummy → None
# current = dummy
#
# Step 1: Compare 1 and 1 (equal)
#   Attach list1's 1
#   dummy → 1
#   list1 = 2→4, list2 = 1→3→4
#
# Step 2: Compare 2 and 1
#   Attach list2's 1
#   dummy → 1 → 1
#   list1 = 2→4, list2 = 3→4
#
# Step 3: Compare 2 and 3
#   Attach list1's 2
#   dummy → 1 → 1 → 2
#   list1 = 4, list2 = 3→4
#
# Step 4: Compare 4 and 3
#   Attach list2's 3
#   dummy → 1 → 1 → 2 → 3
#   list1 = 4, list2 = 4
#
# Step 5: Compare 4 and 4
#   Attach list1's 4
#   dummy → 1 → 1 → 2 → 3 → 4
#   list1 = None, list2 = 4
#
# Step 6: list1 is None, attach remaining list2
#   dummy → 1 → 1 → 2 → 3 → 4 → 4
#
# Output: [1,1,2,3,4,4]

sol = MergePattern()
l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
merged = sol.mergeTwoLists(l1, l2)
print("Merged list:", merged)  # 1→1→2→3→4→4


# ================================================================
# PATTERN 4: IN-PLACE REORDERING
# PATTERN EXPLANATION: Rearrange nodes in complex patterns without creating new list.
# Break problem into simpler steps: find middle (fast/slow), reverse second half, merge
# halves by alternating. Combines multiple techniques (fast/slow, reversal, merge) to
# achieve complex reordering in-place.
#
# TYPICAL STEPS (Reorder List):
# 1. Find middle using fast/slow pointers
# 2. Split list into two halves
# 3. Reverse second half
# 4. Merge halves by alternating nodes
# 5. First half gets all "outer" nodes, second gets "inner"
#
# Applications: Reorder list, palindrome check, complex rearrangements.
# ================================================================

class ReorderingPattern:
    """
    Problem: Reorder list from L0→L1→L2→...→Ln-1→Ln to L0→Ln→L1→Ln-1→L2→Ln-2→...
    
    TC: O(n) - three linear passes (find middle, reverse, merge)
    SC: O(1) - only pointer manipulation, no extra nodes
    
    How it works:
    1. Find middle of list using fast/slow pointers
    2. Split list into two halves at middle
    3. Reverse second half
    4. Merge two halves by alternating nodes:
       - Take one from first half, one from second half, repeat
    
    Why three steps:
    - Find middle: Get two equal halves
    - Reverse second: Positions end nodes for easy access
    - Merge alternating: Weave lists together
    
    Example transformation:
    [1,2,3,4] → [1,4,2,3]
    [1,2,3,4,5] → [1,5,2,4,3]
    """
    def reorderList(self, head: Optional[ListNode]) -> None: # LC 143
        if not head or not head.next:
            return
        
        # Step 1: Find middle using fast/slow
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Split list and reverse second half
        second = slow.next
        slow.next = None  # Break link between halves
        
        # Reverse second half
        prev = None
        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node
        
        # Step 3: Merge halves by alternating
        first = head
        second = prev  # Head of reversed second half
        
        while second:
            # Save next pointers
            first_next = first.next
            second_next = second.next
            
            # Weave nodes together
            first.next = second
            second.next = first_next
            
            # Move to next pair
            first = first_next
            second = second_next

# Example:
# Original: 1 → 2 → 3 → 4 → 5
#
# Step 1: Find middle
#   slow ends at 3
#
# Step 2: Split and reverse
#   First half: 1 → 2 → 3
#   Second half: 5 → 4 (reversed)
#
# Step 3: Merge alternating
#   Take 1, take 5: 1 → 5
#   Take 2, take 4: 1 → 5 → 2 → 4
#   Take 3, no more: 1 → 5 → 2 → 4 → 3
#
# Output: [1,5,2,4,3]

sol = ReorderingPattern()
test_head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
sol.reorderList(test_head)
print("Reordered list:", test_head)  # 1→5→2→4→3


# ================================================================
# PATTERN 5: PARTITION/SPLIT BY VALUE
# PATTERN EXPLANATION: Split list into groups based on value comparison. Create separate
# lists for each group, traverse original list once distributing nodes, then reconnect
# groups. Use dummy heads for each group to simplify pointer management.
#
# TYPICAL STEPS:
# 1. Create dummy heads for each partition (e.g., less, greater)
# 2. Traverse original list
# 3. For each node, determine which partition it belongs to
# 4. Attach node to appropriate partition
# 5. Connect partitions in desired order
# 6. Return combined list
#
# Applications: Partition by value, separate odd/even, split by condition.
# ================================================================

class PartitionPattern:
    """
    Problem: Given linked list and value x, partition it such that all nodes < x come
    before nodes >= x. Preserve original relative order in each partition.

    Original: 1 → 4 → 3 → 2 → 5 → 2, x = 3
    Partition into:
        1 → 2 → 2 → 4 → 3 → 5
        Less (< 3)   Greater (>= 3): 
    
    TC: O(n) - single pass through list
    SC: O(1) - reuse existing nodes, only create dummy nodes
    
    How it works:
    1. Create two separate lists: less (< x) and greater (>= x)
    2. Use dummy heads for both lists to simplify management
    3. Traverse original list, attach each node to appropriate list
    4. Connect less list to greater list
    5. Return combined list
    
    Why dummy heads:
    - No special case for first node of each partition
    - Easy to build lists by appending
    - Simple to connect at end
    """
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]: # LC 86
        # Create dummy heads for two partitions
        less_dummy = ListNode(0)
        greater_dummy = ListNode(0)
        
        # Pointers to build each list
        less = less_dummy
        greater = greater_dummy
        
        # Traverse and partition
        current = head
        while current:
            if current.val < x:
                less.next = current
                less = less.next
            else:
                greater.next = current
                greater = greater.next
            current = current.next
        
        # Connect partitions
        greater.next = None  # Terminate greater list
        less.next = greater_dummy.next  # Connect less to greater
        
        return less_dummy.next

# Example:
# Original: 1 → 4 → 3 → 2 → 5 → 2, x = 3
#
# Partition into:
#      1 → 2 → 2 → 4 → 3 → 5
#     Less (< 3)   Greater (>= 3): 
# 
# Step-by-step:
# Visit 1: < 3, add to less → [1]
# Visit 4: >= 3, add to greater → [4]
# Visit 3: >= 3, add to greater → [4,3]
# Visit 2: < 3, add to less → [1,2]
# Visit 5: >= 3, add to greater → [4,3,5]
# Visit 2: < 3, add to less → [1,2,2]
#
# Connect: [1,2,2] → [4,3,5]
# Output: [1,2,2,4,3,5]

sol = PartitionPattern()
test_head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
partitioned = sol.partition(test_head, 3)
print("Partitioned list:", partitioned)  # 1→2→2→4→3→5


# ================================================================
# PATTERN 6: ODD/EVEN REARRANGEMENT
# PATTERN EXPLANATION: Separate nodes at odd and even indices into two lists, then connect
# them. Maintains relative order within each group. Use two pointers to build odd and even
# lists simultaneously during single traversal.
#
# TYPICAL STEPS:
# 1. Create pointers for odd and even lists
# 2. Save head of even list (needed for final connection)
# 3. Traverse list, alternating between odd and even assignments
# 4. Connect odd.next to even_head
# 5. Return head (which is odd list start)
#
# Applications: Odd/even list, separate by index, rearrange by position.
# ================================================================

class OddEvenPattern:
    """
    Problem: Given head of singly linked list, group all nodes with odd indices together
    followed by nodes with even indices. Return reordered list.
    
    Note: Indices are 1-indexed in problem description.
    
    TC: O(n) - single pass through list
    SC: O(1) - rearrange pointers in-place
    
    How it works:
    1. Odd pointer starts at head (index 1)
    2. Even pointer starts at head.next (index 2)
    3. Save even_head to connect later
    4. Traverse: odd points to next odd, even points to next even
    5. Connect end of odd list to start of even list
    6. Return head (odd list)
    
    Pattern:
    - odd.next = odd.next.next (skip even node)
    - even.next = even.next.next (skip odd node)
    - Both pointers advance simultaneously
    """
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]: # LC 328
        if not head or not head.next:
            return head
        
        odd = head
        even = head.next
        even_head = even  # Save start of even list
        
        while even and even.next:
            # Link odd to next odd node
            odd.next = even.next
            odd = odd.next
            
            # Link even to next even node
            even.next = odd.next
            even = even.next
        
        # Connect odd list to even list
        odd.next = even_head
        
        return head

# Example:
# Original: 1 → 2 → 3 → 4 → 5
#
# Indices:  1   2   3   4   5
# Odd:      1       3       5
# Even:         2       4
#
# Build process:
# odd = 1, even = 2, even_head = 2
#
# Iteration 1:
#   odd.next = 3 (skip 2)
#   odd = 3
#   even.next = 4 (skip 3)
#   even = 4
#   List state: 1→3→5, 2→4→None
#
# Iteration 2:
#   odd.next = 5 (skip 4)
#   odd = 5
#   even.next = None
#   even = None
#
# Connect: odd.next = even_head
#   1 → 3 → 5 → 2 → 4
#
# Output: [1,3,5,2,4]

sol = OddEvenPattern()
test_head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
reordered = sol.oddEvenList(test_head)
print("Odd/Even list:", reordered)  # 1→3→5→2→4
