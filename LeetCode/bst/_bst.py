"""
BINARY SEARCH TREE STUDY GUIDE
=====================================

# What is a Binary Search Tree?

A Binary Search Tree is a hierarchical data structure where:
- Each node has at most two children (left and right)
- Left child's value < parent's value < right child's value
- This ordering property applies to ALL nodes in the tree

Example BST:
        8
       / \
      3   10
     / \    \
    1   6    14
       / \   /
      4   7 13

Key operations (average case O(log n), worst case O(n)):
- Search: Start at root, go left if target < current, right if target > current
- Insert: Find correct position using search logic, add new node as leaf
- Delete: Three cases - no children, one child, or two children (replace with successor)

Advantages:
- Fast search, insert, delete operations (when balanced)
- In-order traversal gives sorted sequence
- No extra memory needed for sorting

Disadvantages:
- Can become unbalanced (essentially a linked list in worst case)
- Performance degrades to O(n) when unbalanced

Common use cases: Database indexing, expression parsing, file systems

# Template Decision Framework:
# 1. Need sorted data? → Template 1 (In-order - BST specific!)
# 2. Find specific value? → Template 2 (Search recursive/iterative)  
# 3. Add new node? → Template 2 (Insert recursive/iterative)
# 4. Remove node? → Template 3 (Delete - 3 cases)
# 5. Find extremes? → Template 3 (Min/Max)
# 6. Find next/prev? → Template 3 (Successor/Predecessor)
# 7. Value constraints? → Template 4 (Bounds)
# 8. Extra storage needed? → Template 5 (+ Data Structure)

STEP 1: MASTER THE CORE TEMPLATES FIRST!
"""

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ========================================================
# CORE BST TEMPLATE - MASTER THESE FIRST!
# =========================================================

# ------------------------------------------------------------------------------
# 🔥 TEMPLATE 1: BST TRAVERSALS (Foundation for everything)
# ------------------------------------------------------------------------------
def inorder_traversal(root):
    """
    In-order: Left → Root → Right
    ⭐ KEY: Gives SORTED sequence for BST! In-order traversal visits nodes in the order: all smaller values (left subtree) → current value (root) → all larger values (right subtree), which naturally produces a sorted sequence because of the BST property.
    """
    result = []
    def dfs(node):
        if not node:  # Base case
            return
        dfs(node.left)      # Traverse left
        result.append(node.val)  # Process current
        dfs(node.right)     # Traverse right
    dfs(root)
    return result

# Build test tree: [5,3,6,2,4,null,7]
#       5
#      / \
#     3   6
#    / \   \
#   2   4   7

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)

# Test traversal
print("In-order (L-Root-R):", inorder_traversal(root))

# ------------------------------------------------------------------------------
# 🔥 TEMPLATE 2: BST SEARCH, INSERT, (Use BST property!) - ITERATIVE & RECURSIVE
# ------------------------------------------------------------------------------

# SEARCH ITERATIVE
def search_iterative(root, target):
    """Iterative version - same logic, O(1) space"""
    while root:
        if root.val == target:
            return root
        elif target < root.val:
            root = root.left
        else:
            root = root.right
    return None

#       5
#      / \
#     3   6
#    / \   \
#   2   4   7

print(search_iterative(root, 4))

# SEARCH RECURSIVE
def search_recursive(root, target):
    """
    Core BST search template - USE THIS PATTERN!
    Time: O(h), Space: O(h) recursive or O(1) iterative
    """
    if not root:
        return None
    if root.val == target:
        return root
    elif target < root.val:
        return search_recursive(root.left, target)
    else:
        return search_recursive(root.right, target)
    
#       5
#      / \
#     3   6
#    / \   \
#   2   4   7
print(search_recursive(root, 4))

# INSERT ITERATIVE
def insert_iterative(root, val):
    new_node = TreeNode(val) # Create a new node for inserting
    if root == None: # Edge Case: If our tree is empty,
        root = new_node # set root to the new node
        return True # return True to stop the code
    
    temp = root # Create temp for traversal
    while (True): # Create an infinite until insertion
        if new_node.val == temp.val: # Can't have == values in BST -> False
            return False 
        if new_node.val < temp.val: # Insertion node <
            if temp.left is None: # Check if open spot left
                temp.left = new_node # Yes -> set NN there
                return True # Stop code
            else: # No open spot
                temp = temp.left # Move ptr left
        else: # Insertion Node >
            if temp.right is None: #Check if open spot right
                temp.right = new_node # Yes -> set NN there
                return True # Stop code
            else: # No open spot
                temp = temp.right # Move ptr right

#       5
#      / \
#     3   6
#    / \   \
#   2   4   7
print(insert_iterative(root, 1))

# INSERT RECURSIVE
def insert_recursive(root, val):
    """
    Complete BST insert - handles empty tree and insertion
    Time: O(h), Space: O(h) recursion stack
    """
    if root == None:  # Base case (empty tree OR we found insertion spot)
        return TreeNode(val) 
    if val < root.val:
        root.left = insert_recursive(root.left, val)
    elif val > root.val:  # Use elif for clarity
        root.right = insert_recursive(root.right, val) # One we hit base case, we connect root.left or root.right to the new treeNode we created
    return root

#       5
#      / \
#     3   6
#    / \   \
#   2   4   7
#  /
# 1
print(insert_recursive(root, 8))

# -------------------------------------------------------------------------
# 🔥 TEMPLATE 3: BST DELETE NODE & SUCCESSOR/PREDECESSOR
# -------------------------------------------------------------------------

# THREE DELETE CASES:
# Case 1: Node has no children -> simply remove it by returning None
# Case 2: Node has one child -> elevate child to take its position
# Case 3: Node has two children -> find successor and replace value

def find_successor(root, target_val): 
    """
    Find smallest value greater than target (inorder successor)
    Keep track of the smallest value that's still larger than the target
    """
    successor = None
    current = root
    
    while current:
        if current.val > target_val: # Current node is larger than target
            successor = current  # Potential successor found
            current = current.left  # Look for smaller successor in left subtree
        else:
            current = current.right  # Current node <= target, go right
    
    return successor

def find_predecessor(root, target_val):
    """
    Find largest value smaller than target (inorder predecessor)
    Keep track of the biggest value that's still less than the target
    """
    predecessor = None
    current = root
    
    while current:
        if current.val < target_val: # Current val < target
            predecessor = current  # Potential predecessor found
            current = current.right  # Look for larger predecessor in right subtree
        else:
            current = current.left  # Current val >= target, go left
    
    return predecessor

def min_value(current):
    """Helper for Case 3: Find min by going left until None (successor in right subtree)"""
    while current.left is not None:
        current = current.left
    return current.val  # Return the value, not the node

def delete_node(current, target):
    """
    Complete BST deletion handling all 3 cases
    Returns updated tree after deletion
    """
    if current == None:
        return None
    
    if target < current.val:  # Traverse left or right until you find target
        current.left = delete_node(current.left, target)
    elif target > current.val:  
        current.right = delete_node(current.right, target)
    else:  # Found node to delete
        # Case 1: No children
        if current.left == None and current.right == None:
            return None # Return None to parent's left/right pointer
        # Case 2: One child - promote child to take deleted node's position
        elif current.left == None: 
            return current.right # Promote right child
        elif current.right == None:
            return current.left # Promote left child
        # Case 3: Two children - replace with successor value
        else:
            sub_tree_min = min_value(current.right) # Find successor (smallest in right subtree)
            current.val = sub_tree_min # Copy successor's value to current node
            current.right = delete_node(current.right, sub_tree_min) # Delete original successor
    
    return current # Return updated tree back up the call stack

# Test tree setup
#       5
#      / \
#     3   6
#    / \   \
#   2   4   7

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)

# Test successor/predecessor
print(find_successor(root, 5))    # 6
print(find_successor(root, 3))    # 4
print(find_predecessor(root, 6))  # 5
print(find_predecessor(root, 4))  # 3

# Test deletion cases
print(delete_node(root, 2))  # Case 1 - node has no children
print(delete_node(root, 7))  # Case 2 - node has one child  
print(delete_node(root, 5))  # Case 3 - node has two children


# ------------------------------------------------------------------------------
# 🔥 TEMPLATE 4: BST WITH BOUNDS (Super important!)
# ------------------------------------------------------------------------------

    # BST traversal with value constraints - uses BST property for efficient pruning
    
    # Purpose: Process only nodes within [min_val, max_val] range
    # Key insight: BST property allows us to skip entire subtrees that can't contain valid nodes
    
    # Algorithm:
    # - If current node < min_val: entire left subtree is too small, only check right
    # - If current node > max_val: entire right subtree is too large, only check left  
    # - If current node in range: check both subtrees and include current node
    
    # Common uses:
    # - Range sum queries (sum all values in range)
    # - Range validation (check if all nodes meet criteria)
    # - Counting nodes in range
    # - Finding nodes within bounds
    
    # Time: O(k + h) where k = nodes in range, h = height
    # Space: O(h) for recursion stack
    
    # Example: For range [3,6] in tree [2,3,4,5,6,7]
    # - Skips node 2 and its subtree (too small)
    # - Includes nodes 3,4,5,6 (in range)  
    # - Skips node 7 and its subtree (too large)

    #        5
    #       / \
    #      3   6
    #     / \   \
    #    2   4   7

def traverse_with_bounds(root, min_val, max_val):
    if not root:
        return 0  # or whatever base case you need
    
    if root.val < min_val:
        # Current too small, go right only
        return traverse_with_bounds(root.right, min_val, max_val)
    elif root.val > max_val:
        # Current too large, go left only  
        return traverse_with_bounds(root.left, min_val, max_val)
    else:
        # Current in range, explore both sides
        left_result = traverse_with_bounds(root.left, min_val, max_val)
        right_result = traverse_with_bounds(root.right, min_val, max_val)
        return root.val + left_result + right_result  # Return range subtree value

# Example 1: Sum all nodes in range [3, 6]
print(traverse_with_bounds(root, 3, 6)) # 18 (3+4+5+6)

# Example 2: Sum all nodes in range [4, 7]
print(traverse_with_bounds(root, 4, 7)) # 22 (4+5+6+7)

# ------------------------------------------------------------------------------
# 🔥 TEMPLATE 5: BST + EXTRA DATA STRUCTURE
# ------------------------------------------------------------------------------
def traverse_with_set(root, target_set, target):
    """
    BST + Data Structure Pattern - combine tree traversal with hash set/map
    
    Purpose: Find relationships between nodes (pairs, duplicates, complements (target - cur.val))
    
    Why: BST gives systematic traversal, hash set gives O(1) lookups
    
    Common uses:
    - Two Sum: find pair that adds to target
    - Find duplicates during traversal
    - Track complements or frequencies
    
    Pattern:
    1. Visit each node in BST
    2. Check if current node completes a condition (using set)
    3. Store info for future nodes (complement, value, etc.)
    4. Return when condition met
    
    Example: Two Sum with target=9
    - Visit 3: check if 6 in set? No. Add 6 to set.
    - Visit 6: check if 3 in set? Yes! Found pair.
    """
    if not root:
        return False
    
    # Check if current node satisfies condition
    if root.val in target_set:
        return True
    
    # Add current node's complement to set
    target_set.add(target - root.val)  # Example for two sum
    
    # Continue traversal
    return (traverse_with_set(root.left, target_set, target) or 
            traverse_with_set(root.right, target_set, target))

    #        5
    #       / \
    #      3   6
    #     / \   \
    #    2   4   7

# Example 1: Find if any two nodes sum to 9
target_set = set()  # Create empty set
print(traverse_with_set(root, target_set, 9)) # Should be True (2+7=9)

# Example 2: Find if any two nodes sum to 15
target_set_2 = set()  # Create empty set
print(traverse_with_set(root, target_set_2, 15)) # Should be False


# =========================================================
# CORE BST PROPERTIES & DECISION FRAMEWORK
# =========================================================
"""
🎯 BST PROPERTIES (Memorize these!):
- Left subtree: ALL values < root
- Right subtree: ALL values > root  
- In-order traversal: ALWAYS gives sorted sequence
- Search/Insert: O(log n) average, O(n) worst case

🎯 DECISION FRAMEWORK:
1. Need sorted sequence? → In-order traversal
2. Need to find something? → Use BST search template
3. Need to add something? → Use BST insert template  
4. Have value constraints? → Use bounds template
5. Need extra info storage? → BST + data structure template

🎯 COMMON BASE CASES:
- if not root: return None/0/False (depends on problem)
- if root.val == target: return root/True
- if condition_met: return result

🎯 RECURSIVE PATTERN:
1. Handle base case
2. Make BST decision (left vs right vs both)
3. Recurse with updated parameters
4. Return/combine results
"""

# ===================================================================
# NOW APPLY THE TEMPLATES TO SPECIFIC PROBLEMS
# ===================================================================

# ===================================================================
# LC 700 - Search in a Binary Search Tree  
# ===================================================================
# Pattern: Basic BST Search
# Key Insight: Use BST property to eliminate half the tree at each step

def searchBSTRecursive(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    """
    Given the root of a BST, search for a node with given value and return it
    Time: O(h) where h = height
    Space: O(h) recursion stack
    """
    if not root:  # Empty tree or we reached the end -> Base case
        return None
    if root.val == val:  # At each node, check if node's val == val
        return root
    if val < root.val: # If target val < curr
        return searchBSTRecursive(root.left, val)  # Recurse left
    else: # If target val > curr
        return searchBSTRecursive(root.right, val)  # Search right

def searchBSTIterative(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root: # Edge case for an empty tree
        return None
    while root: # Iterate until we hit None
        if root.val == val: # Check if values match
            return root # Return subtree
        if val < root.val: # If val is less
            root = root.left # Iterate left
        else:
            root = root.right # Iterate right

#                  4
#                 / \
#                /   \
#               2     7
#              / \
#             1   3

t1 = TreeNode(4)
t1.left = TreeNode(2)
t1.right = TreeNode(7)
t1.left.left = TreeNode(1)
t1.left.right = TreeNode(3)
print(searchBSTRecursive(t1, 2)) # [2,1,3]
print(searchBSTRecursive(t1, 5)) # []

print(searchBSTIterative(t1, 2)) # [2,1,3]
print(searchBSTIterative(t1, 5)) # []


# ===================================================================
# LC 653 - Two Sum IV (Input is a BST)
# ===================================================================
# Pattern: BST + Hash Set
# Template Used: BST + Extra Data Structure (Template 5)
# Key Insight: Use hash set during traversal to find complements

def findTarget(root: Optional[TreeNode], k: int) -> bool:
    """
    Find if there exist two elements that add up to k
    Time: O(n) - visit each node once
    Space: O(n) for set + O(h) recursion stack
    """
    diffs = set()  # Create a set of differences/complements (values we are looking for to complete the sum)
    
    def dfs(node):
        if not node:  # Base case -> reached a leaf node
            return False  # If there is no node it can't be the match
        
        if node.val in diffs:  # Check if we found the matching node
            return True
        
        diffs.add(k - node.val)  # Add the difference needed to find match
        
        # Recursively search the left and right subtrees
        found_in_left = dfs(node.left)
        found_in_right = dfs(node.right)
        
        return found_in_left or found_in_right
    
    return dfs(root)  # Call helper function with the root

#                  5
#                 / \
#                /   \
#               3     6
#              / \     \
#             2   4     7

t1 = TreeNode(5)
t1.left = TreeNode(3)
t1.right = TreeNode(6)
t1.left.left = TreeNode(2)
t1.left.right = TreeNode(4)
t1.right.right = TreeNode(7)
print(findTarget(t1, 9)) # true
print(findTarget(t1, 28)) # false

# ===================================================================
# LC 783 - Minimum Distance Between BST Nodes
# ===================================================================
# Pattern: In-order Traversal + Adjacent Comparison
# Template Used: In-order Traversal (Template 1)
# Key Insight: In-order traversal of BST gives you all the values in sorted order, in any sorted list the minimum must be between neighbors

def minDiffInBST(root: Optional[TreeNode]) -> int:
    """
    Find minimum difference between any two nodes in BST
    Time: O(n) - visit all nodes
    Space: O(n) for array + O(h) recursion
    """
    arr = []  # Array stores in-order DFS elements (sorted)
    
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        arr.append(node.val)  # Create an in-order array
        dfs(node.right)
        return
    
    dfs(root)  # Call helper
    min_diff = float('inf')  # Track min difference
    
    for i in range(1, len(arr)):  # Loop through sorted array from index 1
        min_diff = min(min_diff, arr[i] - arr[i-1])  # Update min diff
    
    return min_diff

#               4
#              / \
#             2   6
#            / \
#           1   3

t1 = TreeNode(4)
t1.left = TreeNode(2)
t1.right = TreeNode(6)
t1.left.left = TreeNode(1)
t1.left.right = TreeNode(3)

print(minDiffInBST(t1))

# ===================================================================
# LC 938 - Range Sum of BST
# ===================================================================
# Pattern: BST Traversal with Pruning
# Template Used: BST With Bounds (Template 4)
# Key Insight: Use BST property to skip entire subtrees

def rangeSumBST(root: Optional[TreeNode], low: int, high: int) -> int:
    """
    Return sum of values of all nodes with value in range [low, high]
    Time: O(n) worst case, better with pruning
    Space: O(h) recursion stack
    """
    def dfs(node, low, high):
        if not node:  # Base case
            return 0  # Empty node adds zero to the sum
        
        if low <= node.val <= high:  # If node in range
            left_sum = dfs(node.left, low, high)  # Calc left sum
            right_sum = dfs(node.right, low, high)  # Calc right sum
            return node.val + left_sum + right_sum  # Return total subtree sum
        
        elif node.val < low:  # If node not in range (too low)
            return dfs(node.right, low, high)  # Only recurse right
        
        else:  # node.val > high (too high)
            return dfs(node.left, low, high)  # Only recurse left
    
    return dfs(root, low, high)  # Call helper function

#                   10
#                  /  \
#                 /    \
#                5     15
#               / \      \
#              3   7      18

t1 = TreeNode(10)
t1.left = TreeNode(5)
t1.right = TreeNode(15)
t1.left.left = TreeNode(3)
t1.left.right = TreeNode(7)
t1.right.right = TreeNode(18)

print(rangeSumBST(t1, 7, 15)) # Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.