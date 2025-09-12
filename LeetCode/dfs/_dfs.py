"""
=================================================================
DEPTH-FIRST SEARCH (DFS) COMPLETE GUIDE
=================================================================

WHAT IS DFS?
-----------
Depth-First Search (DFS) is a graph traversal algorithm that explores as far as possible
along each branch before backtracking. It "goes deep" before going wide.

Key characteristics:
- Uses a STACK (LIFO - Last In, First Out) data structure
- Explores one path completely before trying another path
- Can be implemented recursively (using call stack) or iteratively (using explicit stack)
- Time complexity: O(n) for trees
- Space complexity: O(h) where h is height/depth of recursion

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
    
    # Combine results and return (post-order processing)
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
        
        # Add children (right then left ensures correct processing from back of the stack)
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
    Matrix DFS template - Perform a DFS matrix traversal and return a list of values from the visited cells in the order they were explored
    
    EXPLORATION PATTERN: DFS explores in "deep dive" paths
    - Picks one direction and goes as far as possible before backtracking
    - Like following a single hallway to its end, then returning to try other hallways
    - Path might be: (0,0) → (0,1) → (0,2) → (1,2) → (2,2) → backtrack → try new path
    - Does NOT guarantee shortest path, but explores all reachable cells
    """
    # Edge case: empty matrix or invalid starting position
    if not matrix or not matrix[0] or start_row < 0 or start_col < 0 or start_row >= len(matrix) or start_col >= len(matrix[0]):
        return []
    
    # Initialize stack with starting position and tracking structures
    stack = [(start_row, start_col)]
    visited = set()
    result = []
    
    # Define 4 directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while stack:
        # Get next position (LIFO: Append to end, pop from end)
        row, col = stack.pop()
        
        # Skip if already visited
        if (row, col) in visited:
            continue
            
        # Mark as visited and process current cell
        visited.add((row, col))
        result.append(matrix[row][col])
        
        # DFS - explore 4 directions for each popped cell (cells that are 1 step away)
        for dr, dc in directions: 
            new_row, new_col = row + dr, col + dc # compute matrix cell
            
            # Check bounds valid and if unvisited for new cell
            if (0 <= new_row < len(matrix) and 
                0 <= new_col < len(matrix[0]) and 
                (new_row, new_col) not in visited):
                stack.append((new_row, new_col))  # Add to top of stack (will be processed next - creates depth)
    
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
# PATTERN 1: TREE TRAVERSAL
# LC 94 - Binary Tree Inorder Traversal
# PATTERN EXPLANATION:
# This pattern involves visiting all nodes in a specific order (inorder: left-root-right).
# Key insight: For inorder iterative, we need to go as left as possible first,
# then process the node, then go right. This requires careful stack management.
# ================================================================

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class InorderTraversal:
    # RECURSIVE SOLUTION
    def inorderTraversal(self, root):
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
            if root is None:  # Base case
                return
            dfs(root.left)    # Left
            res.append(root.val)  # Root
            dfs(root.right)   # Right
        
        dfs(root)
        return res
    
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
        stack = []
        curr = root
        
        while curr or stack:
            # Go to the leftmost node
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # Process current node
            curr = stack.pop()
            res.append(curr.val)
            
            # Move to right subtree
            curr = curr.right
        
        return res

# Test the inorder traversal
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

solution = InorderTraversal()
print("Recursive inorder:", solution.inorderTraversal(root))  # [1, 3, 2]
print("Iterative inorder:", solution.inorderTraversalIterative(root))  # [1, 3, 2]

# ================================================================
# PATTERN 2: TREE COMPARISON
# LC 100 - Same Tree
# PATTERN EXPLANATION:
# This pattern compares two trees simultaneously by traversing both at the same time.
# Key insight: Use parallel traversal - compare corresponding nodes at each step.
# Base cases handle mismatched structures (one null, other not null).
# ================================================================

class SameTree:
    # RECURSIVE SOLUTION
    def isSameTree(self, p, q):
        """
        Pattern: Simultaneous tree traversal with comparison
        Time: O(min(m,n)), Space: O(min(m,n))
        
        How it works:
        1. Base cases: both null (true), one null (false), values differ (false)
        2. If current nodes match, recursively check left and right subtrees
        3. Return true only if both subtrees match
        """
        # Base cases
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        # Recursive comparison
        return (self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right))
    
    # ITERATIVE SOLUTION
    def isSameTreeIterative(self, p, q):
        """
        Pattern: Paired node processing with stack
        
        How it works:
        1. Stack stores pairs of corresponding nodes
        2. For each pair, check if they match
        3. Add their children pairs to stack for future comparison
        """
        stack = [(p, q)]
        
        while stack:
            node1, node2 = stack.pop()
            
            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            
            stack.append((node1.left, node2.left))
            stack.append((node1.right, node2.right))
        
        return True

# Test same tree
p = TreeNode(1, TreeNode(2), TreeNode(3))
q = TreeNode(1, TreeNode(2), TreeNode(3))
p2 = TreeNode(1, TreeNode(2), None)
q2 = TreeNode(1, None, TreeNode(2))

same_tree = SameTree()
print("Same trees (recursive):", same_tree.isSameTree(p, q))  # True
print("Different trees (recursive):", same_tree.isSameTree(p2, q2))  # False
print("Same trees (iterative):", same_tree.isSameTreeIterative(p, q))  # True
print("Different trees (iterative):", same_tree.isSameTreeIterative(p2, q2))  # False

# ================================================================
# PATTERN 3: TREE PROPERTY VALIDATION - MIRROR COMPARISON
# LC 101 - Symmetric Tree
# PATTERN EXPLANATION:
# This pattern checks if a tree is symmetric by comparing mirror positions.
# Key insight: For symmetry, left subtree should mirror right subtree.
# Compare left.left with right.right AND left.right with right.left.
# ================================================================

class SymmetricTree:
    # RECURSIVE SOLUTION
    def isSymmetric(self, root):
        """
        Pattern: Mirror comparison with helper function
        Time: O(n), Space: O(h)
        
        How it works:
        1. Helper function compares two nodes for symmetry
        2. Base cases: both null (symmetric), one null (not symmetric)
        3. For symmetry: values must match AND subtrees must be mirrors
        4. Mirror check: left.left vs right.right, left.right vs right.left
        """
        def dfs(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            
            # Mirror comparison: left.left with right.right, left.right with right.left
            return (dfs(left.left, right.right) and 
                    dfs(left.right, right.left))
        
        return dfs(root.left, root.right) if root else True
    
    # ITERATIVE SOLUTION
    def isSymmetricIterative(self, root):
        """
        Pattern: Mirror node pairs in stack
        
        How it works:
        1. Stack stores pairs of nodes that should be mirrors
        2. For each pair, verify they match for symmetry
        3. Add their mirror children pairs to stack
        """
        if not root:
            return True
        
        stack = [(root.left, root.right)]
        
        while stack:
            left, right = stack.pop()
            
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            
            # Add mirror pairs
            stack.append((left.left, right.right))
            stack.append((left.right, right.left))
        
        return True

# Test symmetric tree
symmetric_root = TreeNode(1)
symmetric_root.left = TreeNode(2)
symmetric_root.right = TreeNode(2)
symmetric_root.left.left = TreeNode(3)
symmetric_root.left.right = TreeNode(4)
symmetric_root.right.left = TreeNode(4)
symmetric_root.right.right = TreeNode(3)

asymmetric_root = TreeNode(1)
asymmetric_root.left = TreeNode(2)
asymmetric_root.right = TreeNode(2)
asymmetric_root.left.right = TreeNode(3)
asymmetric_root.right.right = TreeNode(3)

symmetric = SymmetricTree()
print("Symmetric tree (recursive):", symmetric.isSymmetric(symmetric_root))  # True
print("Asymmetric tree (recursive):", symmetric.isSymmetric(asymmetric_root))  # False
print("Symmetric tree (iterative):", symmetric.isSymmetricIterative(symmetric_root))  # True
print("Asymmetric tree (iterative):", symmetric.isSymmetricIterative(asymmetric_root))  # False

# ================================================================
# PATTERN 4: PATH SUM PROBLEMS - TARGET TRACKING
# LC 112 - Path Sum
# PATTERN EXPLANATION:
# This pattern tracks a running sum/target while traversing root-to-leaf paths.
# Key insight: Subtract current node value from target and pass remaining target down.
# Success condition: reach a leaf node with remaining target = node value.
# ================================================================

class PathSum:
    # RECURSIVE SOLUTION
    def hasPathSum(self, root, targetSum):
        """
        Pattern: Path tracking with remaining sum
        Time: O(n), Space: O(h)
        
        How it works:
        1. Base case: no node means no path
        2. Leaf node check: if leaf, check if remaining sum equals node value
        3. Recursive calls: subtract current value and check subtrees
        4. Return true if ANY path sums to target
        """
        if not root:
            return False
        
        # Leaf node check
        if not root.left and not root.right:
            return targetSum == root.val
        
        # Recursive calls with updated sum
        remaining = targetSum - root.val
        return (self.hasPathSum(root.left, remaining) or 
                self.hasPathSum(root.right, remaining))
    
    # ITERATIVE SOLUTION
    def hasPathSumIterative(self, root, targetSum):
        """
        Pattern: Node-sum pairs in stack
        
        How it works:
        1. Stack stores (node, remaining_sum) pairs
        2. For each node, calculate new remaining sum
        3. If leaf node and remaining sum is 0, found path
        4. Add children with updated remaining sum
        """
        if not root:
            return False
        
        stack = [(root, targetSum)]
        
        while stack:
            node, curr_sum = stack.pop()
            remaining = curr_sum - node.val
            
            # Check leaf node
            if not node.left and not node.right and remaining == 0:
                return True
            
            # Add children with updated sum
            if node.right:
                stack.append((node.right, remaining))
            if node.left:
                stack.append((node.left, remaining))
        
        return False

# Test path sum
path_root = TreeNode(5)
path_root.left = TreeNode(4)
path_root.right = TreeNode(8)
path_root.left.left = TreeNode(11)
path_root.right.left = TreeNode(13)
path_root.right.right = TreeNode(4)
path_root.left.left.left = TreeNode(7)
path_root.left.left.right = TreeNode(2)
path_root.right.right.right = TreeNode(1)

path_sum = PathSum()
print("Has path sum 22 (recursive):", path_sum.hasPathSum(path_root, 22))  # True
print("Has path sum 22 (iterative):", path_sum.hasPathSumIterative(path_root, 22))  # True

# ================================================================
# PATTERN 5: TREE MODIFICATION - IN-PLACE CHANGES
# LC 226 - Invert Binary Tree
# PATTERN EXPLANATION:
# This pattern modifies tree structure while traversing.
# Key insight: Make changes to current node, then recursively process children.
# Order matters: can modify before recursion (preorder) or after (postorder).
# ================================================================

class InvertTree:
    # RECURSIVE SOLUTION
    def invertTree(self, root):
        """
        Pattern: Tree modification with recursive processing
        Time: O(n), Space: O(h)
        
        How it works:
        1. Base case: null node needs no inversion
        2. Swap current node's children
        3. Recursively invert both subtrees
        4. Return modified root
        """
        if not root:
            return None
        
        # Swap children
        root.left, root.right = root.right, root.left
        
        # Recursively invert subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
    
    # ITERATIVE SOLUTION
    def invertTreeIterative(self, root):
        """
        Pattern: Node processing with stack
        
        How it works:
        1. Use stack to visit all nodes
        2. For each node, swap its children
        3. Add children to stack for future processing
        """
        if not root:
            return None
        
        stack = [root]
        
        while stack:
            node = stack.pop()
            
            # Swap children
            node.left, node.right = node.right, node.left
            
            # Add children to stack
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return root

# Test invert tree
invert_root = TreeNode(4)
invert_root.left = TreeNode(2)
invert_root.right = TreeNode(7)
invert_root.left.left = TreeNode(1)
invert_root.left.right = TreeNode(3)
invert_root.right.left = TreeNode(6)
invert_root.right.right = TreeNode(9)

def print_tree_inorder(root):
    if not root:
        return []
    result = []
    def inorder(node):
        if node:
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
    inorder(root)
    return result

print("Original tree inorder:", print_tree_inorder(invert_root))
invert_tree = InvertTree()
inverted = invert_tree.invertTree(invert_root)
print("Inverted tree inorder:", print_tree_inorder(inverted))

# ================================================================
# PATTERN 6: LOWEST COMMON ANCESTOR - BOTTOM-UP INFORMATION FLOW
# LC 236 - Lowest Common Ancestor of Binary Tree
# PATTERN EXPLANATION:
# This pattern propagates information up from children to parents.
# Key insight: If a node receives non-null from both children, it's the LCA.
# If it receives non-null from one child, it passes that up (the LCA is above).
# ================================================================

class LCA:
    # RECURSIVE SOLUTION (Most elegant for this problem)
    def lowestCommonAncestor(self, root, p, q):
        """
        Pattern: Bottom-up information propagation
        Time: O(n), Space: O(h)
        
        How it works:
        1. If current node is p or q, return it (found one target)
        2. Recursively search left and right subtrees
        3. If both return non-null: current node is LCA (targets in different subtrees)
        4. If one returns non-null: pass it up (both targets in that subtree)
        5. If both return null: neither target found in this subtree
        
        Key insight: The first node that receives non-null from both children is the LCA
        """
        if not root or root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:  # Found both nodes in different subtrees
            return root
        return left or right  # Return whichever is non-null

# Test LCA
lca_root = TreeNode(3)
lca_root.left = TreeNode(5)
lca_root.right = TreeNode(1)
lca_root.left.left = TreeNode(6)
lca_root.left.right = TreeNode(2)
lca_root.right.left = TreeNode(0)
lca_root.right.right = TreeNode(8)
lca_root.left.right.left = TreeNode(7)
lca_root.left.right.right = TreeNode(4)

lca = LCA()
result = lca.lowestCommonAncestor(lca_root, lca_root.left, lca_root.right)  # nodes 5 and 1
print("LCA of 5 and 1:", result.val if result else None)  # 3

class GoodNodes:
    def goodNodes(self, root):
        """
        Pattern: Conditional counting with path context
        Time: O(n), Space: O(h)
        
        How it works:
        1. Pass down the maximum value seen on current path
        2. For each node, check if it's >= max_so_far (good node condition)
        3. Update max value and continue to children
        4. Sum up good nodes from current node and both subtrees
        """
        def dfs(node, max_val):
            if not node:
                return 0
            
            # Check if current node is good
            good_count = 1 if node.val >= max_val else 0
            
            # Update max value for children
            new_max = max(max_val, node.val)
            
            # Add good nodes from subtrees
            good_count += dfs(node.left, new_max)
            good_count += dfs(node.right, new_max)
            
            return good_count
        
        return dfs(root, root.val)

# Test good nodes
good_root = TreeNode(3)
good_root.left = TreeNode(1)
good_root.right = TreeNode(4)
good_root.left.left = TreeNode(3)
good_root.right.left = TreeNode(1)
good_root.right.right = TreeNode(5)

good_nodes = GoodNodes()
print("Number of good nodes:", good_nodes.goodNodes(good_root))  # 4
