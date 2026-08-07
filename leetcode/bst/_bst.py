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

"""
BST COMPLEXITY REFERENCE
=========================

+--------------------------------+----------+----------+
| Pattern                        | Time     | Space    |
+--------------------------------+----------+----------+
| BST Search / Navigation        | O(h)     | O(h)     |
| In-Order Traversal             | O(n)     | O(n)     |
| Validation with Bounds         | O(n)     | O(h)     |
| Range Queries (Bounds Pruning) | O(k + h) | O(h)     |
| BST Construction / Conversion  | O(n)     | O(log n) |
+--------------------------------+----------+----------+

n = number of nodes in the tree, h = height of the tree (log n balanced, n worst
case skewed), k = number of nodes within the query range

WHAT EACH PATTERN IS:
- BST Search / Navigation: walk down the tree comparing the target to each node's
  value, going left or right based on the comparison, the same way you'd narrow down
  a guess in a sorted list.
- In-Order Traversal: visit every node left-then-root-then-right so the values come
  out in sorted order for free, without a separate sorting step.
- Validation with Bounds: check that every node's value still falls inside an allowed
  low/high range that gets tightened as you move down toward each child.
- Range Queries (Bounds Pruning): walk the tree but skip entire branches that are
  already known to be too small or too large to contain any values in the target range.
- BST Construction / Conversion: build a balanced tree from a sorted list by always
  picking the middle element as the current root and repeating the process on the two
  halves.

NOTES:
- BST Search / Navigation: each comparison rules out one whole subtree -> O(h);
  recursion stack costs O(h), iterative version costs O(1)
- In-Order Traversal: every node is visited exactly once with no pruning possible ->
  O(n); storing values costs O(n), recursion depth adds O(h)
- Validation with Bounds: every node is visited once to check its inherited bounds ->
  O(n); recursion stack depth is O(h)
- Range Queries: nodes outside [low, high] are pruned entirely, so only the k
  in-range nodes plus the O(h) path to reach them are visited -> O(k + h)
- BST Construction / Conversion: one node created per array element -> O(n); picking
  the middle each time keeps the tree balanced, so recursion depth is O(log n)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ================================================================
# BST SEARCH TEMPLATE - RECURSIVE & ITERATIVE
# ================================================================
def bst_search(root, target):
    """
    Template for searching in BST using BST property
    
    TC: O(h) where h = height of tree (log n average, n worst case for skewed tree) -> eliminate half of the search space each iteration
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
    curr = root

    while curr:
        if curr.val == target:
            return curr
        elif target < curr.val:
            curr = curr.left
        else:
            curr = curr.right
    return None

# ================================================================
# BST INSERT TEMPLATE
# ================================================================
def bst_insert(root, val):
    """
    Template for inserting into BST
    
    TC: O(h) where h = height, O(n) worst case
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
    if not root: # We hit leaf node
        return TreeNode(val) # Create node w/ val & assign to parent
    
    if val < root.val:
        root.left = bst_insert(root.left, val)
    elif val > root.val:
        root.right = bst_insert(root.right, val)
    
    return root

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

print("Search for 4:", bst_search(root, 4)) # Recursive
print("Search for 4:", bst_search_iterative(root, 4)) # Iterative
print("Insert 1:", bst_insert(root, 1))

# ================================================================
# BST DELETE TEMPLATE
# ================================================================
def bst_delete(root, key):
    """
    Template for deleting from BST
    
    TC: O(h) where h = height
    SC: O(h) for recursive call stack
    
    THREE CASES:
    1. Leaf node → just remove
    2. One child → replace with child
    3. Two children → replace with in-order successor, delete successor
        - In Order Successor: next node in sorted order/the smallest value greater than the current node
        - How to Find: Go right, then go left as far as possible
    
    KEY INSIGHT:
    - Use search to find node, then handle based on children
    - In-order successor = smallest in right subtree (leftmost)
    """
    if not root: # Edge cases -> empty tree or key not found
        return None
    
    # Search for node
    if key < root.val:
        root.left = bst_delete(root.left, key)
    elif key > root.val:
        root.right = bst_delete(root.right, key)
    else: # key == curr node
        # Found node to delete
        if not root.left and not root.right:  # Case 1: leaf node returns None
            return None
        if not root.left:      # Case 1 -> Assigns root.right None to caller
            return root.right  # Case 2: No left child -> root.right assigned to caller
        if not root.right:     # Case 2: No right child -> root.left assigned to caller
            return root.left   
        
        # Case 3: two children - find in-order successor
        successor = root.right    # Go right
        while successor.left:     # Go left as far as possible
            successor = successor.left
        root.val = successor.val  # Copy successor value to curr node
        root.right = bst_delete(root.right, successor.val)  # Delete successor node
    
    return root

# Example:
#         5                   5                   5                     5                   7
#       /   \               /   \               /   \                 /   \                /
#      /     \    delete   /     \    delete   /     \     delete    /     \    delete    /   
#     3       6    (2)    3       6    (3)    4       6     (6)     4       7    (5)     4   
#    / \     /      →      \     /      →            /       →                     →
#   2   4   7               4   7                   7
#
# Delete 2: leaf node, just remove
# Delete 3: has one child (4), replace with child
# Delete 5: has two children, replace with successor (6)

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)

print("Delete 2:", bst_delete(root, 2)) # Case 1 -> leaf node
print("Delete 3:", bst_delete(root, 3)) # Case 2 -> One child: no left child
print("Delete 7:", bst_delete(root, 6)) # Case 2 -> One child: no right child
print("Delete 5:", bst_delete(root, 5)) # Case 3 -> Two children

"""
BST COMPLEXITY QUICK REFERENCE
==============================

TIME COMPLEXITY:

- O(h) — Search, Insert, Delete
Eliminate half the tree at each step by going left or right.
Balanced: O(log n). Skewed: O(n).

- O(n) — Traversals (in-order, pre-order, post-order)
Must visit every node once, no pruning possible.

- O(k + h) — Range Queries with Pruning
h to reach range boundaries, k to visit all nodes in range.

SPACE COMPLEXITY:

- O(h) — Recursive DFS
Call stack depth equals height of tree.

- O(1) — Iterative approaches
No recursion, just pointer manipulation.

- O(n) — Storing results
Building an array of all node values.

- DEFAULT FOR INTERVIEWS:
Most tree problems: O(n) time, O(h) space
BST with pruning: O(h) time, O(h) space

================================================================
PATTERN 1: BST SEARCH/NAVIGATION

PATTERN EXPLANATION: Navigate BST using the fundamental property that left < root < right. At each node, compare target with current value to decide which subtree to explore. This eliminates half the remaining nodes at each step, giving logarithmic time in balanced trees. Used for finding values, insertion points, or navigating based on value comparisons.
#
Applications: Search, find insertion point, find successor/predecessor, navigate to value.
================================================================
"""

class BSTSearch:
    """
    Problem: Given the root of a binary search tree and an integer "val", find the node
    in the BST that equals "val" and return the subtree rooted with that node. If such node doesn't exist, return null.

    TC: O(h) where h = height (log n average, n worst case for skewed tree)
    SC: O(h) for recursive call stack, O(1) for iterative

    Giveaway: given a binary search tree (not just a "binary tree") and asked to
    find the node equal to val — calling it out as a search tree instead of a plain
    tree is the tell to compare val against root.val and go left/right, rather than
    searching both subtrees like you would in an unordered tree.

    Steps:
    1. If root is null, return None (base case — val not found)
    2. If root.val == val, return root (found the node)
    3. If val < root.val, recurse into the left subtree
    4. If val > root.val, recurse into the right subtree
    """
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]: # LC 700
        # Recursive approach
        if not root:
            return None
        
        if root.val == val:
            return root
        elif val < root.val: # val is less than -> search left
            return self.searchBST(root.left, val)
        else: # val is greater than -> search right
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

"""
================================================================
PATTERN 2: IN-ORDER TRAVERSAL (SORTED SEQUENCE)
PATTERN EXPLANATION: In-order traversal (Left-Root-Right) of a BST always produces
values in sorted ascending order. This is the most important BST property for solving
problems. Use it when you need sorted data, need to find kth smallest, compare adjacent
values, or validate ordering. Can track previous node to compare adjacent elements.
#
Applications: Get sorted array, kth smallest, validate ordering, find pairs, mode.
================================================================
"""

class InOrderPattern:
    """
    Problem: Given the root of a Binary Search Tree, return the minimum difference
    between the values of any two different nodes in the tree.

    TC: O(n) - visit each node once in in-order traversal
    SC: O(n) for storing values + O(h) average for recursion stack

    Giveaway: "minimum difference between the values of any two different nodes"
    in a BST — because in-order traversal of a BST yields sorted values, the true
    minimum difference can only ever occur between two adjacent elements in that
    sorted order, which is what points to an in-order walk instead of comparing
    every pair of nodes.

    Steps:
    1. Run in-order traversal (left → root → right) to collect node values in sorted order
    2. After traversal, the minimum difference must be between adjacent elements in the sorted list
    3. Iterate through adjacent pairs and track the running minimum difference
    4. Return the minimum difference found
    """
    def minDiffInBST(self, root: Optional[TreeNode]) -> int: # LC 783
        values = [] # Sorted BST list
        
        def inorder(node): # In order traversal of BST 
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

"""
================================================================
PATTERN 3: VALIDATION WITH BOUNDS
PATTERN EXPLANATION: Validate BST property by tracking min and max bounds for each node.
As you traverse, tighten bounds: when going left, parent value becomes upper bound;
when going right, parent value becomes lower bound. Each node must stay within its
inherited bounds. This pattern extends beyond validation to any problem needing to
enforce value constraints based on ancestors.
#
Applications: Validate BST, count valid nodes, enforce constraints, range validation.
================================================================
"""

class ValidationPattern:
    """
    Problem: Given the root of a binary tree, determine if it is a valid binary search tree.

    A valid BST is defined as follows:
    - The left subtree of a node contains only nodes with keys less than the node's key
    - The right subtree contains only nodes with keys greater than the node's key
    - Both left and right subtrees must also be binary search trees

    TC: O(n) - visit each node once
    SC: O(h) - recursion stack depth

    Giveaway: "determine if it is a valid binary search tree" — checking a global
    ordering property across the whole tree, not just a node against its immediate
    children, is what signals passing down a shrinking (min, max) bound through the
    recursion instead of only comparing a node to its direct children.

    Steps:
    1. Call validate(root, -inf, +inf) — root is unconstrained initially
    2. At each node, check if node.val is within (min_val, max_val); return False if not
    3. Recurse left: pass current node's value as the new upper bound
    4. Recurse right: pass current node's value as the new lower bound
    5. Return True only if both left and right subtrees are valid
    """
    def isValidBST(self, root: Optional[TreeNode]) -> bool: # LC 98
        def validate(node, min_val, max_val):
            if not node: # Base Case -> return True at end of path
                return True
            
            # Check if current node violates bounds
            if node.val <= min_val or node.val >= max_val:
                return False
            
            # Check left subtree: curr val becomes upper bound
            # Check right subtree: curr val becomes lower bound
            is_valid_left = validate(node.left, min_val, node.val)
            is_valid_right = validate(node.right, node.val, max_val)

            return is_valid_left and is_valid_right
        
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

"""
================================================================
PATTERN 4: RANGE QUERIES (BOUNDS PRUNING)
PATTERN EXPLANATION: Use BST property to efficiently process only nodes within a
target range by pruning entire subtrees. If current node is below range minimum, skip
left subtree (all smaller). If above range maximum, skip right subtree (all larger).
Only explore both subtrees when current node is within range. This dramatically reduces
nodes visited compared to checking every node.
#
Applications: Range sum, range count, range search, delete in range, collect range values.
================================================================
"""

class RangeQueryPattern:
    """
    Problem: Given the root of a binary search tree and two integers low and high,
    return the sum of values of all nodes with a value in the inclusive range [low, high].

    # Example:
    #                   10
    #                  /  \
    #                 5    15
    #                / \     \
    #               3   7    18
    #
    # Range: [7, 15]

    Giveaway: "return the sum of ... all nodes with a value in the inclusive range
    [low, high]" on a search tree — an explicit numeric range combined with the BST
    ordering guarantee is the tell that whole subtrees can be skipped (go right only
    if too small, left only if too large) instead of visiting every node.

    Steps:
    1. If root is null, return 0 (base case)
    2. If root.val < low, prune the left subtree and recurse only right
       a. All nodes to the left are even smaller — none can be in range
    3. If root.val > high, prune the right subtree and recurse only left
       a. All nodes to the right are even larger — none can be in range
    4. If root.val is within [low, high], include root.val and recurse both subtrees
    5. Return root.val + left sum + right sum
    """
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int: # LC 938
        """
        TC: O(k + h) where k = nodes in range, h = height
            - Visit only nodes in range (k)
            - To reach the range boundaries, worst case you traverse down the tree height to a leaf
        SC: O(h) - the deepest the recursion stack goes is the height of the tree
        """
        if not root:
            return 0
        
        if root.val < low: # Curr node too small, prune left subtree 
            return self.rangeSumBST(root.right, low, high) # Search right
        
        elif root.val > high: # Current node too large, prune right subtree
            return self.rangeSumBST(root.left, low, high) # Search left
        
        else: # Current node in range [low, high]
                # Include it and check both subtrees
                left_sum = self.rangeSumBST(root.left, low, high)
                right_sum = self.rangeSumBST(root.right, low, high)
                return root.val + left_sum + right_sum

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

"""
================================================================
PATTERN 5: BST CONSTRUCTION/CONVERSION
PATTERN EXPLANATION: Build BST from sorted array or convert BST to other structures.
For building from sorted array, use middle element as root to maintain balance, then
recursively build left and right subtrees. This creates height-balanced BST with
O(log n) height. For conversions, traverse in desired order and construct new structure.
#
Applications: Convert sorted array to BST, flatten BST, serialize/deserialize, rebalance.
================================================================
"""

class BSTConstructionPattern:
    """
    Problem: Given an integer array nums where the elements are sorted in ascending order,
    convert it to a height-balanced binary search tree.

    A height-balanced BST is a binary tree in which the depth of the two subtrees of every
    node never differs by more than one.

    Giveaway: "elements ... sorted in ascending order, convert it to a
    height-balanced binary search tree" — being told the input is already sorted
    and the output must be height-balanced is what signals recursively picking the
    middle element as root, rather than inserting values one at a time, which can
    skew the tree.

    Steps:
    1. Compute mid = (left + right) // 2 and create a TreeNode with nums[mid] as root
    2. Recursively call buildTree(left, mid - 1) and assign the result to root.left
       a. Elements to the left of mid are all smaller — they form the left subtree
    3. Recursively call buildTree(mid + 1, right) and assign the result to root.right
       a. Elements to the right of mid are all larger — they form the right subtree
    4. Return root so the caller can attach it as a child
    5. Base case: if left > right, return None (empty subarray)
    """
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]: # LC 108
        """  
        - TC: O(n) - create each node once
        - SC: O(log n) - recursion stack for balanced tree
        """
        def buildTree(left, right):
            if left > right:
                return None
            
            # Choose middle element as root for balance
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            
            # Recursively build left and right subtrees
            root.left = buildTree(left, mid - 1)
            root.right = buildTree(mid + 1, right)
            
            return root # return node to prev callstack & attach
        
        return buildTree(0, len(nums) - 1)

# Example:
# nums = [-10, -3, 0, 5, 9]
#
# buildTree(0, 4): mid=2, create node 0
#   │
#   ├── root.left = buildTree(0, 1): mid=0, create node -10
#   │     ├── root.left = buildTree(0, -1): returns None
#   │     └── root.right = buildTree(1, 1): mid=1, create node -3
#   │           ├── root.left = buildTree(1, 0): returns None
#   │           └── root.right = buildTree(2, 1): returns None
#   │           returns node(-3) to caller
#   │     returns node(-10) with right child -3 to caller
#   │
#   └── root.right = buildTree(3, 4): mid=3, create node 5
#         ├── root.left = buildTree(3, 2): returns None
#         └── root.right = buildTree(4, 4): mid=4, create node 9
#               ├── root.left = buildTree(4, 3): returns None
#               └── root.right = buildTree(5, 4): returns None
#               returns node(9) to caller
#         returns node(5) with right child 9 to caller
#
# returns node(0) with left child -10, right child 5
#
# Final tree:
#         0
#        / \
#      -10  5
#        \   \
#        -3   9

sol = BSTConstructionPattern()
nums = [-10, -3, 0, 5, 9]
print(sol.sortedArrayToBST(nums))
