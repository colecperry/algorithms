"""
BFS (Breadth-First Search) Complete Guide for LeetCode Problems
Based on problems: 100, 101, 103, 104, 111, 199, 200, 257, 404, 417, 559, 637, 733, 783, 993
"""

from collections import deque
from typing import List, Optional

# =============================================================================
# WHAT IS BFS?
# =============================================================================
"""
BFS explores nodes level by level, visiting all nodes at depth d before visiting nodes at depth d+1. Uses a queue (FIFO) data structure.

Key characteristics:
- Processes nodes in order of distance from starting point
- Guarantees shortest path in unweighted graphs
- Uses more memory than DFS due to queue storage
"""

# =============================================================================
# BASIC BFS STRUCTURE
# =============================================================================

def basic_bfs_template(start_node):
    """
    Standard BFS template - memorize this pattern
    """
    if not start_node:
        return
    
    queue = deque([start_node]) # deque & set expects an iterable obj (array or tuple)
    visited = set([start_node])  # Prevent revisiting nodes
    
    while queue:
        node = queue.popleft()
        
        # Process current node
        print(node.val)  # Or whatever processing needed
        
        # Add neighbors to queue (replace with specific neighbor access)
        # For binary tree:
        if node.left and node.left not in visited: # not null & not visited
            visited.add(node.left) 
            queue.append(node.left) # add to be explored
        if node.right and node.right not in visited:
            visited.add(node.right)
            queue.append(node.right)
        
        # For graph with adjacency list (node.neighbors):
        # for neighbor in node.neighbors:
        #     if neighbor not in visited:
        #         visited.add(neighbor)
        #         queue.append(neighbor)
        
        # For grid/matrix (assuming node has row, col attributes):
        # directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # for dr, dc in directions:
        #     new_row, new_col = node.row + dr, node.col + dc
        #     if (0 <= new_row < rows and 
        #         0 <= new_col < cols and 
        #         grid[new_row][new_col] not in visited):
        #         visited.add(grid[new_row][new_col])
        #         queue.append(grid[new_row][new_col])

# =============================================================================
# TREE BFS VARIANTS
# =============================================================================

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_traversal(root):
    """
    Basic tree BFS - no visited set needed since trees have no cycles
    Used in: LC 100, 101, 103, 104, 111, 199, 404, 559, 637, 783, 993
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)  # Process entire level at once
        level_nodes = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level_nodes.append(node.val)
            
            if node.left: # Add each node's children
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level_nodes)
    
    return result

# Create the tree nodes
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def bfs_with_level_tracking(self):
        """
        Track level explicitly - useful for problems requiring level information
        Used in: LC 103 (zigzag), 199 (right side view), 637 (level averages)
        """
        if not root:
            return []
        
        result = []
        queue = deque([(root, 0)])  # tuple with (node, level)
        
        while queue:
            node, level = queue.popleft() # destructure to get node val and level
            
            # Extend result if new level
            if level >= len(result):
                result.append([])
            
            result[level].append(node.val) # Append val to level (index in array)
            
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        
        return result
    
    #       3
    #      / \
    #     9   20
    #        /  \
    #       15   7
    
# Build the tree
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(root.bfs_with_level_tracking())  # Output: [[3], [9, 20], [15, 7]]

# Common Tuple Tracking in Tree-Based BFS:
# 1. (node, level): Track the level of each node for level-specific processing (e.g., Zigzag Level Order, Right Side View).
# 2. (node, is_left_child): Track if a node is a left child for problems like Sum of Left Leaves.
# 3. (node, parent): Track the parent of each node for parent-child relationship problems (e.g., Lowest Common Ancestor).
# 4. (node, path): Track the path from the root to the current node for path reconstruction (e.g., Binary Tree Paths).
# 5. (node, cumulative_sum): Track the sum of values from the root to the current node (e.g., Path Sum).
# 6. (node, depth): Track the depth of each node for depth-specific processing (e.g., Maximum Depth).
# 7. (node, distance): Track the distance from a target node (e.g., All Nodes Distance K).
# 8. (node, visited): Track visited nodes in trees with parent pointers to avoid revisiting (e.g., Distance

# =============================================================================
# GRID BFS TEMPLATE 
# =============================================================================

from collections import deque

def grid_bfs_example(grid, start_row, start_col):
    """
    Grid BFS template - Grid BFS template - Perform a BFS matrix traversal and return a list of values from the visited cells in the order they were explored

    EXPLORATION PATTERN: BFS explores in "ripple" or "wave" layers
    - Layer 0: Starting cell (0,0)
    - Layer 1: All direct neighbors of start
    - Layer 2: All neighbors of layer 1 (2 steps from start)
    - Layer 3: All neighbors of layer 2 (3 steps from start)
    This guarantees shortest path/minimum steps to any reachable cell.
    """
    if not grid or not grid[0]: # If grid is empty or first row is empty, grid invalid for BFS
        return []
    
    rows, cols = len(grid), len(grid[0]) # get number of rows and columns
    queue = deque([(start_row, start_col)]) # create queue with tuple of (row, col)
    visited = set([(start_row, start_col)]) # create visited set with tuple of (row, col)
    result = [] # collect values in order visited
    
    # 4 directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        row, col = queue.popleft() # FIFO: add to end, pop from front
        
        # Process current cell - collect its value
        result.append(grid[row][col])
        
        for dr, dc in directions: # travel all four directions
            new_row, new_col = row + dr, col + dc
            
            # Check bounds and conditions
            if (0 <= new_row < rows and # row not OOB
                0 <= new_col < cols and # col not OOB
                (new_row, new_col) not in visited): # not already visited
                
                visited.add((new_row, new_col)) # Add new cell to visited set
                queue.append((new_row, new_col)) # Add to end of queue (will be processed in next layer)
    
    return result

# Test matrix
test_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Run the function
print("Matrix BFS from (0,0):", grid_bfs_example(test_matrix, 0, 0))

# =============================================================================
# BFS VS DFS - WHEN TO USE WHICH
# =============================================================================
"""
Use BFS when:
- Need shortest path in unweighted (all steps cost 1) graph/grid. BFS guarentees that the first time a node is reached, it is reached via the shortest path b/c it explores all nodes at the curr level before moving to the next level
- Need to process nodes level by level
- Want to find minimum steps/distance
- Memory usage is not a primary concern

Use DFS when:
- Memory usage is critical (stack uses less space than queue)
- Need to explore all paths (backtracking)
- Tree problems that don't require level information
- Recursive solutions are more intuitive

Examples from problems:
- LC 111 (min depth): BFS better - stops at first leaf
- LC 104 (max depth): DFS equally good, more intuitive
- LC 200 (islands): Both work, DFS slightly more memory efficient
"""

# =============================================================================
# COMMON BFS PATTERNS & SOLUTIONS
# =============================================================================

# ----------------------------------------
# Pattern 1: Zigzag Level Order Traversal
# ----------------------------------------

# Traverse a binary tree level by level, but alterates the direction of traversal for each level

def zigzag_level_order(root):  # LC 103
    """Return the values of a binary tree's nodes level by level, but alternate the direction for each level."""
    # Handle empty tree
    if not root:
        return []
    
    # Initialize BFS components
    queue = deque([root])  # BFS queue starting with root
    output = []            # Final result list
    flag = False           # Toggle for zigzag direction
    
    # Process each level
    while queue:
        inner = []  # Store current level's values
        
        for _ in range(len(queue)): # Process all nodes in cur lvl
            node = queue.popleft() # Get next node from queue
            
            # Add children to queue for next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
            # Collect node value for current level
            inner.append(node.val)
        
        # Apply zigzag logic based on flag
        if flag == False:
            output.append(inner)                    # Normal order
        else:
            output.append(list(reversed(inner)))    # Reversed order
        
        # Toggle direction for next level
        flag = not flag
    
    return output

# Example Tree:
#       3
#      / \
#     9   20
#        /  \
#       15   7

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(zigzag_level_order(root))  # Output: [[3], [20, 9], [15, 7]]

# ----------------------------------
# Pattern 2: Early termination BFS
# ----------------------------------

def min_depth(root):  # LC 111
    """Find minimum depth - BFS stops at first leaf"""
    if not root: # Handle empty tree
        return 0
    
    # Initialize BFS components
    q = deque([root])  # BFS queue with root
    depth = 1          # Track current depth
    
    # Level-by-level processing
    while q: 
        for _ in range(len(q)): # Process all nodes at cur level
            node = q.popleft() # Get next node from current level
            
            # Check if this is a leaf node (first leaf = minimum depth)
            if not node.left and not node.right:
                return depth  # Return depth immediately when leaf found
            
            # Add children to queue for next level
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        # Move to next level - increment depth
        depth += 1

# Example Tree:
#       3
#      / \
#     9   20
#        /  \
#       15   7

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(min_depth(root))  # Output: 2

# ----------------------------
# Pattern 3: Grid flood fill
# ----------------------------

def flood_fill(image, start_row, start_col, new_color):  # LC 733
    """Change connected pixels of same color"""
    num_rows, num_cols = len(image), len(image[0]) # Get grid dimensions
    original_color = image[start_row][start_col] # Store original color we're replacing
    
    # Early return if already the target color
    if original_color == new_color:
        return image
    
    # Initialize BFS with starting position
    queue = deque([(start_row, start_col)])
    
    # Direction vectors for 4-directional movement: up, down, left, right
    direction_deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Process all connected pixels
    while queue:
        current_row, current_col = queue.popleft() # Get current pixel position
        
        image[current_row][current_col] = new_color # Change current pixel to new color
        
        # Check all 4 neighboring pixels
        for delta_row, delta_col in direction_deltas:
            # Calculate neighbor position
            neighbor_row = current_row + delta_row
            neighbor_col = current_col + delta_col
            
            # Check if neighbor is valid and needs to be changed
            if (0 <= neighbor_row < num_rows and  # Row not OOB
                0 <= neighbor_col < num_cols and  # Col not OOB
                image[neighbor_row][neighbor_col] == original_color):  # Has original color -> add to queue to be changed to target color
                queue.append((neighbor_row, neighbor_col)) # add neighbor to be explored
    
    return image

image = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]
start_row, start_col = 1, 1
new_color = 2

print(flood_fill(image, start_row, start_col, new_color))
# Output:
# [
#     [2, 2, 2],
#     [2, 2, 0],
#     [2, 0, 1]
# ]


# -------------------------------
# Pattern 4: Multi-source BFS
# -------------------------------

def pacific_atlantic(heights):  # LC 417
    """Water flow to both oceans - start BFS from all ocean edges and return a list of coordinates [row, col] where water can flow to both the pacific and atlantic"""
    # Edge case: empty grid
    if not heights or not heights[0]:
        return []

    # Get grid dimensions
    rows, cols = len(heights), len(heights[0])

    # Initialize queues for BFS starting points (cells touching each ocean)
    pacific_queue = deque()
    atlantic_queue = deque()

    # Add all cells in the first and last columns
    for r in range(rows):
        pacific_queue.append((r, 0)) # Left column touches Pacific
        atlantic_queue.append((r, cols - 1))  # Right column touches Atlantic

    # Add all cells in the first and last rows
    for c in range(cols):
        pacific_queue.append((0, c)) # Top row touches Pacific
        atlantic_queue.append((rows - 1, c))  # Bottom row touches Atlantic

    # BFS function to find all cells reachable from a given ocean
    def bfs(queue):
        visited = set()
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]  # up, down, right, left

        while queue:
            r, c = queue.popleft()  # Get current position
            visited.add((r, c))     # Mark as visited

            # Check all 4 neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc  # Calc neighbor position

                # Check if neighbor is valid and water can flow FROM it TO current cell
                if (
                    0 <= nr < rows and # Neighbor row in bounds
                    0 <= nc < cols and # Neighbor col in bounds
                    (nr, nc) not in visited and # Not visited
                    heights[nr][nc] >= heights[r][c] # Water can flow uphill (reverse logic)
                ):
                    queue.append((nr, nc))  # Add neighbor for exploration

        return visited  # Return all cells reachable by this ocean

    # Run BFS from Pacific and Atlantic starting points
    pacific_reachable = bfs(pacific_queue)   # Returns cells that can reach Pacific
    atlantic_reachable = bfs(atlantic_queue) # Returns cells that can reach Atlantic

    # Find cells reachable by both oceans
    result = []
    for r in range(rows):
        for c in range(cols):
            # Cell must be reachable by both oceans
            if (r, c) in pacific_reachable and (r, c) in atlantic_reachable:
                result.append([r, c])

    return result


# FN Calls
heights = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4]
]

print(pacific_atlantic(heights))
# Output: [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]

# =============================================================================
# BFS NUANCES & PROBLEM-SPECIFIC INSIGHTS
# =============================================================================

#  ----------------------------------------------------------------------------------------------------
# NUANCE 1: You must process corresponding nodes from two trees simultaneously, carefully handling None cases and ensuring structural and value equality at every step.
#  ----------------------------------------------------------------------------------------------------

def isSameTree(self, p, q): # BFS
        queue = deque([(p, q)])  # Always wrap root nodes/tuples in a list when creating a deque so it's iterable

        while queue:
            node1, node2 = queue.popleft()  # Pop off pair of nodes p, q

            if not node1 and not node2:  # Both nodes are None, continue checking -> Tree still equal
                continue
            if not node1 or not node2:  # If only one is None, trees are different
                return False
            if node1.val != node2.val:  # Different values -> trees are different
                return False

            # Add left children and right children to the queue
            queue.append((node1.left, node2.left))
            queue.append((node1.right, node2.right))

        return True  # If we never return False, the trees are identical

# Ex. 1
#           1              1
#         /   \          /   \
#        2     3        2     3

p = TreeNode(1, TreeNode(2), TreeNode(3))
q = TreeNode(1, TreeNode(2), TreeNode(3))
print(isSameTree(p, q))

# Ex. 2
#           1              1
#         /                  \
#        2                    2

p2 = TreeNode(1, TreeNode(2), None)
q2 = TreeNode(1, None, TreeNode(2))
print(isSameTree(p2, q2))

# Ex. 3
#           1              1
#         /   \          /   \
#        2     1        1     2

p3 = TreeNode(1, TreeNode(2), TreeNode(1))
q3 = TreeNode(1, TreeNode(1), TreeNode(2))
print(isSameTree(p3, q3))

# =============================================================================
# TIME & SPACE COMPLEXITY ANALYSIS
# =============================================================================
"""
TIME COMPLEXITY:
- Tree BFS: O(N) where N = number of nodes
  Each node visited exactly once
  
- Grid BFS: O(M×N) where M×N = grid dimensions  
  Each cell visited at most once
  
- Graph BFS: O(V + E) where V = vertices, E = edges
  Visit each vertex once, examine each edge once

SPACE COMPLEXITY:
- Queue space: O(W) where W = maximum width of tree/graph
  Tree: can be O(N) for complete binary tree (last level has N/2 nodes)
  Grid: O(min(M,N)) for typical patterns
  
- Visited set: O(N) to store all visited nodes
- Total: O(N) in most cases

BFS vs DFS space comparison:
- BFS queue can grow large (stores entire level)
- DFS recursion stack depth = O(H) where H = height
- For balanced trees: BFS uses more space
- For skewed trees: DFS uses more space
"""

# =============================================================================
# KEY TAKEAWAYS FOR INTERVIEWS
# =============================================================================
"""
1. Always check for empty input first
2. Use deque for efficient queue operations (O(1) append/popleft)
3. Track visited nodes to avoid cycles (except in trees)
4. Process entire levels when level information is needed
5. Consider multi-source BFS for problems with multiple starting points
6. BFS guarantees shortest path - use when minimum distance/steps needed
7. Early termination in BFS can save significant time
8. Handle None/boundary cases carefully in tree problems
"""

# =============================================================================
# Additional Patterns & Problems to Consider
# =============================================================================

'''
994
542
934
513
662
'''