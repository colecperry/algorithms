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

DFS vs BFS:
- Both can find all paths, but DFS is more memory efficient for it
- DFS: one path at a time, backtrack and reuse → O(depth) space
- BFS: many paths at once, each queue item needs its own copy → O(width × path length) space
- Use BFS only when you need SHORTEST path or LEVEL-BY-LEVEL processing

DFS CORE TEMPLATES
==================
"""

"""
DFS COMPLEXITY REFERENCE
=========================

+----------------------------------+---------------+-----------+
| Pattern                          | Time          | Space     |
+----------------------------------+---------------+-----------+
| Tree DFS - Build Up (Post-Order) | O(n)          | O(h)      |
| Tree DFS - Pass Down (Pre-Order) | O(n)          | O(h)      |
| Graph DFS with Visited           | O(n + e)      | O(n)      |
| Matrix DFS - Flood Fill          | O(m * n)      | O(m * n)  |
| DFS + Memoization (Top-Down DP)  | O(amount * k) | O(amount) |
+----------------------------------+---------------+-----------+

n = number of nodes/rooms, h = height of tree (worst case O(n) if skewed),
e = edges (keys found in rooms), m * n = grid dimensions, amount = target
value being built up to, k = number of choices tried per subproblem (coins)

WHAT EACH PATTERN IS:
- Tree DFS - Build Up (Post-Order): process a node's children first, then combine their
  answers into the current node's answer — like asking each subordinate for a number
  before adding them up into your own total.
- Tree DFS - Pass Down (Pre-Order): carry information from a parent down to its
  children as you descend, so each node already knows things like "how much is left"
  before it decides what to do.
- Graph DFS with Visited: explore a network of connected nodes by following one path
  as far as it goes, keeping a "seen" list so cycles don't cause infinite loops.
- Matrix DFS - Flood Fill: spread outward from a starting cell into every connected
  neighboring cell that matches, like a paint-bucket tool filling a region in an image.
- DFS + Memoization (Top-Down DP): explore a tree of recursive choices, but remember
  the answer to any sub-choice you've already solved so it's never redone.

NOTES:
- Tree DFS (build-up / pass-down): each node visited exactly once -> O(n); recursion
  depth is bounded by tree height h, which is O(n) worst case if the tree is skewed
- Graph DFS with visited: each vertex visited once, each edge/key checked once ->
  O(n + e); visited set holds up to n entries
- Matrix DFS flood fill: each cell visited at most once thanks to the visited/color
  check -> O(m*n); recursion stack can reach O(m*n) in the worst case
- DFS + memoization: each distinct subproblem from 0..amount is solved once and
  cached, with k choices tried per subproblem -> O(amount * k) time; memo dict plus
  recursion stack -> O(amount) space
"""

# ================================================================
# RECURSIVE DFS TEMPLATE - TREES
# ================================================================
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs_recursive_template(node):
    '''
    Calculate max depth of a binary tree - showcases fundamental DFS structure for trees
    
    TC: O(n) - visit each node once
    SC: O(h) - recursion stack depth, where h = height of tree (worst case O(n) if skewed)
    '''
    # Base case - when to stop recursion
    if not node:
        return 0
    
    # Recursive calls to explore children/neighbors
    left_result = dfs_recursive_template(node.left)   # <- keeps calling left 
    right_result = dfs_recursive_template(node.right) #    until base case
    
    # MY height = 1 (me) + max of both children
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
    
    TC: O(n) - visit each node once
    SC: O(h) - stack holds at most h nodes, where h = height of tree (worst case O(n) if skewed)
    '''
    if not root: # Edge case: empty tree
        return []
    
    stack = [root] # DFS stack initalization 
    result = []
    
    # MAIN DFS LOOP: 
    while stack:
        node = stack.pop()      # Get the next node -> DFS pops from end
        result.append(node.val) # Process current node
        
        # Add children (adding right then left ensures we would pop and process the left side first - DFS) 
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
    stack = [(start_row, start_col)] # DFS uses a stack (.pop()) from end -> LIFO
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
            
            if (0 <= new_row < rows and # OOB checks
                0 <= new_col < cols and 
                (new_row, new_col) not in visited): # Only visit new cells 
                
                visited.add((new_row, new_col))
                stack.append((new_row, new_col))  # Add to END (will be processed next when popped - creates DFS depth)
    
    return result

# Test matrix
test_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Run the function
print("Matrix DFS from (0,0):", matrix_dfs_template(test_matrix, 0, 0))

# ================================================================
# GRAPH DFS TEMPLATE
# ================================================================

def graph_dfs_template(graph, start_node):
    """
    Graph DFS template with visited tracking using adjacency list
    
    EXPLORATION PATTERN: DFS explores in "deep dive" paths
    - Follows one path completely before trying alternatives
    - Like exploring one tunnel system fully before checking other tunnels
    - Path might be: A → B → D → E → backtrack → C → F
    - Does NOT guarantee shortest path, but visits all reachable nodes
    
    Graph format: {node: [list of neighbors]}
    Example: {'A': ['B', 'C'], 'B': ['D'], 'C': ['F'], ...}
    
    TC: O(V + E) - visit each vertex once, explore each edge once
    SC: O(V) - we only hold verticies not edges in our visited set + stack
    """
    # Edge case: empty graph or start not in graph
    if not graph or start_node not in graph:
        return []
    
    stack = [start_node]  # DFS uses a stack (.pop())
    visited = set([start_node])
    result = []
    
    while stack:
        node = stack.pop()  # <- DFS line: pops from end (LIFO - Last In First Out)
        
        # Process current node
        result.append(node)
        
        # Add unvisited neighbors to stack
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)  # Add to END (will be processed next - creates DFS depth)
    
    return result


def graph_dfs_recursive(graph, start_node):
    """
    Recursive DFS template - cleaner for many problems
    
    Same exploration pattern but uses call stack instead of explicit stack
    Often preferred for tree problems and clearer logic
    """
    visited = set()
    result = []
    
    def dfs(node):
        if node in visited:
            return
        
        visited.add(node)
        result.append(node)  # Process node
        
        # Recursively visit all neighbors
        for neighbor in graph[node]:
            dfs(neighbor)
    
    dfs(start_node)
    return result

test_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'F'],
    'D': ['B', 'E'],
    'E': ['D', 'G'],
    'F': ['C', 'G'],
    'G': ['E', 'F']
}

print("Iterative DFS from 'A':", graph_dfs_template(test_graph, 'A'))
# Possible output: ['A', 'C', 'F', 'G', 'E', 'D', 'B']
# (order depends on which neighbor added to stack last)

print("Recursive DFS from 'A':", graph_dfs_recursive(test_graph, 'A'))
# Possible output: ['A', 'B', 'D', 'E', 'G', 'F', 'C']
# (visits first neighbor completely before second)


# Graph visualization:
#       A
#      / \
#     B   C
#    /     \
#   D       F
#    \     /
#     E - G

"""
================================================================
PATTERN 1: TREE DFS - BUILD UP (POST-ORDER)

PATTERN EXPLANATION: Recursively process children nodes before processing the current node, then combine information from children to compute the parent's result. This bottom-up approach allows each node to make decisions based on complete information from its subtrees. Values flow upward through the tree as the recursion unwinds.

#
Applications: Height calculation, diameter, balanced tree check, LCA, subtree properties.
================================================================
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TreeDFSBuildUp:
    """
    Giveaway: "find the maximum depth/height" of a tree means every node's answer
    depends on the answer of BOTH its children combined (1 + max of the two) — you
    can't know a node's depth until its subtrees are fully solved, which is the
    signal for post-order build-up instead of passing state downward.

    Find the maximum depth (height) of a binary tree.
    Depth = number of nodes from root to furthest leaf.
    
    #      3
    #     / \
    #    9  20
    #      /  \
    #     15   7
    
    # Depth = 3 (path: 3 -> 20 -> 15)
    
    Steps:
    1. Base case: if node is None, return 0 (empty subtree has depth 0)
    2. Recurse left: call maxDepth on left child to get left subtree depth
    3. Recurse right: call maxDepth on right child to get right subtree depth
    4. Combine: return 1 + max(left_depth, right_depth) for the current node
    """
    def maxDepth(self, root):  # LC 104
        """
        - TC: O(n) - visit each node once
        - SC: O(h) - recursion stack depth
        """
        if not root: # Base case: we reached end of path -> 
            return 0 # empty tree has depth 0
        
        # Step 1: Get res from left child (build up from bottom)
        left_depth = self.maxDepth(root.left)
        
        # Step 2: Get result from right child
        right_depth = self.maxDepth(root.right)
        
        # Step 3: Process current node using children's results
        # Current depth = 1 (for this node) + max of children
        current_depth = 1 + max(left_depth, right_depth)
        
        # Step 4: Return to parent (value bubbles up)
        return current_depth

#      3
#     / \
#    9  20
#      /  \
#     15   7
#
# Depth = 3 (path: 3 -> 20 -> 15)
# 
#
# How it builds up (following DFS order):
# POST-ORDER: Visit left subtree → right subtree → process current node
# Key insight: A node can only compute its depth AFTER both children return
#
# maxDepth(3)
#   ├─ left: maxDepth(9)
#   │    ├─ left: maxDepth(None) → 0
#   │    ├─ right: maxDepth(None) → 0
#   │    └─ return 1 + max(0,0) = 1  ← Node 9 done
#   │
#   └─ right: maxDepth(20)
#        ├─ left: maxDepth(15)
#        │    ├─ left: maxDepth(None) → 0
#        │    ├─ right: maxDepth(None) → 0
#        │    └─ return 1 + max(0,0) = 1  ← Node 15 done
#        │
#        ├─ right: maxDepth(7)
#        │    ├─ left: maxDepth(None) → 0
#        │    ├─ right: maxDepth(None) → 0
#        │    └─ return 1 + max(0,0) = 1  ← Node 7 done
#        │
#        └─ return 1 + max(1,1) = 2  ← Node 20 done
#
#   return 1 + max(1,2) = 3  ← Node 3 done (final answer)

# Test
root = TreeNode(3, 
    TreeNode(9), 
    TreeNode(20, TreeNode(15), TreeNode(7)))

sol = TreeDFSBuildUp()
print("Max Depth:", sol.maxDepth(root))  # Output: 3

"""
===============================================================
PATTERN 2: TREE DFS - PASS DOWN (PRE-ORDER)
PATTERN EXPLANATION: Pass information downward from parent to children during traversal. Each node receives accumulated context from its ancestors (such as path sum, depth, or constraints) and uses this information to make decisions or check conditions. State is updated as you descend and passed to recursive calls.

#
Applications: Path sum validation, path finding, ancestor-dependent counting, level tracking.
===============================================================
"""
class TreeDFSPassDown:
    """
    Giveaway: the check is specifically "root-to-leaf" path sum — the answer at a
    leaf depends on a running total accumulated from the root down (targetSum minus
    everything spent so far), so each node needs its ancestors' contribution passed
    down to it rather than needing anything back from its children.

    Determine if tree has root-to-leaf path that sums to targetSum.
    
    #        5
    #       / \
    #      4   8
    #     /   / \
    #    11  13  4
    #   /  \      \
    #  7    2      1
    #
    # targetSum = 22
    # Path: 5 -> 4 -> 11 -> 2 = 22 ✓
    # Output: True
    
    Steps:
    1. Base case (empty): if root is None, return False (no path exists)
    2. Base case (leaf): if node has no children, return root.val == targetSum
    3. Update state: compute remaining = targetSum - root.val
    4. Recurse left: call hasPathSum on left child with remaining
    5. Recurse right: call hasPathSum on right child with remaining
    6. Combine: return left_has_path or right_has_path
    """
    def hasPathSum(self, root, targetSum):  # LC 112 - Path Sum
        """
        - TC: O(n) - visit each node once
        - SC: O(h) - recursion stack depth
        """
        if not root: # Base case 1: empty tree has no paths 
            return False # & cannot sum to target
        
        # Base case 2: Leaf node: check if this completes a valid path
        if not root.left and not root.right:
            return root.val == targetSum # Return boolean to caller
        
        # Update state: calculate remaining sum after this node processed
        remaining = targetSum - root.val
        
        # Pass down to children: check if either subtree has valid path
        left_has_path = self.hasPathSum(root.left, remaining)
        right_has_path = self.hasPathSum(root.right, remaining)
        
        return left_has_path or right_has_path

        #        5
        #       / \
        #      4   8
        #     /   / \
        #    11  13  4
        #   /  \      \
        #  7    2      1
        #
        # targetSum = 22
        # Path: 5 -> 4 -> 11 -> 2 = 22 ✓
        # Output: True

# Test
root = TreeNode(5, 
    TreeNode(4, 
        TreeNode(11, TreeNode(7), TreeNode(2))),
    TreeNode(8, 
        TreeNode(13), 
        TreeNode(4, None, TreeNode(1))))

sol = TreeDFSPassDown()
print("Has Path Sum (22):", sol.hasPathSum(root, 22))  # True
print("Has Path Sum (100):", sol.hasPathSum(root, 100))  # False

"""
===============================================================
PATTERN 3: GRAPH DFS WITH VISITED
PATTERN EXPLANATION: Traverse a graph represented as an adjacency list while maintaining a visited set to track already-explored nodes. This prevents infinite loops in cyclic graphs and avoids redundant processing. Can be implemented recursively (using call stack) or iteratively (using explicit stack).

#
Applications: Graph traversal, reachability, connected components, cycle detection.
================================================================
"""                  
class GraphDFS:
    """
    Giveaway: rooms are only reachable by keys found in other rooms — "visit all
    rooms" is really a reachability question over an implicit graph (room = node,
    key = edge), and the natural cycle risk (keys can point back to visited rooms)
    is what calls for a visited set during traversal instead of plain recursion.

    There are n rooms labeled 0 to n-1. All rooms are locked except room 0. Your goal is to visit all rooms. When you visit a room, you get all keys in that room. Can you visit all rooms?
    
    Example 1:
        rooms = [[1],[2],[3],[]]
        
        Visual: 0 -> 1 -> 2 -> 3
        
        Start in room 0, get key to room 1
        Visit room 1, get key to room 2
        Visit room 2, get key to room 3
        Visit room 3
        
        Output: True (visited all 4 rooms)
    
    Steps:
    1. Initialize visited set and start DFS from room 0 (the only unlocked room)
    2. Mark current room as visited
    3. For each key in the current room:
       a. Skip if that room is already in visited
       b. Recursively call dfs on the room that key unlocks
    4. After DFS completes, check if len(visited) == len(rooms)
    """
    def canVisitAllRooms(self, rooms):  # LC 841
        """
        - TC: O(n + e) - visit each room once, check each key once
        - SC: O(n) - visited set stores up to n rooms
        """
        visited = set()  # Track which rooms we've visited
        
        def dfs(room):
            """Visit a room and recursively visit all reachable rooms"""
            # Mark current room as visited (before processing neighbors)
            visited.add(room)
            
            # For each key (neighbor) in this room
            for key in rooms[room]:
                if key not in visited:  # Only visit unvisited rooms
                    dfs(key)
        
        # Start DFS from room 0 (the only unlocked room)
        dfs(0)
        
        # Check if we visited all rooms
        return len(visited) == len(rooms)

    # ITERATIVE SOLUTION (using explicit stack)
    def canVisitAllRoomsIterative(self, rooms):
        """
        Pattern: DFS with explicit stack and visited set
        
        How it works:
        1. Use stack for DFS traversal (instead of recursion)
        2. visited set tracks which rooms we've entered
        3. Process each room: mark visited, add unvisited neighbors to stack
        """
        visited = set([0])  # Start with room 0
        stack = [0] # dfs stack holds keys for next room to visit
        
        while stack:
            room = stack.pop() # dfs pops from end
            
            for key in rooms[room]: # Process each key in curr room 
                if key not in visited:  # Haven't visited this room yet
                    visited.add(key)
                    stack.append(key) # dfs appends to end
        
        return len(visited) == len(rooms)

# Test case 1: Can visit all rooms
rooms1 = [[1],[2],[3],[]]
sol = GraphDFS()
print("Can visit all rooms:", sol.canVisitAllRooms(rooms1))  # True
print("Can visit all rooms (iterative):", sol.canVisitAllRoomsIterative(rooms1))  # True

# Test case 2: Cannot visit all rooms (room 2 unreachable)
rooms2 = [[1,3],[3,0,1],[2],[0]]
print("Can visit all rooms:", sol.canVisitAllRooms(rooms2))  # False
print("Can visit all rooms (iterative):", sol.canVisitAllRoomsIterative(rooms2))  # False

# Test case 3: Single room
rooms3 = [[]]
print("Can visit all rooms:", sol.canVisitAllRooms(rooms3))  # True

"""
===============================================================
PATTERN 4: MATRIX DFS - FLOOD FILL
PATTERN EXPLANATION: Explore connected regions in a 2D grid by recursively visiting adjacent cells. The grid represents an implicit graph where each cell's neighbors are the adjacent cells (4 or 8 directions). Track visited cells to avoid infinite recursion, either using a separate set or by modifying the grid in-place.

#
Applications: Fill regions, change colors, connected components in grid, islands.
================================================================
"""
class MatrixDFS:
    """
    Giveaway: "change the color of the starting pixel and all connected pixels of
    the same color" is literally describing a paint-bucket fill — the region to
    change is defined by connectivity through matching neighbor values, which is
    the exact shape of a flood-fill DFS on a grid.

    Perform flood fill starting from pixel (sr, sc). Change the color of the starting pixel and all connected pixels of the same color to the new color.
    
    Connected = 4-directionally adjacent (up, down, left, right).
    
    Example:
        image = [[1,1,1],
                 [1,1,0],
                 [1,0,1]]
        sr = 1, sc = 1, color = 2
        
        Starting pixel is 1, all connected 1's become 2:
        
        Output: [[2,2,2],
                 [2,2,0],
                 [2,0,1]]
    
    Steps:
    1. Save original_color = image[sr][sc]; if it already equals color, return early
    2. Call dfs(sr, sc) to start the fill from the starting pixel
    3. In dfs(r, c): change image[r][c] to color (marks cell as visited)
    4. For each of the 4 directions (up, down, left, right):
       a. Compute neighbor coordinates (nr, nc)
       b. Skip if out of bounds or image[nr][nc] != original_color
       c. Recurse: call dfs(nr, nc)
    5. Return the modified image
    """
    def floodFill(self, image, sr, sc, color):  # LC 733
        """
        - TC: O(m * n) - visit each pixel at most once
        - SC: O(m * n) - recursion stack in worst case
        """
        original_color = image[sr][sc]
        
        # Edge case: already the target color (would cause infinite recursion!)
        if original_color == color:
            return image
        
        rows, cols = len(image), len(image[0])
        
        def dfs(r, c):
            """Fill cell at (r,c) and all connected cells"""
            image[r][c] = color  # Change color (marks as visited)
            
            # Explore 4 directions - check BEFORE recursing to avoid unnecessary calls
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc # updated row & col
                if (0 <= nr < rows and   # Row not OOB 
                    0 <= nc < cols and   # Col not OOB 
                    image[nr][nc] == original_color): # Matches original color (not yet visited)
                    dfs(nr, nc) # now we can recurse
        
        dfs(sr, sc)
        return image

# Test
image = [[1,1,1],
         [1,1,0],
         [1,0,1]]

sol = MatrixDFS()
print(sol.floodFill(image, 1, 1, 2))
# Output: [[2,2,2],
#          [2,2,0],
#          [2,0,1]]

"""
===============================================================
PATTERN 5: DFS + MEMOIZATION (TOP-DOWN DYNAMIC PROGRAMMING)
===============================================================

CORE IDEA: 
Cache recursive results to avoid solving the same subproblem twice.
Think: "Have I seen this before? Yes → return cached answer. No → solve and cache it."

WHEN TO USE:
✓ Recursive solution exists but has overlapping subproblems
✓ Problem has optimal substructure (optimal solution = combination of optimal sub-solutions)
✓ State can be captured as hashable parameters (int, tuple, string)

TEMPLATE:
    memo = {}
    
    def dfs(state):
        # 1. Check cache first
        if state in memo:
            return memo[state]
        
        # 2. Base case(s)
        if base_case:
            return base_value
        
        # 3. Recursive case: try all options
        result = combine(dfs(smaller_state) for each option)
        
        # 4. Cache and return
        memo[state] = result
        return result

COMMON APPLICATIONS:
Coin change, climbing stairs, decode ways, unique paths, 
partition problems, subsequence problems, house robber
===============================================================
"""

class CoinChange:  # LC 322
    """
    Giveaway: "minimum number of coins" to hit a target, where you try every
    denomination at every remaining amount, produces the same sub-amount over and
    over from different coin orderings (e.g. 5 then 2 or 2 then 5) — that repeated,
    overlapping subproblem is the tell for caching DFS results instead of plain
    recursion.

    Given coin denominations and target amount, return minimum coins needed.
    Return -1 if impossible.
    
    Example 1: coins = [1,2,5], amount = 11 → 3  (5+5+1)
    Example 2: coins = [2], amount = 3 → -1      (impossible)
    """
    
    def coinChange(self, coins: list[int], amount: int) -> int:
        """
        TC: O(amount * len(coins)) - each amount computed once, trying all coins
        SC: O(amount) - memo dict + recursion stack
        """
        memo = {}
        
        def dfs(remaining):
            # Base cases
            if remaining == 0:
                return 0  # no coins needed for $0
            if remaining < 0:
                return float('inf')  # impossible, use inf so min() ignores it
            
            # Check cache
            if remaining in memo:
                return memo[remaining]
            
            # Try each coin, find minimum
            min_coins = float('inf')
            for coin in coins:
                coins_needed = dfs(remaining - coin)  # use this coin + solve the rest
                min_coins = min(min_coins, coins_needed)
            
            # Cache: 1 coin used now + minimum for the rest
            memo[remaining] = 1 + min_coins
            return memo[remaining]
        
        result = dfs(amount)
        return result if result != float('inf') else -1


# ============== SIMPLE EXAMPLE FIRST ==============
# coins = [2, 5], amount = 7
#
# dfs(7)
#   Try coin 2: dfs(5)
#     Try coin 2: dfs(3)
#       Try coin 2: dfs(1)
#         Try coin 2: dfs(-1) → inf  ❌
#         Try coin 5: dfs(-4) → inf  ❌
#         memo[1] = 1 + inf = inf
#       Try coin 5: dfs(-2) → inf  ❌
#       memo[3] = 1 + inf = inf
#     Try coin 5: dfs(0) → 0  ✓
#     memo[5] = 1 + 0 = 1
#   Try coin 5: dfs(2)
#     Try coin 2: dfs(0) → 0  ✓
#     Try coin 5: dfs(-3) → inf  ❌
#     memo[2] = 1 + 0 = 1
#   memo[7] = 1 + min(1, 1) = 2
#
# Answer: 2 coins (5+2)


# ============== DETAILED WALKTHROUGH ==============
# coins = [1, 2, 5], amount = 5
# Watch how memoization prevents redundant work!
#
# dfs(5)
#   coin 1 → dfs(4)
#     coin 1 → dfs(3)
#       coin 1 → dfs(2)
#         coin 1 → dfs(1)
#           coin 1 → dfs(0) = 0  ✓
#           coin 2 → dfs(-1) = inf
#           coin 5 → dfs(-4) = inf
#           CACHE: memo[1] = 1 + 0 = 1
#         
#         coin 2 → dfs(0) = 0  ✓
#         coin 5 → dfs(-3) = inf
#         CACHE: memo[2] = 1 + 0 = 1
#       
#       coin 2 → dfs(1) = 1  📋 MEMO HIT! No recursion needed
#       coin 5 → dfs(-2) = inf
#       CACHE: memo[3] = 1 + min(1, 1, inf) = 2
#     
#     coin 2 → dfs(2) = 1  📋 MEMO HIT!
#     coin 5 → dfs(-1) = inf
#     CACHE: memo[4] = 1 + min(1, 1, inf) = 2
#   
#   coin 2 → dfs(3) = 2  📋 MEMO HIT!
#   coin 5 → dfs(0) = 0  ✓
#   CACHE: memo[5] = 1 + min(2, 2, 0) = 1
#
# FINAL ANSWER: 1 (just use the 5-cent coin)
#
# 🔑 KEY INSIGHTS:
# • Recursion goes DEEP first (all the way to base case)
# • Each amount is computed ONCE and cached
# • Memo hits (📋) save massive amounts of work
# • Without memo: exponential paths. With memo: linear in amount!
# • The "1 +" happens AFTER the recursive call returns


# ============== TESTS ==============
sol = CoinChange()
print(sol.coinChange([1, 2, 5], 5))   # 1
print(sol.coinChange([2], 3))         # -1
print(sol.coinChange([1, 2, 5], 11))  # 3
print(sol.coinChange([2], 3))         # -1

