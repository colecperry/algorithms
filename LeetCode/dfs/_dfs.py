"""
=================================================================
DEPTH-FIRST SEARCH (DFS) COMPLETE GUIDE
=================================================================

WHAT IS DFS?
-----------
Depth-First Search (DFS) explores as far as possible along each branch before backtracking. It "goes deep" before going wide.

Key characteristics:
- Uses a STACK (LIFO - Last In, First Out) or recursion
- Explores one complete path before trying another
- Time: O(n) for trees, O(V + E) for graphs
- Space: O(h) where h is height/depth

WHEN TO USE DFS
---------------
1. PATH PROBLEMS: Finding paths, detecting cycles, backtracking (permutations, combinations, N-Queens)
2. TREE TRAVERSALS: Preorder/inorder/postorder, tree validation, path sums
3. EXHAUSTIVE SEARCH: Generate all subsets, word search, Sudoku solver
4. CONNECTED COMPONENTS: Count islands, check reachability, graph validation

COMMON PATTERNS:
- "Find all possible..." → DFS with backtracking
- "Does a path exist..." → DFS with early return
- "Traverse the tree..." → DFS traversal
- "Count paths/islands..." → DFS with counter

DFS vs BFS: Use DFS for exploring ALL paths or going DEEP. Use BFS for SHORTEST path or LEVEL-BY-LEVEL.

DFS CORE TEMPLATES
==================
"""

# ================================================================
# RECURSIVE DFS TEMPLATE - TREES
# ================================================================
class TreeNode(object):
    '''
    Calculate max depth of a binary tree - showcases fundamental DFS structure for trees
    '''
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs_recursive_template(node):
    # Base case - when to stop recursion
    if not node:
        return 0
    
    # Process current node (pre-order processing)
    print(f"Processing node with value: {node.val}")  # Example: print node value
    
    # Recursive calls to explore children/neighbors
    left_result = dfs_recursive_template(node.left)
    right_result = dfs_recursive_template(node.right)
    
    # Combine results and return (post-order processing) to prev callstack
    return 1 + max(left_result, right_result)

#         3
#        / \
#       /   \
#      9    20
#          /  \
#        15    7

# Test the recursive DFS template
template_root = TreeNode(3)
template_root.left = TreeNode(9)
template_root.right = TreeNode(20)
template_root.right.left = TreeNode(15)
template_root.right.right = TreeNode(7)

print("Recursive DFS Template (Tree Height):", dfs_recursive_template(template_root))  # Output: 3

# ================================================================
# ITERATIVE DFS TEMPLATE
# ================================================================
def dfs_iterative_template(root):
    '''
    Perform a pre order traversal of a binary tree using an iterative stack: Node, Left, Right
    '''
    if not root: # Edge case: empty tree
        return []
    
    stack = [root] # DFS stack initalization
    result = []
    
    # MAIN DFS LOOP: 
    while stack:
        # Get the next node
        node = stack.pop() 
        
        # Process current node
        result.append(node.val)
        
        # Add children (right then left ensures correct processing as we would pop the left side first) 
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return result

#         3
#        / \
#       /   \
#      9    20
#          /  \
#        15    7

print("Iterative DFS Template:", dfs_iterative_template(template_root)) # [3,9,20,15,7] 

# ================================================================
# MATRIX DFS TEMPLATE
# ================================================================

def matrix_dfs_template(matrix, start_row, start_col):
    """
    Matrix DFS template with visited tracking
    
    EXPLORATION PATTERN: DFS explores in "deep dive" paths
    - Picks one direction and goes as far as possible before backtracking
    - Like following a single hallway to its end, then returning to try other hallways
    - Path might be: (0,0) → (0,1) → (0,2) → (1,2) → (2,2) → backtrack → try new path
    - Does NOT guarantee shortest path, but explores all reachable cells
    
    TC: O(rows * cols) - each cell visited at most once
    SC: O(rows * cols) - visited set + stack can grow to this size
    """
    # Edge case: empty matrix
    if not matrix or not matrix[0]:
        return []
    
    rows, cols = len(matrix), len(matrix[0])
    stack = [(start_row, start_col)] # DFS uses a stack (.pop())
    visited = set([(start_row, start_col)])
    result = []
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
    
    while stack:
        row, col = stack.pop() # <- DFS line pops from end and explores newest first (LIFO)
        
        # Process current cell
        result.append(matrix[row][col])
        
        # Add valid neighbors
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < rows and 
                0 <= new_col < cols and 
                (new_row, new_col) not in visited):
                
                visited.add((new_row, new_col))
                stack.append((new_row, new_col))  # Add to END (will be processed next - creates depth)
    
    return result

# Test matrix
test_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Run the function
print("Matrix DFS from (0,0):", matrix_dfs_template(test_matrix, 0, 0))

"""
DFS VARIANTS & WHEN TO USE
===========================

1. TREE-BASED DFS:
   - Binary trees, N-ary trees
   - No cycle detection needed
   - Examples: traversals, path problems, tree modifications

2. MATRIX-BASED DFS:
   - 2D grids treated as implicit graphs
   - Each cell connects to adjacent cells
   - Examples: island problems, path finding, flood fill

WHEN TO USE DFS VS BFS:
- Use DFS when you need to explore all paths or find ANY solution
- Use DFS for tree traversals, backtracking problems
- Use BFS for shortest path problems, level-by-level processing
- DFS uses less memory for sparse graphs, BFS better for dense graphs

COMMON LEETCODE PATTERNS
========================
"""

# ================================================================
# PATTERN 1: SYSTEMATIC NODE VISITATION
# PATTERN EXPLANATION: Visit every node in a tree following a predetermined order.
# Key insight: Choose traversal order based on when you need to process data.
# Applications: Data collection, validation, transformation, serialization.
# ================================================================

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class InorderTraversal:
    # RECURSIVE SOLUTION 
    def inorderTraversal(self, root): # LC 94 - Binary Tree Inorder Traversal
        """
        Pattern: Tree traversal with result collection
        Time: O(n), Space: O(h) where h is height
        
        How it works:
        1. Base case: if node is None, return (end of branch)
        2. Recurse left subtree completely
        3. Process current node (add to result)
        4. Recurse right subtree completely
        """
        res = []
        
        def dfs(root):
            if root is None:  # Base case - hit end 
                return
            dfs(root.left)    # Keep going left until base case
            res.append(root.val)  # Process root
            dfs(root.right)   # Go right
        
        dfs(root)
        return res
    
        #           1
        #         /   \
        #        /     \
        #       2       3
        #      / \       \
        #     4   5       8
        #        / \     /
        #       6   7   9
    
    # ITERATIVE SOLUTION
    def inorderTraversalIterative(self, root):
        """
        Pattern: Controlled traversal with stack
        Key insight: Go left as much as possible, then process and go right
        
        How it works:
        1. Push all left nodes to stack while going left
        2. When can't go left anymore, pop and process node
        3. Move to right child and repeat
        """
        res = []
        stack = [] # Store nodes we need to return to after exploring left subtrees
        curr = root # Current node we are exploring
        
        while curr or stack: # Continue while we have a current node or nodes to explore
            # Step 1: Go left as far as possible
            while curr:
                stack.append(curr) # Save node for later processing
                curr = curr.left
            
            # Step 2: Once we can't go any further, process deepest left node
            curr = stack.pop() # Go back to last unprocessed node (end of stack)
            res.append(curr.val) # Append node (follows in order principle)
            
            # Step 3: Move to right subtree and continue traversal
            curr = curr.right
        
        return res

    #           1
    #         /   \
    #        /     \
    #       2       3
    #      / \       \
    #     4   5       8
    #        / \     /
    #       6   7   9

# Test the inorder traversal
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(6), TreeNode(7))), TreeNode(3, None, TreeNode(8, TreeNode(9), None)))

solution = InorderTraversal()
print("Recursive inorder:", solution.inorderTraversal(root))  # [4,2,6,5,7,1,3,9,8]
print("Iterative inorder:", solution.inorderTraversalIterative(root))  # [4,2,6,5,7,1,3,9,8]

# ================================================================
# PATTERN 2: SIMULTANEOUS DUAL TRAVERSAL
# PATTERN EXPLANATION: This pattern traverses two parts of a tree (or two trees) 
# simultaneously to compare their structure, values, or relationships.
# Key insight: Instead of traversing once and storing results, traverse both 
# sides at the same time making comparisons at each step.
# Applications: Tree symmetry, tree equality, subtree matching, mirror validation.
# ================================================================

# RECURSIVE SOLUTION
def isSymmetric(root): # LC 101
    """
    Problem: Given the root of a binary tree, check whether it is a mirror of itself
    
    How it works:
    1. Helper function compares two nodes for symmetry
    2. Base cases: both null (symmetric), one null (not symmetric), different values (not symmetric)
    3. For symmetry: values must match AND subtrees must be mirrors
    4. Mirror check: left.left vs right.right, left.right vs right.left
    """
    def dfs(left, right):
        if not left and not right: # Both null -> Symmetric
            return True
        if not left or not right: # One node null -> Not symmetric
            return False
        if left.val != right.val: # Nodes have diff vals -> Not symmetric
            return False
        
        # Mirror comparison: left.left with right.right, left.right with right.left
        return (dfs(left.left, right.right) and 
                dfs(left.right, right.left))
    
    return dfs(root.left, root.right) if root else True # Pass in child nodes to start fn call if not empty tree, if empty Tree return True (empty tree is symmetric)

#               1                  1
#              / \                / \
#             /   \              /   \
#            2     2            2     2
#           / \   / \            \     \
#          3   4 4   3            3     3

# ITERATIVE SOLUTION
def isSymmetricIterative(root):
    """
    Pattern: Mirror node pairs in stack
    
    How it works:
    1. Stack stores pairs of nodes that should be mirrors
    2. For each pair, verify they match for symmetry
    3. Add their mirror children pairs to stack
    """
    if not root: # Base Case -> empty Tree is symmetric
        return True
    
    stack = [(root.left, root.right)] # Iterative stack starts at root's l and r subtrees
    
    while stack:
        left, right = stack.pop() # Pop the pair of nodes 
        
        if not left and not right: # Both null -> Symmetric 
            continue # do not add children
        if not left or not right: # One node null -> Not symmetric
            return False # Return False immediately
        if left.val != right.val: # Nodes have diff vals -> Not symmetric
            return False # Return False immediately
        
        # Add mirror pairs to continue search
        stack.append((left.left, right.right))
        stack.append((left.right, right.left))
    
    return True # Return True if we explore all nodes and no pairs are asymmetric

#               1                  1
#              / \                / \
#             /   \              /   \
#            2     2            2     2
#           / \   / \            \     \
#          3   4 4   3            3     3

# Symmetric tree
symmetric_root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))

# Asymmetric tree  
asymmetric_root = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))

print("Symmetric tree (recursive):", isSymmetric(symmetric_root))  # True
print("Asymmetric tree (recursive):", isSymmetric(asymmetric_root))  # False
print("Symmetric tree (iterative):", isSymmetricIterative(symmetric_root))  # True
print("Asymmetric tree (iterative):", isSymmetricIterative(asymmetric_root))  # False

# ================================================================
# PATTERN 3: ACCUMULATIVE PATH TRACKING
# PATTERN EXPLANATION: Track running values while traversing paths to meet conditions.
# Key insight: Update target/sum at each node and check condition at path endpoints.
# Applications: Path sum validation, counting paths, finding target sequences.
# ================================================================

# RECURSIVE SOLUTION
def hasPathSum(root, targetSum): # LC 112 - Path Sum
    """
    # Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
    """
    if not root: # Edge case for null tree -> cannot rearch target 
        return False
    
    # Base Case -> Found a leaf node
    if not root.left and not root.right:
        return targetSum == root.val # Check if we reached our target
    
    # Recursive calls with updated sum for children
    remaining = targetSum - root.val # Update sum we are looking for
    return (hasPathSum(root.left, remaining) or 
            hasPathSum(root.right, remaining)) # If any point we return True, no need to check second part -> True propogates up the call stack

# Ex. 1 - target = 22
#
#               5 x
#              / \
#             /   \
#            4 x   8
#           /     / \
#          /     /   \
#         11 x  13    4
#        /  \          \
#       7    2 x        1

# ITERATIVE SOLUTION
def hasPathSumIterative(root, targetSum):
    if not root: # Edge case null tree
        return False
    
    stack = [(root, targetSum)] # Iterative DFS stack
    
    while stack:
        node, curr_sum = stack.pop() # Pop the node and check the needed sum
        remaining = curr_sum - node.val # Update remaining sum for children
        
        # Check leaf node
        if not node.left and not node.right and remaining == 0:
            return True
        
        # Add children with updated sum -> adding R first follows DFS property
        if node.right:
            stack.append((node.right, remaining))
        if node.left:
            stack.append((node.left, remaining))
    
    return False

# Ex. 1 - target = 22
#
#               5 x
#              / \
#             /   \
#            4 x   8
#           /     / \
#          /     /   \
#         11 x  13    4
#        /  \          \
#       7    2 x        1

# Test path sum
path_root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)), None), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))

print("Has path sum 22 (recursive):", hasPathSum(path_root, 22))  # True
print("Has path sum 22 (iterative):", hasPathSumIterative(path_root, 22))  # True

# ================================================================
# PATTERN 4: STRUCTURAL TRANSFORMATION
# PATTERN EXPLANATION: Modify tree structure or node values during traversal.
# Key insight: Timing of changes matters - modify before recursion or after based on needs.
# Applications: Tree inversion, flattening, value updates, structural rebuilding.
# ================================================================

# RECURSIVE SOLUTION
def invertTree(root): # LC 226 - Invert Binary Tree
    """
    # Given the root of a binary tree, invert the tree, and return its root.
    Time: O(n), Space: O(h)
    
    How it works:
    1. Base case: null node needs no inversion
    2. Swap current node's children
    3. Recursively invert both subtrees
    4. Return modified root
    """
    if not root: # Base case -> reach end of tree path
        return None # Edge case -> empty tree
    
    # Swap children
    root.left, root.right = root.right, root.left
    
    # Recursively invert subtrees
    invertTree(root.left)
    invertTree(root.right)
    
    return root # Return modified root of each recursive call back to caller (parent) and return the tree of the original root with it's updated subtrees
#
#               4                    4
#              / \                  / \
#             /   \                /   \
#            2     7      ->      7     2
#           / \   / \            / \   / \
#          1   3 6   9          9   6 3   1

# ITERATIVE SOLUTION
def invertTreeIterative(root):
    if not root: # Empty Tree
        return None
    
    stack = [root] # Iterative DFS stack
    
    while stack:
        node = stack.pop()
        
        # Swap children
        node.left, node.right = node.right, node.left
        
        # Add children to stack to swap their subtrees later
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    
    return root

#
#               4                    4
#              / \                  / \
#             /   \                /   \
#            2     7      ->      7     2
#           / \   / \            / \   / \
#          1   3 6   9          9   6 3   1

invert_root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))


print(invertTree(invert_root))
print(invertTreeIterative(invert_root))


# ================================================================
# PATTERN 5: BOTTOM-UP INFORMATION PROPAGATION
# PATTERN EXPLANATION: Gather info from children and propagate it up to parents.
# Key insight: Child results determine parent behavior - process children first, then parent.
# Applications: LCA finding, tree validation, height calculation, subtree properties.
# ================================================================

# RECURSIVE SOLUTION 
def lowestCommonAncestor(root, p, q): # LC 236
    """
    # Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree. The lowest common ancestor is defined between two nodes p and q as the lowest node (lowest depth on tree) in T that has both p and q as descendants (where we allow a node to be a descendant of itself).
    """
    if not root: # Base Case: Reached end of path OR empty tree
        return None # No node found in this direction
    
    if root == p or root == q: # If we find p or q
        return root # Return that node to the caller (parent)
    
    # DFS: # If we do not find p or q, 
    l = lowestCommonAncestor(root.left, p, q) # Child reports back
    r = lowestCommonAncestor(root.right, p, q) # a target node or nothing

    if l and r: # Case 1: p & q on opposite sides of subtree
        return root # current node we are at is the LCA
    else: # Case 2: only p or q returns a target
        return l or r # Return whatever was found (target node/ LCA from subtree or None if we reach the end of path or target not found in this subtree)

#                3                  
#              /   \             
#             /     \
#            /       \
#           5         1
#          / \       / \
#         /   \     /   \
#        6     2   0     8
#             / \ 
#            7   4
#
#      ex.1  p = 5, q = 1
#            output = 3
#
#      ex.2  p = 5, q = 4
#            output = 5

# Test LCA
lca_root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8)))

lowestCommonAncestor(lca_root, lca_root.left, lca_root.right)  # 3
lowestCommonAncestor(lca_root, lca_root.left, lca_root.left.right.right)  # 5

# ================================================================
# PATTERN 6: TOP-DOWN CONTEXT PASSING
# PATTERN EXPLANATION: Pass path-specific information down from parent to children.
# Key insight: Each node makes decisions based on accumulated context from ancestors.
# Applications: Path validation, constraint checking, ancestor-dependent counting, resource tracking.
# ================================================================

def goodNodes(root):
    """
    # Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X. Return the number of good nodes in the binary tree.
    """
    def dfs(node, max_val):
        if not node: 
            return 0
        
        # Check if current node is good (curr node > root)
        good_count = 1 if node.val >= max_val else 0
        
        # Update max path value for children 
        new_max = max(max_val, node.val)
        
        # Add good nodes from subtrees
        good_count = good_count + dfs(node.left, new_max)
        good_count = good_count + dfs(node.right, new_max)
        
        return good_count
    
    return dfs(root, root.val) # Pass in the 

#                3
#               / \
#              /   \
#             1     4
#            /     / \
#           /     /   \
#          3     1     5
#
# Output: 4
# Root Node (3) is always a good node.
# Node 4 -> (3,4) is the maximum value in the path starting from the root.
# Node 5 -> (3,4,5) is the maximum value in the path
# Node 3 -> (3,1,3) is the maximum value in the path.

# Test good nodes
good_root = TreeNode(3, TreeNode(1, TreeNode(3), None), TreeNode(4, TreeNode(1), TreeNode(5)))

print("Number of good nodes:", goodNodes(good_root))  # 4
