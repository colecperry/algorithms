"""
=================================================================
BINARY SEARCH TREE COMPLETE GUIDE
=================================================================

WHAT IS A BINARY SEARCH TREE?
-----------------------------
A Binary Search Tree (BST) is a hierarchical data structure where each node has at most
two children, and the tree maintains a strict ordering property:
- All values in left subtree < node value < all values in right subtree
- This property holds for EVERY node in the tree
- Enables efficient search, insert, and delete operations

Example BST:
        8
       / \
      3   10
     / \    \
    1   6    14
       / \   /
      4   7 13

BST Properties:
- In-order traversal always gives sorted sequence
- Search/Insert/Delete: O(log n) average, O(h) worst case where h = height
- Can degrade to O(n) if tree becomes unbalanced (like linked list)

When to use BST:
- Need to maintain sorted data with frequent insertions/deletions
- Need fast lookups (O(log n) average)
- Want sorted traversal without extra sorting step

When NOT to use BST:
- Need guaranteed O(log n) operations (use balanced BST like AVL/Red-Black)
- Data rarely changes (just sort array once)
- Need range minimum/maximum queries (use segment tree)

Common BST problem types:
- Basic operations (search, insert, delete)
- Traversal problems (especially in-order)
- Validation and property checking
- Range queries
- Two-pointer style with BST structure
- Construction and conversion

BST CORE TEMPLATES
==================
"""

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ================================================================
# BST SEARCH TEMPLATE
# ================================================================
def bst_search(root, target):
    """
    Template for searching in BST using BST property
    
    TC: O(h) where h = height of tree (log n average, n worst case)
    SC: O(h) for recursive, O(1) for iterative
    
    WHEN TO USE:
    - Need to find specific value in BST
    - Need to find insertion position
    - Navigate tree based on value comparisons
    
    KEY INSIGHT:
    - BST property allows eliminating half the tree at each step
    - Compare with current node to decide left or right
    """
    # Recursive version
    if not root:
        return None
    if root.val == target:
        return root
    elif target < root.val:
        return bst_search(root.left, target)
    else:
        return bst_search(root.right, target)

def bst_search_iterative(root, target):
    """Iterative version - same logic, O(1) space"""
    while root:
        if root.val == target:
            return root
        elif target < root.val:
            root = root.left
        else:
            root = root.right
    return None

# ==============================================================================
# IN-ORDER TRAVERSAL TEMPLATE - a BST gives a sorted sequence for this traversal
# ==============================================================================
def inorder_traversal(root):
    """
    Template for in-order traversal of BST
    
    TC: O(n) - visit each node once
    SC: O(h) - recursion stack depth
    
    WHEN TO USE:
    - Need sorted sequence from BST
    - Need to process nodes in ascending order
    - Compare adjacent values in sorted order
    
    KEY INSIGHT:
    - In-order (Left-Root-Right) always gives sorted sequence in BST
    - This is THE fundamental BST traversal pattern
    """
    result = []
    
    def dfs(node):
        if not node:
            return
        dfs(node.left)          # Visit left subtree first
        result.append(node.val)  # Process current node
        dfs(node.right)         # Visit right subtree last
    
    dfs(root)
    return result

# ================================================================
# BST VALIDATION TEMPLATE (WITH BOUNDS)
# ================================================================
def validate_bst(root, min_val=float('-inf'), max_val=float('inf')):
    """
    Template for validating BST property with bounds. Learn this general pattern to learn how to pass constraints down the tree.     
    
    BST WITH BOUNDS Technique:
    Instead of comparing each node with ALL ancestors, we pass down
    valid RANGE (min, max) that each node must satisfy. As we go down:
    - Left child: inherits parent as NEW upper bound
    - Right child: inherits parent as NEW lower bound
    
        Example of bounds changing:
                  5 (min=-∞, max=∞)
                 / \
         (-∞,5) 3   7 (5,∞)
               / \ / \
        (-∞,3)2  4 6 8 (7,∞)
             (3,5)(5,7)
    
    Node 4: must be > 3 (from parent) AND < 5 (from grandparent)
    Node 6: must be > 5 (from grandparent) AND < 7 (from parent)
    
    TC: O(n) - visit each node once
    SC: O(h) - recursion stack
    
    WHEN TO USE:
    - Need to validate if tree is valid BST
    - Check if all nodes satisfy value constraints
    - Track min/max bounds as you traverse
    
    KEY INSIGHT:
    - Each node must be within bounds set by ancestors
    - Left child: max bound becomes parent value
    - Right child: min bound becomes parent value
    """
    # Empty tree is valid
    if not root:
        return True
    
    # Check if current node is within bounds
    if root.val <= min_val or root.val >= max_val:
        return False
    
    # Check left subtree: all values must be < root.val 
    is_left_valid = validate_bst(root.left, min_val, root.val) # -> pass down root as max_val
    
    # Check right subtree: all values must be > root.val 
    is_right_valid = validate_bst(root.right, root.val, max_val) # -> pass down root as min_val
    
    # Both subtrees must be valid
    return is_left_valid and is_right_valid

# Test 1: Valid BST
#      5
#     / \
#    3   7
#   / \
#  2   4
valid_bst = TreeNode(5,
    TreeNode(3, TreeNode(2), TreeNode(4)),
    TreeNode(7))
print("Test 1 (Valid BST):", validate_bst(valid_bst))  # True

# Test 2: Invalid BST - right subtree has value less than root
#      5
#     / \
#    3   7
#   / \
#  2   6  ← 6 is in left subtree but > 5
invalid_bst = TreeNode(5,
    TreeNode(3, TreeNode(2), TreeNode(6)),
    TreeNode(7))
print("Test 2 (Invalid BST):", validate_bst(invalid_bst))  # False


# ================================================================
# RANGE QUERY TEMPLATE (BOUNDS PRUNING)
# ================================================================
def rangeSumBST(root, low, high):
    """
    Template for range queries with pruning.

    Problem: find sum of all node values within range [low, high] in a BST.

    BOUNDS PRUNING Technique:
    Instead of visiting every node, we use BST properties to SKIP entire
    subtrees that can't contain values in our range. This is much more
    efficient than checking every node.
    
    TC: O(k + h) where k = nodes in range, h = height
    SC: O(h) - recursion stack
    
    WHEN TO USE:
    - Need to process only nodes within value range
    - Want to skip entire subtrees outside range
    - Range sum, range count, range search
    
    KEY INSIGHT:
    - If node.val < low: skip left subtree (all too small)
    - If node.val > high: skip right subtree (all too large)
    - Only explore both subtrees if node in range
    """
    if not root: # Base case -> reached end of tree
        return 0 # Null node adds zero to sum
    
    if root.val < low:
        # Current too small, entire left subtree too small, do not add to sum
        return rangeSumBST(root.right, low, high) # -> only check right
    elif root.val > high:
        # Current too large, entire right subtree too large, do not add to sum
        return rangeSumBST(root.left, low, high) # -> only check left
    else:
        # Current in range, check both subtrees and add valid nodes to sum
        left_sum = rangeSumBST(root.left, low, high) # go left
        right_sum = rangeSumBST(root.right, low, high) # and right
        return root.val + left_sum + right_sum
    
# Test 1: Standard example
#        10
#       /  \
#      5    15
#     / \     \
#    3   7    18
tree1 = TreeNode(10,
    TreeNode(5, TreeNode(3), TreeNode(7)),
    TreeNode(15, None, TreeNode(18)))
print("Range [7, 15]:", rangeSumBST(tree1, 7, 15))  # 32 (7+10+15)

# ================================================================
# BST + HASH SET TEMPLATE
# ================================================================
def bst_with_set(root, target):
    """
    Template for BST traversal with hash set
    
    TC: O(n) - visit each node once
    SC: O(n) - hash set storage
    
    WHEN TO USE:
    - Need to find pairs/relationships between nodes
    - Track seen values or complements
    - Two sum, find duplicates, etc.
    
    KEY INSIGHT:
    - Combine BST traversal with O(1) hash set lookups
    - Store complements or values as you traverse
    - Check set before adding to find relationships
    """
    seen = set()
    
    def dfs(node):
        if not node:
            return False
        
        # Check if current node completes condition
        if node.val in seen:
            return True
        
        # Add complement to set
        seen.add(target - node.val)
        
        # Continue traversal
        return dfs(node.left) or dfs(node.right)
    
    return dfs(root)

# ================================================================
# BST INSERT TEMPLATE
# ================================================================
def bst_insert(root, val):
    """
    Template for inserting into BST
    
    TC: O(h) where h = height
    SC: O(h) for recursive, O(1) for iterative
    
    WHEN TO USE:
    - Need to add new node to BST
    - Build BST from array
    - Maintain BST property during insertion
    
    KEY INSIGHT:
    - Use search logic to find insertion position
    - Always insert as leaf node
    - Recursive: return new/updated node at each level
    """
    if not root:
        return TreeNode(val)
    
    if val < root.val:
        root.left = bst_insert(root.left, val)
    elif val > root.val:
        root.right = bst_insert(root.right, val)
    
    return root

"""
COMPLEXITY QUICK REFERENCE
==========================

BST Operation Complexities:
- Search: O(h) where h = height
- Insert: O(h)
- Delete: O(h)
- In-order Traversal: O(n)
- Range Query: O(k + h) where k = nodes in range

Height Analysis:
- Balanced BST: h = O(log n)
- Skewed BST (worst case): h = O(n)
- Average case: h = O(log n)

Space Complexities:
- Recursive operations: O(h) for call stack
- Iterative operations: O(1) typically
- Traversal with result: O(n) for output

Pattern Complexities:
1. BST Search: O(h) time, O(h) or O(1) space
2. In-order Traversal: O(n) time, O(n) space
3. Validation: O(n) time, O(h) space
4. Range Query: O(k + h) time, O(h) space
5. BST + Hash: O(n) time, O(n) space
6. Construction: O(n log n) average, O(n²) worst

When to Use Each Pattern:
1. BST Search: Finding values, navigating tree
2. In-order: Need sorted sequence, adjacent comparisons
3. Validation: Check BST property, enforce constraints
4. Range Query: Process subset of nodes, optimize with pruning
5. BST + Hash: Find pairs, relationships, frequencies
6. Construction: Build from sorted array, convert structures
"""

# Test tree for templates
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

print("Search for 4:", bst_search(root, 4))
print("In-order:", inorder_traversal(root))
print("Is valid BST:", validate_bst(root))
print("Range sum [3,6]:", range_query(root, 3, 6))
print("Two sum (target 9):", bst_with_set(root, 9))

"""
BST PATTERNS
============
"""

# ================================================================
# PATTERN 1: BST SEARCH/NAVIGATION
# PATTERN EXPLANATION: Navigate BST using the fundamental property that left < root < right.
# At each node, compare target with current value to decide which subtree to explore. This
# eliminates half the remaining nodes at each step, giving logarithmic time in balanced trees.
# Used for finding values, insertion points, or navigating based on value comparisons.
#
# TYPICAL STEPS:
# 1. Check if current node is null (base case)
# 2. Compare target with current node value
# 3. If equal, found target
# 4. If less, recurse/iterate left
# 5. If greater, recurse/iterate right
# 6. Return result (node, boolean, or position)
#
# Applications: Search, find insertion point, find successor/predecessor, navigate to value.
# ================================================================

class BSTSearch:
    """
    Problem: Given the root of a binary search tree and an integer val, find the node
    in the BST that the node's value equals val and return the subtree rooted with that node.
    If such node doesn't exist, return null.
    
    TC: O(h) where h = height (log n average, n worst case for skewed tree)
    SC: O(h) for recursive call stack, O(1) for iterative
    
    How it works:
    1. Use BST property: left < root < right
    2. Compare target with current node to decide direction
    3. Recursively search left if target smaller, right if larger
    4. Return node when found or null if doesn't exist
    """
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]: # LC 700
        # Recursive approach
        if not root:
            return None
        
        if root.val == val:
            return root
        elif val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)
    
    def searchBST_iterative(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Iterative approach - saves space
        while root:
            if root.val == val:
                return root
            elif val < root.val:
                root = root.left
            else:
                root = root.right
        return None

# Example:
#                  4
#                 / \
#                2   7
#               / \
#              1   3
#
# Search for 2:
# - Start at 4: 2 < 4, go left
# - At node 2: 2 == 2, found!
# Return subtree rooted at 2: [2,1,3]
#
# Search for 5:
# - Start at 4: 5 > 4, go right
# - At node 7: 5 < 7, go left
# - Reach null, return null
# Output: null

sol = BSTSearch()
test_root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
print("Search for 2:", sol.searchBST(test_root, 2))  # [2,1,3]
print("Search for 5:", sol.searchBST(test_root, 5))  # None


# ================================================================
# PATTERN 2: IN-ORDER TRAVERSAL (SORTED SEQUENCE)
# PATTERN EXPLANATION: In-order traversal (Left-Root-Right) of a BST always produces
# values in sorted ascending order. This is the most important BST property for solving
# problems. Use it when you need sorted data, need to find kth smallest, compare adjacent
# values, or validate ordering. Can track previous node to compare adjacent elements.
#
# TYPICAL STEPS:
# 1. Traverse left subtree completely (smallest values)
# 2. Process current node (add to result, compare with previous, etc.)
# 3. Traverse right subtree completely (largest values)
# 4. Result is in sorted order
#
# Applications: Get sorted array, kth smallest, validate ordering, find pairs, mode.
# ================================================================

class InOrderPattern:
    """
    Problem: Given the root of a Binary Search Tree, return the minimum difference
    between the values of any two different nodes in the tree.
    
    TC: O(n) - visit each node once in in-order traversal
    SC: O(n) for storing values + O(h) for recursion stack
    
    How it works:
    1. Perform in-order traversal to get sorted sequence
    2. In sorted sequence, minimum difference must be between adjacent elements
    3. Compare each adjacent pair to find minimum difference
    4. Return minimum difference found
    """
    def minDiffInBST(self, root: Optional[TreeNode]) -> int: # LC 783
        values = []
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            values.append(node.val)
            inorder(node.right)
        
        inorder(root)
        
        # Find minimum difference between adjacent values
        min_diff = float('inf')
        for i in range(1, len(values)):
            min_diff = min(min_diff, values[i] - values[i-1])
        
        return min_diff
    
    def minDiffInBST_optimized(self, root: Optional[TreeNode]) -> int:
        """
        Space-optimized version: track only previous value
        SC: O(h) - only recursion stack, no array
        """
        self.min_diff = float('inf')
        self.prev = None
        
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            
            # Process current node
            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val
            
            inorder(node.right)
        
        inorder(root)
        return self.min_diff

# Example:
#               4
#              / \
#             2   6
#            / \
#           1   3
#
# In-order traversal: [1, 2, 3, 4, 6]
#
# Compare adjacent values:
# 2 - 1 = 1
# 3 - 2 = 1
# 4 - 3 = 1
# 6 - 4 = 2
#
# Minimum difference = 1
# Output: 1

sol = InOrderPattern()
test_root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
print("Min difference:", sol.minDiffInBST(test_root))  # 1
print("Min difference (optimized):", sol.minDiffInBST_optimized(test_root))  # 1


# ================================================================
# PATTERN 3: VALIDATION WITH BOUNDS
# PATTERN EXPLANATION: Validate BST property by tracking min and max bounds for each node.
# As you traverse, tighten bounds: when going left, parent value becomes upper bound;
# when going right, parent value becomes lower bound. Each node must stay within its
# inherited bounds. This pattern extends beyond validation to any problem needing to
# enforce value constraints based on ancestors.
#
# TYPICAL STEPS:
# 1. Start with bounds (-inf, +inf)
# 2. For each node, check if value within current bounds
# 3. When recursing left, update upper bound to current value
# 4. When recursing right, update lower bound to current value
# 5. Return false if any node violates its bounds
#
# Applications: Validate BST, count valid nodes, enforce constraints, range validation.
# ================================================================

class ValidationPattern:
    """
    Problem: Given the root of a binary tree, determine if it is a valid binary search tree.
    
    A valid BST is defined as follows:
    - The left subtree of a node contains only nodes with keys less than the node's key
    - The right subtree contains only nodes with keys greater than the node's key
    - Both left and right subtrees must also be binary search trees
    
    TC: O(n) - visit each node once
    SC: O(h) - recursion stack depth
    
    How it works:
    1. Each node must be within bounds set by ancestors
    2. Initially, root can be any value (-inf to +inf)
    3. Going left: upper bound becomes parent value (all values must be < parent)
    4. Going right: lower bound becomes parent value (all values must be > parent)
    5. Any node outside its bounds means invalid BST
    """
    def isValidBST(self, root: Optional[TreeNode]) -> bool: # LC 98
        def validate(node, min_val, max_val):
            if not node:
                return True
            
            # Check if current node violates bounds
            if node.val <= min_val or node.val >= max_val:
                return False
            
            # Check left subtree: upper bound becomes current value
            # Check right subtree: lower bound becomes current value
            return (validate(node.left, min_val, node.val) and
                    validate(node.right, node.val, max_val))
        
        return validate(root, float('-inf'), float('inf'))

# Example 1: Valid BST
#       2
#      / \
#     1   3
#
# Node 2: bounds (-inf, +inf), 2 is valid
# Node 1: bounds (-inf, 2), 1 is valid
# Node 3: bounds (2, +inf), 3 is valid
# Output: True
#
# Example 2: Invalid BST
#       5
#      / \
#     1   4
#        / \
#       3   6
#
# Node 5: bounds (-inf, +inf), 5 is valid
# Node 1: bounds (-inf, 5), 1 is valid
# Node 4: bounds (5, +inf), 4 is NOT valid! (4 < 5)
# Output: False
#
# Key: Node 4 violates BST property because it's in right subtree
# of 5 but 4 < 5

sol = ValidationPattern()
valid_tree = TreeNode(2, TreeNode(1), TreeNode(3))
invalid_tree = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
print("Valid BST:", sol.isValidBST(valid_tree))  # True
print("Invalid BST:", sol.isValidBST(invalid_tree))  # False


# ================================================================
# PATTERN 4: RANGE QUERIES (BOUNDS PRUNING)
# PATTERN EXPLANATION: Use BST property to efficiently process only nodes within a
# target range by pruning entire subtrees. If current node is below range minimum, skip
# left subtree (all smaller). If above range maximum, skip right subtree (all larger).
# Only explore both subtrees when current node is within range. This dramatically reduces
# nodes visited compared to checking every node.
#
# TYPICAL STEPS:
# 1. Check if current node is null (base case)
# 2. If node.val < low: skip left subtree, only search right
# 3. If node.val > high: skip right subtree, only search left
# 4. If low <= node.val <= high: process node and search both subtrees
# 5. Combine results from valid nodes
#
# Applications: Range sum, range count, range search, delete in range, collect range values.
# ================================================================

class RangeQueryPattern:
    """
    Problem: Given the root of a binary search tree and two integers low and high,
    return the sum of values of all nodes with a value in the inclusive range [low, high].
    
    TC: O(k + h) where k = nodes in range, h = height
        - Visit only nodes in range (k) plus path nodes (h)
        - Much better than O(n) when range is small
    SC: O(h) - recursion stack
    
    How it works:
    1. Use BST property to prune search space
    2. If node < low: entire left subtree is too small, skip it
    3. If node > high: entire right subtree is too large, skip it
    4. If in range: include node and check both subtrees
    5. Only traverse paths that might contain valid nodes
    """
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int: # LC 938
        if not root:
            return 0
        
        if root.val < low:
            # Current node too small, left subtree even smaller
            # Only search right subtree
            return self.rangeSumBST(root.right, low, high)
        
        elif root.val > high:
            # Current node too large, right subtree even larger
            # Only search left subtree
            return self.rangeSumBST(root.left, low, high)
        
        else:
            # Current node in range [low, high]
            # Include it and check both subtrees
            return (root.val + 
                    self.rangeSumBST(root.left, low, high) + 
                    self.rangeSumBST(root.right, low, high))

# Example:
#                   10
#                  /  \
#                 5    15
#                / \     \
#               3   7    18
#
# Range: [7, 15]
#
# Node 10: in range, check both sides
#   Left (5): 5 < 7, skip left subtree, check right
#     Node 7: in range, include (7), check both
#       No children, return 7
#   Right (15): in range, include (15), check both
#     Right (18): 18 > 15, skip right subtree, check left
#       No left child, return 0
#
# Total: 7 + 10 + 15 = 32
# Nodes pruned: 3 (too small), 18's right subtree (too large)
# Output: 32

sol = RangeQueryPattern()
test_root = TreeNode(10,
    TreeNode(5, TreeNode(3), TreeNode(7)),
    TreeNode(15, None, TreeNode(18)))
print("Range sum [7, 15]:", sol.rangeSumBST(test_root, 7, 15))  # 32
print("Range sum [6, 10]:", sol.rangeSumBST(test_root, 6, 10))  # 22


# ================================================================
# PATTERN 5: BST + HASH SET (RELATIONSHIPS)
# PATTERN EXPLANATION: Combine BST traversal with hash set to find relationships between
# nodes. As you traverse, check if current node completes a condition (using set), then
# store information for future nodes. Common for two sum problems, finding pairs, tracking
# frequencies, or detecting duplicates. Hash set provides O(1) lookups while BST provides
# systematic traversal.
#
# TYPICAL STEPS:
# 1. Initialize empty hash set
# 2. Traverse BST (any order, often in-order)
# 3. For each node, check if it completes condition (node.val in set)
# 4. Store complement or value in set for future nodes
# 5. Return when condition met or after full traversal
#
# Applications: Two sum, find pairs, detect duplicates, find mode, track frequencies.
# ================================================================

class BSTHashPattern:
    """
    Problem: Given the root of a Binary Search Tree and a target number k, return true
    if there exist two elements in the BST such that their sum is equal to the given target.
    
    TC: O(n) - visit each node once
    SC: O(n) - hash set stores up to n complements
    
    How it works:
    1. Traverse BST (in-order, pre-order, or post-order all work)
    2. For each node, check if its complement (k - node.val) exists in set
    3. If yes, we found a pair that sums to k
    4. If no, add complement to set for future nodes
    5. Continue until pair found or tree fully traversed
    """
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool: # LC 653
        complements = set()
        
        def dfs(node):
            if not node:
                return False
            
            # Check if current node's complement exists
            if node.val in complements:
                return True
            
            # Store complement for future nodes
            complements.add(k - node.val)
            
            # Continue searching both subtrees
            return dfs(node.left) or dfs(node.right)
        
        return dfs(root)

# Example:
#                  5
#                 / \
#                3   6
#               / \   \
#              2   4   7
#
# Target k = 9
#
# Visit 2: complement = 9-2 = 7, add 7 to set, set = {7}
# Visit 3: complement = 9-3 = 6, add 6 to set, set = {7, 6}
# Visit 4: complement = 9-4 = 5, add 5 to set, set = {7, 6, 5}
# Visit 5: complement = 9-5 = 4, add 4 to set, set = {7, 6, 5, 4}
# Visit 6: 6 is in set! Found pair (3, 6)
# Output: True
#
# The pair (3, 6) sums to 9

sol = BSTHashPattern()
test_root = TreeNode(5,
    TreeNode(3, TreeNode(2), TreeNode(4)),
    TreeNode(6, None, TreeNode(7)))
print("Two sum exists (k=9):", sol.findTarget(test_root, 9))  # True
print("Two sum exists (k=28):", sol.findTarget(test_root, 28))  # False


# ================================================================
# PATTERN 6: BST CONSTRUCTION/CONVERSION
# PATTERN EXPLANATION: Build BST from sorted array or convert BST to other structures.
# For building from sorted array, use middle element as root to maintain balance, then
# recursively build left and right subtrees. This creates height-balanced BST with
# O(log n) height. For conversions, traverse in desired order and construct new structure.
#
# TYPICAL STEPS (Build from Sorted Array):
# 1. Find middle element of current range (becomes root)
# 2. Recursively build left subtree from left half
# 3. Recursively build right subtree from right half
# 4. Connect subtrees to root
# 5. Return root
#
# Applications: Convert sorted array to BST, flatten BST, serialize/deserialize, rebalance.
# ================================================================

class BSTConstructionPattern:
    """
    Problem: Given an integer array nums where the elements are sorted in ascending order,
    convert it to a height-balanced binary search tree.
    
    A height-balanced BST is a binary tree in which the depth of the two subtrees of every
    node never differs by more than one.
    
    TC: O(n) - create each node once
    SC: O(log n) - recursion stack for balanced tree
    
    How it works:
    1. Choose middle element as root (ensures balance)
    2. Elements before middle go to left subtree
    3. Elements after middle go to right subtree
    4. Recursively build left and right subtrees
    5. This guarantees height = O(log n)
    """
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]: # LC 108
        def buildTree(left, right):
            if left > right:
                return None
            
            # Choose middle element as root for balance
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            
            # Recursively build left and right subtrees
            root.left = buildTree(left, mid - 1)
            root.right = buildTree(mid + 1, right)
            
            return root
        
        return buildTree(0, len(nums) - 1)

# Example:
# nums = [-10, -3, 0, 5, 9]
#
# Step 1: mid = 2, root = 0
#         Left range: [-10, -3]
#         Right range: [5, 9]
#
# Step 2: Build left subtree from [-10, -3]
#         mid = 0, root = -10
#         Right range: [-3]
#         Right child = -3
#
# Step 3: Build right subtree from [5, 9]
#         mid = 3, root = 5
#         Right range: [9]
#         Right child = 9
#
# Final tree:
#         0
#        / \
#      -10  5
#        \   \
#        -3   9
#
# Height = 2 (balanced)
# Output: [0,-10,5,null,-3,null,9]

sol = BSTConstructionPattern()
nums = [-10, -3, 0, 5, 9]
result = sol.sortedArrayToBST(nums)
print("Built BST from sorted array:", inorder_traversal(result))  # [-10,-3,0,5,9]
