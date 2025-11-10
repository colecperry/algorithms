# =============================================================================
# WHAT IS A LINKED LIST?
# =============================================================================
"""
A linked list is a linear data structure where elements (nodes) are connected via pointers:
    - Each node contains data and a reference (pointer) to the next node
    - Unlike arrays, elements are not stored in contiguous memory
    - Head points to first node, last node points to None
    - Types: Singly linked, doubly linked, circular

                                VISUAL EXAMPLE:

    Singly Linked List: head → [1|●] → [2|●] → [3|●] → None
    
    Each box represents a node:
        [data | next pointer]
    
    Node structure:
        class ListNode:
            def __init__(self, val=0, next=None):
                self.val = val      # Data
                self.next = next    # Pointer to next node
    
    Example: LinkedList with values 1 → 2 → 3
    
        head
         ↓
        [1|●]──→[2|●]──→[3|●]──→ None
         node1   node2   node3
    
    Access patterns:
    - head.val = 1 (first node's value)
    - head.next = node2 (pointer to second node)
    - head.next.val = 2 (second node's value)
    - head.next.next.next = None (end of list)

Array vs Linked List representation:
- Array: [1, 2, 3] → contiguous memory, direct index access
- Linked List: head → 1 → 2 → 3 → None → non-contiguous, sequential access
"""

# =============================================================================
# LINKED LIST ADVANTAGES & DISADVANTAGES
# =============================================================================
"""
Advantages:
- Dynamic size (no fixed capacity)
- Efficient insertion/deletion at beginning: O(1)
- No memory waste from unused capacity
- Easy to implement stacks and queues

Disadvantages:
- No random access (must traverse from head)
- Extra memory for pointers
- Cache-unfriendly (non-contiguous memory)
- Traversal is sequential only

        Operation       | Linked List | Array (Dynamic)
        ----------------|-------------|------------------
        get(index)      | O(n)        | O(1)
        prepend         | O(1)        | O(n) -> must shift all ele's one position to the right
        append          | O(n)*       | O(1)**
        pop_first       | O(1)        | O(n) -> must shift all ele's one position to the left
        pop             | O(n)        | O(1)
        insert(index)   | O(n)        | O(n)
        remove(index)   | O(n)        | O(n)

*O(1) if tail pointer is maintained
**Amortized O(1) for dynamic arrays (occasionally O(n) when resizing)
    
"""

# =============================================================================
# WHEN TO USE LINKED LISTS
# =============================================================================
"""
When linked lists shine:
    - Frequent insertions/deletions at beginning
    - Unknown or dynamic size
    - Don't need random access
    - Implementing other data structures (stacks, queues)
    - Memory fragmentation concerns (dynamic allocation)

Real-world use cases:
    - Undo/redo functionality (doubly linked list)
    - Music playlist (next/previous)
    - Browser history
    - Image viewer (next/previous image)
    - Hash table collision handling (chaining)
    - Operating system process scheduling

"""

# =============================================================================
# LINKED LIST TYPES
# =============================================================================
"""
1. **Singly Linked List**: One pointer (next) per node
    head → [1|●] → [2|●] → [3|●] → None

2. **Doubly Linked List**: Two pointers (prev, next) per node
    None ← [●|1|●] ↔ [●|2|●] ↔ [●|3|●] → None

3. **Circular Linked List**: Last node points back to head
    head → [1|●] → [2|●] → [3|●] ─┐
            ↑                     │
            └─────────────────────┘
"""

# ============================================================================
# CORE TEMPLATE: LINKED LIST IMPLEMENTATION WITH CORE OPERATIONS
# ============================================================================

class ListNode:
    """LeetCode standard node definition"""
    def __init__(self, val=0, next=None):
        self.val = val      # Data stored in node
        self.next = next    # Pointer to next node

class LinkedListOperations:
    """
    Common linked list operations using LeetCode ListNode
    Note: LeetCode problems typically give you head, not a LinkedList class
    """
    
    # ========================================================================
    # CORE OPERATION 1: APPEND - Add node to end
    # ========================================================================
    def append(self, head, value):
        """
        Add node to end of list - O(n)
        
        TC: O(n) - traverse to end
        SC: O(1) - only create one node
        """
        new_node = ListNode(value)  # Create new node
        
        if not head:  # If list is empty
            return new_node # return only that node (it's the head)
        
        # Traverse to last node
        current = head # curr pointer
        while current.next:
            current = current.next
        current.next = new_node  # Link last node to new node

        return head # return whole LL
    
    # ========================================================================
    # CORE OPERATION 2: PREPEND - Add node to beginning
    # ========================================================================


    def prepend(self, head, value):
        """
        Add node to beginning - O(1)
        
        TC: O(1) - just update pointers
        SC: O(1) - only create one node
        """
        new_node = ListNode(value)  # Create new node
        new_node.next = head        # Point new node to current head
        return new_node             # Return new head
    
    # ========================================================================
    # CORE OPERATION 3: POP - Remove from end
    # ========================================================================
    def pop(self, head):
        """
        Remove node from end - O(n)
        
        TC: O(n) - traverse to second-to-last node
        SC: O(1) - constant space
        """
        if not head:  # Empty list -> can't pop
            return None
        
        if not head.next:  # Only one node 
            return None
        
        # Find second-to-last node
        current = head
        while current.next.next:
            current = current.next
        
        current.next = None  # Remove last node
        return head
    
    # ========================================================================
    # CORE OPERATION 4: POP_FIRST - Remove from beginning
    # ========================================================================
    def pop_first(self, head):
        """
        Remove node from beginning - O(1)
        
        TC: O(1) - just update head
        SC: O(1) - constant space
        """
        if not head:  # Empty list
            return None
        
        return head.next  # Return new head (second node)
    
    # ========================================================================
    # CORE OPERATION 5: GET - Access node at index
    # ========================================================================
    def get(self, head, index):
        """
        Get node at index - O(n)
        
        TC: O(n) - traverse to index
        SC: O(1) - constant space
        """
        if index < 0:  # Invalid index (negative index)
            return None
        
        current = head
        for _ in range(index):
            if not current:  # Index out of bounds (index >= length)
                return None
            current = current.next
        
        return current
    
    # ========================================================================
    # CORE OPERATION 6: SET_VALUE - Update node value at index
    # ========================================================================
    def set_value(self, head, index, value):
        """
        Update value at index - O(n)
        
        TC: O(n) - traverse to index
        SC: O(1) - constant space
        """
        node = self.get(head, index)  # Get node at index
        if node: # If we find a node with that index
            node.val = value  # Update value
            return True
        return False
    
    # ========================================================================
    # CORE OPERATION 7: INSERT - Add node at index
    # ========================================================================
    def insert(self, head, index, value):
        """
        Insert node at index - O(n)
        
        TC: O(n) - traverse to index
        SC: O(1) - only create one node
        """
        if index < 0:  # Invalid index
            return head
        
        if index == 0:  # Insert at beginning
            return self.prepend(head, value)
        
        # Find node before insertion point
        prev = self.get(head, index - 1)
        if not prev:  # Index out of bounds
            return head
        
        new_node = ListNode(value)      # Create new node
        prev.next = new_node            # Point prev (node before insertion) to new node
        new_node.next = prev.next       # Point new node (node we are inserting) to next node
        return head
    
    # ========================================================================
    # CORE OPERATION 8: REMOVE - Delete node at index
    # ========================================================================
    def remove(self, head, index):
        """
        Remove node at index - O(n)
        
        TC: O(n) - traverse to index
        SC: O(1) - constant space
        """
        if index < 0 or not head:  # Invalid index or empty list
            return head
        
        if index == 0:  # Remove first node
            return head.next
        
        # Find node before target
        prev = self.get(head, index - 1)
        if not prev or not prev.next:  # Index out of bounds
            return head
        
        prev.next = prev.next.next  # Skip target node (removes the node after prev)
        return head