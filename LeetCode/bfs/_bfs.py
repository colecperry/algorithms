"""
=================================================================
BREADTH-FIRST SEARCH (BFS) COMPLETE GUIDE
=================================================================

WHAT IS BFS?
-----------
Breadth-First Search (BFS) is a graph traversal algorithm that explores nodes level by level, visiting all nodes at distance d before visiting nodes at distance d+1.

Key characteristics:
- Uses a QUEUE (FIFO - First In, First Out) data structure
- Explores all neighbors at current level before going deeper
- Guarantees shortest path in unweighted graphs

BFS CORE TEMPLATES
==================
"""

from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ================================================================
# BFS TREE TEMPLATE
# ================================================================
def bfs_tree_template(root):
    """
    Basic tree BFS template - no visited set needed (trees have no cycles)
    - TC: O(n) -> n = number or total nodes -> BFS visits each node exactly once and not revisited (trees have no cycles)
    - SC: O(w) -> w is maximum width of any level of a tree since BFS queues store all nodes from current level before moving to next level
    """
    if not root:
        return []
    
    queue = deque([root])
    result = []
    
    while queue:
        node = queue.popleft()
        
        # Process current node
        result.append(node.val)
        
        # Add children to queue (left then right - order matters for some problems)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result

# ================================================================
# BFS MATRIX TEMPLATE
# ================================================================
def bfs_matrix_template(matrix, start_row, start_col):
    """
    Basic matrix BFS template with visited tracking
    - TC: O(rows * cols) -> each cell in the matrix is visited at most once due to visited set tracking
    - SC: O(rows * cols) -> visited set can store up to (rows * cols) tuples, queue can store up to O(min(rows, cols)) worst case per BFS level
    """
    if not matrix or not matrix[0]: # Empty matrix or empty data in first row
        return []
    
    rows, cols = len(matrix), len(matrix[0])
    queue = deque([(start_row, start_col)]) # Use a queue for BFS (.popleft)
    visited = set([(start_row, start_col)])
    result = []
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
    
    while queue:
        row, col = queue.popleft() # <- BFS line pops from front and explores oldest first (FIFO)
        
        # Process current cell
        result.append(matrix[row][col])
        
        # Add valid neighbors
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < rows and 
                0 <= new_col < cols and 
                (new_row, new_col) not in visited):
                
                visited.add((new_row, new_col))
                queue.append((new_row, new_col))
    
    return result

"""
WHEN TO USE BFS VS DFS
======================

Use BFS when:
- Need shortest path/minimum steps in unweighted graphs
- Need to process nodes level by level
- Want guaranteed minimum distance/depth
- Multi-source problems (start from multiple points)

Use DFS when:
- Memory is limited (stack uses less space than queue)
- Need to explore all paths (backtracking)
- Tree problems without level requirements
- Recursive solutions are more natural

COMMON BFS PATTERNS
===================
"""

# ================================================================
# PATTERN 1: LEVEL-BY-LEVEL PROCESSING
# PATTERN EXPLANATION: Process entire levels at once, maintaining level structure in results.
# Key insight: BFS naturally visits nodes level by level due to its FIFO queue structure. By capturing level_size = len(queue) at the start of each iteration, you can process exactly one complete level before moving to the next.
# Applications: Level order traversal, zigzag traversal, level averages, right view.
# ================================================================

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]: # LC 102
    '''
    Problem: Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
    TC: O(n) -> each node visited once
    SC:
        - O(n) -> output list stores all n node values
        - O(w) -> queue stores nodes from current level where w is the widest level
        - Combined: O(n) > O(w), total = O(n)
    '''
    if not root: # Edge case - empty tree
        return []
    queue = deque([root]) # BFS queue
    output = []
    while queue:
        inner = [] # collect BFS level
        for _ in range(len(queue)): # travese full BFS level
            node = queue.popleft() # Pop and process curr node
            inner.append(node.val) 
            if node.left: # Append children if non null (next level)
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        output.append(inner) # Append the full level each iteration
    
    return output

#            3
#           / \
#          /   \
#         9    20
#             /  \
#           15    7

# Test level processing
test_root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))) # [[3],[9,20],[15,7]]
print("Level order:", levelOrder(test_root))

# ================================================================
# PATTERN 2: EARLY TERMINATION BFS
# PATTERN EXPLANATION: Stop BFS as soon as target condition is met, avoiding unnecessary exploration.
# Key insight: BFS guarantees first occurrence is at minimum distance/level.
# Applications: Minimum depth, shortest path, first target found.
# ================================================================

def min_depth_early_termination(root): # LC 111
    """
    Problem: Given a binary tree, find its minimum depth. The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
    TC: O(n) worst case -> visit all nodes if the first leaf is at maximum depth
    SC: O(w) where w = max width of any tree level, queue holds nodes from each level in the tree
    """
    if not root: # Edge case - empty tree has a min depth of 0
        return 0
    
    queue = deque([root]) # Initialize BFS queue with the root
    depth = 1 # track min depth
    
    while queue:
        level_size = len(queue) # Capture the current level
        
        for _ in range(level_size): # Level based logic -> process all nodes in the level
            node = queue.popleft()
            
            # Early termination: first leaf found is minimum depth
            if not node.left and not node.right:
                return depth
            
            if node.left: # Appending children of each node at current level adds next level to the queue
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        depth += 1  # Move to next level only after processing current level
    
    return depth

#               3
#              / \
#             9   20
#                /  \
#               15   17

root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

print("Minimum depth:", min_depth_early_termination(root))

# ================================================================
# PATTERN 3: MULTI-SOURCE BFS - 994
# PATTERN EXPLANATION: Start BFS from multiple source points simultaneously in the same structure, useful for problems where multiple starting conditions exist or need to find closest distance to any source.
# Key insight: Add all sources to initial queue, they all start at distance 0.
# Applications: Rotten oranges, walls and gates, pacific atlantic.
# ================================================================

def orangesRotting(grid: List[List[int]]) -> int:
    '''
    # Problem: You are given an m x n grid where each cell can have one of three values: 0 representing an empty cell, 1 representing a fresh orange, or 2 representing a rotten orange. Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten. Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
    # TC: Initial scan to find rotten oranges: O(rows * cols)
        # BFS traversal: O(rows * cols) - each cell visited once
        # Final check for remaining fresh oranges: O(rows * cols)
        # Total: O(rows * cols)
    # SC: O(rows * cols) worst case -> queue if grid is all rotten oranges 
    '''
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    
    # Add all initially rotten oranges to queue
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0)) # row, col, time elapsed
    
    max_time = 0   # Track max time elapsed to spread rot to max area
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Matrix BFS goes 4 directions
    
    # BFS to spread rot
    while queue:
        row, col, time = queue.popleft() # Explore multi-direction level
        max_time = max(max_time, time) # Update max time
        
        for dr, dc in directions: # Explore 4 directions from curr 
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < rows and # OOB check
                0 <= new_col < cols and 
                grid[new_row][new_col] == 1):  # Find a fresh orange
                
                grid[new_row][new_col] = 2  # Make rotten
                queue.append((new_row, new_col, time + 1)) # Add cell to explore with updated elapsed time 
    
    # Check if any fresh oranges remain
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:  # If any fresh oranges remain, return -1
                return -1
    
    return max_time

#         Minute 0         Minute 1         Minute 2         Minute 3           Minute 4
#        [[2, 1, 1],      [[2, 2, 1],      [[2, 2, 2],      [[2, 2, 2],        [[2, 2, 2],
#         [1, 1, 0],       [2, 1, 0],       [2, 2, 0],       [2, 2, 0],         [2, 2, 0]
#         [1, 0, 1]]       [1, 0, 1]]       [1, 0, 1]]       [2, 0, 1]]         [2, 0, 2]]
#

print(orangesRotting([[2,1,1],
                      [1,1,0],
                      [0,1,1]])) # 4

print(orangesRotting([[2,1,1],
                      [0,1,1],
                      [1,0,1]])) # -1

# ================================================================
# PATTERN 4: CONNECTED REGION EXPLORATION
# PATTERN EXPLANATION: Explore/process connected regions or simultaneously compare multiple structures.
# Key insight: Use BFS to systematically discover and process related elements, whether exploring connected components in one structure or comparing corresponding elements across multiple structures.
# Applications: Island counting, flood fill, tree comparison, tree symmetry, connected components.
# ================================================================

def numIslands(grid: List[List[str]]) -> int:
    '''
    # Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
    '''
    if not grid: # edge case -> empty grid
        return 0

    num_rows, num_cols = len(grid), len(grid[0]) # track num of rows and cols for OOB checks
    visited = set() # track visited elements so we don't revisit eles -> infinite loop caused by continuing to explore elements we have already explored and adding their neighbors over and over
    island_count = 0 # output

    def bfs(start_row, start_col): # Nested fn keeps exploring neighbors until island disconnects
        queue = deque([(start_row, start_col)]) # append the first ele (tuple of rows and cols)
        visited.add((start_row, start_col)) # add curr ele to visited set (tuple of rows and cols)

        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)] # up, down, left, right (tuples of rows and cols)

        while queue: # Keep exploring island
            current_row, current_col = queue.popleft() # pop the ele & get it's row and col

            for d_row, d_col in directions: # Matrix BFS explores 4 directions
                neighbor_row = current_row + d_row # update row to neighbor's row
                neighbor_col = current_col + d_col # update col to neighbor's col

                if (
                    0 <= neighbor_row < num_rows and # if row in bounds
                    0 <= neighbor_col < num_cols and # if col in bounds
                    grid[neighbor_row][neighbor_col] == '1' and # if we find land (island continues) 
                    (neighbor_row, neighbor_col) not in visited # and it's not already visited
                ):
                    queue.append((neighbor_row, neighbor_col)) # append neighbor if land is connected
                    visited.add((neighbor_row, neighbor_col)) # add the node to visited

    for row in range(num_rows): # iterate through each ele in the matrix ([row][col]) and explore if we find new unvisited land
        for col in range(num_cols):
            if grid[row][col] == '1' and (row, col) not in visited: # if we find a new land
                bfs(row, col) # explore it's neighbors until we can't go further
                island_count += 1 # increment island count

    return island_count

    
print(numIslands([
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
])) # 1

print(numIslands(
    [["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
])) # 3

"""
BFS COMPLEXITY ANALYSIS
=======================

TIME COMPLEXITY:
- Tree BFS: O(n) - visit each node exactly once
- Grid BFS: O(rows × cols) - visit each cell at most once  
- Graph BFS: O(V + E) - visit each vertex once, examine each edge once

SPACE COMPLEXITY:
- Queue: O(w) where w = maximum width of tree/level
- Visited set: O(n) for nodes/cells visited
- Total: O(n) in most cases

BFS vs DFS Space Comparison:
- BFS: Queue can store entire level (wide trees use more space)
- DFS: Recursion stack depth equals height (deep trees use more space)
- Choose based on expected tree/graph structure

KEY INSIGHTS FOR INTERVIEWS
===========================

1. Always handle empty/null inputs first
2. Use deque for O(1) append/popleft operations
3. Track visited nodes/cells to prevent cycles (except pure trees)
4. Process entire levels when level information needed
5. Multi-source BFS: add all sources to initial queue
6. Early termination: first occurrence in BFS is guaranteed minimum
7. Simultaneous traversal: handle null cases carefully
8. Flood fill: check boundaries and conditions before adding to queue
"""