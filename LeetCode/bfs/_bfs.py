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
    - TC: O(rows * cols) -> each cell in the matrix is visited at most once (no revisits due to visited set tracking)
    - SC: O(rows * cols) -> visited set can store up to (rows * cols) tuples, queue can store up to O(min(rows, cols)) worst case per BFS level
    """
    if not matrix or not matrix[0]: # Empty matrix or empty data in first row
        return []
    
    rows, cols = len(matrix), len(matrix[0])
    queue = deque([(start_row, start_col)]) # Use a queue for BFS (.popleft)
    visited = set([(start_row, start_col)]) # Keeps us from re-visitng 
    result = []
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
    
    while queue:
        row, col = queue.popleft() # <- BFS line pops from front and explores oldest first (FIFO)
        
        # Process current cell
        result.append(matrix[row][col])
        
        # Add valid neighbors
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < rows and  # Row not OOB
                0 <= new_col < cols and  # Col not OOB
                (new_row, new_col) not in visited): # Not already visited
                
                visited.add((new_row, new_col)) # Mark new cell as visited
                queue.append((new_row, new_col)) # & add it to the queue to explore
    
    return result

# ================================================================
# BFS GRAPH TEMPLATE
# ================================================================
def bfs_graph_template(graph, start_node):
    """
    Basic graph BFS template with visited tracking using adjacency list
    
    Graph format: {node: [list of neighbors]}
    Example: {'A': ['B', 'C'], 'B': ['D'], 'C': ['F'], ...}
    
    TC: O(V + E) - visit each vertex once (V), explore each edge once (E)
    SC: O(V) - visited set stores up to V nodes, queue stores up to V nodes worst case
    """
    if not graph or start_node not in graph:  # Empty graph or invalid start
        return []
    
    queue = deque([start_node])  # Use a queue for BFS (.popleft)
    visited = set([start_node])  # Keeps us from re-visiting
    result = []
    
    while queue:
        node = queue.popleft()  # <- BFS line: pops from front and explores oldest first (FIFO)
        
        # Process current node
        result.append(node)
        
        # Add unvisited neighbors to queue
        for neighbor in graph[node]: # Visit node's neighbors (edges)
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor) # Add edge to be explored
    
    return result


# Test graph
test_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'F'],
    'D': ['B', 'E'],
    'E': ['D', 'G'],
    'F': ['C', 'G'],
    'G': ['E', 'F']
}

#       A
#      / \
#     B   C
#    /     \
#   D       F
#    \     /
#     E - G

print("BFS from 'A':", bfs_graph_template(test_graph, 'A'))
# Output: ['A', 'B', 'C', 'D', 'F', 'E', 'G']

"""
BFS TIME COMPLEXITY GUIDE
=========================

TREE: O(n)
----------
- n = total nodes
- Visit each node exactly once
- No visited set needed (no cycles)

MATRIX: O(rows * cols)
----------------------
- Each cell visited at most once
- Visited set prevents re-processing
- Think of it as O(n) where n = total cells

GRAPH: O(V + E)
---------------
- V = vertices (nodes)
- E = edges (connections)
- Visit each vertex once (V), traverse each edge once (E)
- For dense graphs, almost every node connects to every other node (E ≈ V²): simplifies to O(V²)
- For sparse graphs where each node has 1 to 2 edges (E ≈ V): simplifies to O(V)

WHY BFS IS EFFICIENT
--------------------
The visited set is the key. Without it:

Brute force (no visited tracking):
- Same cell/node can be reached via multiple paths
- Each path explored separately → exponential blowup
- Matrix example: O(4^(rows*cols)) — 4 directions, unlimited revisits
- Graph example: O(V!) — every permutation of nodes

With visited tracking:
- Each cell/node processed exactly once
- "Already seen? Skip." — eliminates redundant work
- Converts exponential → linear

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

from collections import deque
from typing import List, Optional

"""
================================================================
PATTERN 1: TREE LEVEL-ORDER BFS
================================================================
PATTERN EXPLANATION: Traverse a tree level by level, processing all nodes at 
depth d before moving to depth d+1. No visited set needed since trees have no 
cycles. Use level_size = len(queue) to process one complete level per iteration.

TYPICAL STEPS:
1. Initialize queue with root
2. While queue not empty:
   - Capture level_size = len(queue)
   - Process exactly level_size nodes (one full level)
   - Add children to queue (they form the next level)
3. Collect results per level if needed

KEY CHARACTERISTICS:
- No visited set (trees are acyclic)
- level_size loop to batch process each level
- Result is often List[List] (values grouped by level)

Applications: Level order traversal, zigzag traversal, right side view, 
minimum/maximum depth, level averages.

Examples: LC 102, 103, 107, 111, 199, 515, 637
================================================================
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TreeLevelOrderBFS: # PART A: TREE BFS
    """
    Problem: Given the root of a binary tree, return the level order traversal of its nodes' values (i.e., from left to right, level by level).

    # Ex. 1
    #            3
    #           / \
    #          /   \
    #         9    20
    #             /  \
    #           15    7
    #
    # Input: root = [3,9,20,null,null,15,7]
    # Output: [[3],[9,20],[15,7]]
    
    How it works:
    1. Use queue for BFS, process nodes level by level
    2. Capture level_size = len(queue) to know how many nodes in current level
    3. Process exactly that many nodes before moving to next level
    4. Children of current level become the next level
    """
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]: # LC 102
        """
        TC: O(n) - visit each node exactly once
        SC: O(w) - queue stores nodes at widest level w (worst case n/2 for complete tree)
        """
        if not root:  # Edge case - empty tree
            return []
        
        queue = deque([root])
        result = []
        
        while queue:
            level = [] # Capture nodes on each level & then reset
            level_size = len(queue)  # Capture current level size
            
            # Process all nodes at current level
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val) # Append all nodes to curr lvl
                
                # Add children (they form the next level)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(level) # Append each BFS level
        
        return result

#            3
#           / \
#          9   20
#             /  \
#            15   7
#
# Level 0: [3]
# Level 1: [9, 20]
# Level 2: [15, 7]
# Output: [[3], [9,20], [15,7]]

# Test tree BFS
sol = TreeLevelOrderBFS()
tree_root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print("Level order:", sol.levelOrder(tree_root))  # [[3], [9,20], [15,7]]


"""
================================================================
PATTERN 2: SHORTEST PATH BFS
================================================================
PATTERN EXPLANATION: Find the minimum distance/steps from a starting point to 
a target in a grid or graph. BFS guarantees the first time we reach the target 
is via the shortest path. Requires visited tracking to avoid cycles.

TYPICAL STEPS:
1. Initialize queue with starting position (and distance 0 or 1)
2. Mark start as visited
3. While queue not empty:
   - Dequeue current position and distance
   - If current is target, return distance (early termination)
   - Add unvisited neighbors to queue with distance + 1
   - Mark neighbors as visited immediately when adding to queue
4. Return -1 if queue exhausts without finding target

KEY CHARACTERISTICS:
- Visited set required (grids/graphs can have cycles)
- Early termination when target found
- Returns single value (distance), not grouped levels
- Mark visited WHEN ADDING to queue, not when processing

Applications: Shortest path in grid, nearest exit, minimum moves, 
maze solving, minimum steps to reach target.

Examples: LC 1091, 542, 1926, 934, 317, 909
================================================================
"""

class ShortestPathBFS: # PART B: GRID BFS (SHORTEST PATH)
    """
    Problem: Given an n x n binary matrix grid, return the length of the shortest clear path from top-left (0,0) to bottom-right (n-1,n-1). A clear path has all cells = 0.
    
    You can move in 8 directions (horizontal, vertical, diagonal).
    If no path exists, return -1.
    
    How it works:
    1. Start BFS from (0,0) with distance 1
    2. Explore all 8 directions from current cell
    3. First arrival at destination = shortest path (BFS guarantee)
    4. Mark visited by modifying grid (or use visited set)
    """
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int: # LC 1091
        """
        TC: O(n²) - visit each cell at most once -> row (n) * col (n)
        SC: O(n)
            - O(1) - visited tracking done by marking grid in place
            - O(n) - queue stores at most O(n) cells (the minimum side of the matrix is the BFS frontier/diagonal)
        """
        n = len(grid)
        
        # Edge cases
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1  # Start or end blocked
        if n == 1:
            return 1  # Special case: 1x1 grid
        
        # 8 directions: 4 cardinal + 4 diagonal
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1), # up, down, left, right
            (-1, -1), (-1, 1), (1, -1), (1, 1) # diagonals
        ]
        
        # Start BFS from first cell
        queue = deque([(0, 0, 1)])  # (row, col, distance)
        grid[0][0] = 1  # Mark visited (reuse grid to save space)
        
        while queue:
            row, col, dist = queue.popleft()
            
            # Early termination: reached destination
            if row == n - 1 and col == n - 1:
                return dist  # First arrival = shortest
            
            # Explore 8 directions
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                # Check bounds, clear cell (0), and unvisited
                if (0 <= new_row < n and          # Row in bounds
                    0 <= new_col < n and          # Col in bounds
                    grid[new_row][new_col] == 0): # 0 -> unvisited
                    
                    grid[new_row][new_col] = 1    # Mark new cell as visited
                    queue.append((new_row, new_col, dist + 1)) # Add cell to explore
        
        return -1  # No path found

sol = ShortestPathBFS()
print(sol.shortestPathBinaryMatrix([
        [0,1,0],
        [0,0,0],
        [0,0,0]
]))  # 3
print(sol.shortestPathBinaryMatrix([
    [1,0,0],
    [1,1,0],
    [1,1,0]
]))  # -1

"""
================================================================
PATTERN 3: MULTI-SOURCE BFS
PATTERN EXPLANATION: Begin BFS exploration from multiple starting points simultaneously rather than a single source. All sources start at the same initial distance/time and spread outward together in sync.

Used when you need to find the minimum distance to ANY of several sources, or when multiple origins spread/affect their surroundings at the same rate.

TYPICAL STEPS:
1. Initialize queue with ALL starting source nodes/cells
2. Mark all sources as visited
3. Process BFS level by level (each level = one unit of distance/time)
4. Spread from all current positions simultaneously
5. Track what changes or count what's affected

Applications: Rotting oranges, walls and gates, fire spreading, infection spread, 01 matrix.

Examples: LC 994, 286, 542, 1162, 934
================================================================
"""

class MultiSourceBFS: 
    """
    Problem: You are given an m x n grid where:
    - 0 = empty cell
    - 1 = fresh orange
    - 2 = rotten orange
    
    Every minute, fresh oranges adjacent (4-directionally) to rotten oranges become rotten.
    Return minimum minutes until no fresh oranges remain. Return -1 if impossible.
    
    How it works:
    1. Add ALL initially rotten oranges to queue (multi-source start)
    2. Count fresh oranges initially
    3. BFS spreads rot level by level (each level = 1 minute)
    4. Decrease fresh count as oranges rot
    5. Check if any fresh oranges remain unreachable
    """
    def orangesRotting(self, grid: List[List[int]]) -> int: # LC 994
        """
        TC: O(rows * cols) - visit each cell once in the initialization loop -> (O(rows * cols)), and each cell enters the BFS queue at most once (we mark it as '2') -> (O(rows * cols))
        SC: O(min(rows, cols)) - queue holds BFS frontier
        """
        rows, cols = len(grid), len(grid[0])
        queue = deque()  # BFS queue
        fresh_count = 0  # Number of fresh oranges left
        
        # Initialize: find all rotten oranges and count fresh
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:  # Found a rotten orange
                    queue.append((r, c, 0))  # Multi-source initialization (row, col, time)
                elif grid[r][c] == 1:
                    fresh_count += 1  # Initial num of fresh oranges
        
        # Edge case: no fresh oranges
        if fresh_count == 0:
            return 0
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # BFS explores 4 directions
        max_time = 0  # Track minutes elapsed
        
        # BFS: spread rot from all rotten oranges simultaneously
        while queue:
            row, col, time = queue.popleft()
            
            # Spread rot to 4 adjacent cells
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                if (0 <= new_row < rows and  # OOB checks
                    0 <= new_col < cols and 
                    grid[new_row][new_col] == 1):  # If we find a fresh orange
                    
                    grid[new_row][new_col] = 2  # Make it rotten (so we don't revisit)
                    fresh_count -= 1  # Decrease fresh oranges
                    max_time = time + 1  # Update max time
                    queue.append((new_row, new_col, max_time))  # Append with incremented time
        
        return max_time if fresh_count == 0 else -1

#  Minute 0      Minute 1      Minute 2      Minute 3      Minute 4
# [2, 1, 1]     [2, 2, 1]     [2, 2, 2]     [2, 2, 2]     [2, 2, 2]
# [1, 1, 0]  →  [2, 1, 0]  →  [2, 2, 0]  →  [2, 2, 0]  →  [2, 2, 0]
# [0, 1, 1]     [0, 1, 1]     [0, 2, 1]     [0, 2, 2]     [0, 2, 2]
#
# Two sources at (0,0) and (0,1) spread simultaneously

sol = MultiSourceBFS()
print("Minutes to rot:", sol.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))  # 4
print("Impossible:", sol.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))  # -1
print("Already done:", sol.orangesRotting([[0,2]]))  # 0

"""
================================================================
PATTERN 4: BFS WITH EXTENDED STATE
PATTERN EXPLANATION: Track more than just position - include additional information as part of the state.
State becomes a tuple like (position, extra_data) where extra_data might be keys collected, obstacles broken, moves remaining, etc. The visited set must track the COMPLETE state, not just position, because arriving at the same position with different additional information represents different scenarios.

KEY DISTINCTION: The extra data must affect REVISITING. If you can visit (row, col) multiple times with different states, it's extended state. If time/distance is just metadata you're carrying (each cell still visited once), it's NOT extended state.

TYPICAL STEPS:
1. Define state as tuple: (position, additional_info)
2. Initialize queue with starting state
3. Use visited set that tracks FULL state tuple
4. When generating neighbors:
   - Update position AND additional info
   - Check if new state already visited
5. Process until goal state reached or queue exhausted

Applications: Lock combinations, collecting keys, obstacle elimination, turn limits, resource tracking.
================================================================
"""

class ExtendedStateBFS:
    """
    Problem: Given m x n grid (0 = empty, 1 = obstacle), find shortest path from 
    top-left to bottom-right. You can eliminate AT MOST k obstacles.

    Ex. 
    Input: grid = 
    [[0,0,0],
     [1,1,0],
     [0,0,0],
     [0,1,1],
     [0,0,0]], k = 1
    Output: 6
    Explanation: 
    The shortest path without eliminating any obstacle is 10.
    The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
    """
    def shortestPath(self, grid: List[List[int]], k: int) -> int:  # LC 1293
        """
        TC: O(m * n * k) - each cell can be visited with k+1 different states - one for each possible remaining value: 
        Cell (2, 3) could be visited as:
        - (2, 3, 0)
        - (2, 3, 1)
        - (2, 3, 2)
        - ...
        - (2, 3, k)
        SC: O(m * n * k) - visited set can store all possible states ->  (row, col, remaining) tuples
        """
        rows, cols = len(grid), len(grid[0])
        
        # Edge case: already at destination
        if rows == 1 and cols == 1:
            return 0
        
        # (row, col, remaining, dist) — remaining affects revisiting (state), dist is just a counter
        queue = deque([(0, 0, k, 0)])
        
        # Initialize visited set -> Only track (row, col, remaining) — same cell with more eliminations left is worth revisiting
        visited = {(0, 0, k)}
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            row, col, remaining, dist = queue.popleft()
            
            for dr, dc in directions: # try 4 directions
                new_row, new_col = row + dr, col + dc
                
                # OOB check
                if not (0 <= new_row < rows and 0 <= new_col < cols):
                    continue
                
                # Calculate new remaining eliminations from current cell being explored
                new_remaining = remaining - grid[new_row][new_col]  # Subtract 1 if obstacle, 0 if empty
                
                # Skip if out of eliminations
                if new_remaining < 0:
                    continue
                
                # Check if reached destination
                if new_row == rows - 1 and new_col == cols - 1:
                    return dist + 1
                
                # EXTENDED STATE CHECK: have I been to this cell with this many eliminations left?
                if (new_row, new_col, new_remaining) not in visited:
                    visited.add((new_row, new_col, new_remaining))
                    queue.append((new_row, new_col, new_remaining, dist + 1))
        
        return -1  # No path found


# Example walkthrough:
# Grid:        k = 1 (can break 1 wall)
# [0, 0, 0]
# [1, 1, 0]
# [0, 0, 0]
#
# Path A: (0,0) → (0,1) → (0,2) → (1,2) → (2,2)  = 4 steps, 0 walls broken
# Path B: (0,0) → (1,0) → (2,0) → (2,1) → (2,2)  = 4 steps, 1 wall broken
#
# Both valid! BFS finds shortest.

sol = ExtendedStateBFS()
print(sol.shortestPath([[0,0,0],[1,1,0],[0,0,0], [0,1,1], [0,0,0]], 1))  # 6
print(sol.shortestPath([[0,0,0],[1,1,0],[0,0,0]], 1))  # 4

"""
================================================================
PATTERN 5: IMPLICIT GRAPH BFS
PATTERN EXPLANATION: The graph structure is not explicitly provided. Instead, generate neighbors/next states on-the-fly based on problem rules. Each state is treated as a node, and transitions between states form edges. This transforms problems into graph traversal where you define what "neighbors" means for your problem domain.

TYPICAL STEPS:
1. Define what constitutes a "state" in your problem
2. Define rules for generating valid next states (neighbors)
3. Implement get_neighbors() function based on problem rules
4. Run standard BFS treating states as nodes
5. Track visited states to avoid cycles

Applications: Word transformation, sliding puzzles, DNA mutation, string transformations, state machines.
================================================================
"""

class GraphBFS:
    """
    Problem: A gene string is an 8-character string from 'A', 'C', 'G', 'T'.
    To mutate from startGene to endGene, change one character at a time.
    Each intermediate mutation must be in the bank. Return minimum mutations needed, or -1.

    Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
    Output: 2
    
    How it works:
    1. Treat each gene as a node in implicit graph
    2. Generate neighbors by changing one character to A/C/G/T
    3. Only consider neighbors that exist in bank
    4. BFS finds shortest path from start to end gene
    5. Return number of mutations (path length - 1)
    """
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int: # LC 433
        """
        TC: O(N * M * 4) where N = bank size, M = gene length (8)
        For each gene, try 4 possible characters at each position
        SC: O(N) - visited set and queue store genes from bank
        """
        if endGene not in bank:  # Target must be reachable (in bank)
            return -1
        
        bank_set = set(bank)  # Convert to set for O(1) lookup 
        visited = {startGene}  # Track explored genes to avoid cycles
        queue = deque([(startGene, 0)])  # BFS queue: (current_gene, mutation_count)
        genes = ['A', 'C', 'G', 'T']  # Possible characters for gene string
        
        def get_neighbors(gene):
            """
            Generate next states (neighbors) by trying all single-character mutations. This is the "implicit" part - we create edges on-the-fly based on rules.
            """
            neighbors = [] # list of neighbors -> one char different than input
            for i in range(len(gene)):  # Try mutating each position
                for char in genes:  # Try each possible character
                    if char != gene[i]:  # Skip if same char
                        neighbor = gene[:i] + char + gene[i+1:]  # Build new gene string
                        if neighbor in bank_set:  # Only valid if exists in bank
                            neighbors.append(neighbor)
            return neighbors
        
        # Standard BFS loop
        while queue:
            gene, mutations = queue.popleft()
            
            # Early termination: reached target
            if gene == endGene:
                return mutations
            
            # Explore all valid next states (one mutation away & exist in bank)
            for next_gene in get_neighbors(gene):
                if next_gene not in visited:  # Haven't explored this gene yet
                    visited.add(next_gene)  # Mark as explored
                    queue.append((next_gene, mutations + 1))  # Add to queue with incremented count
        
        return -1  # Exhausted all possibilities, no path exists

# Start: "AACCGGTT"
# End:   "AACCGGTA"
# Bank: ["AACCGGTA"]
#
# Mutation: AACCGGTT → AACCGGTA (change one character)
# Mutations needed: 1

sol = GraphBFS()
print(sol.minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]))  # 1
print(sol.minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA","AACCGCTA","AAACGGTA"]))  # 2
print(sol.minMutation("AACCGGTT", "AACCGGTA", []))  # -1
