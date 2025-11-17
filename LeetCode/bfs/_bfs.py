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
            
            if (0 <= new_row < rows and 
                0 <= new_col < cols and 
                (new_row, new_col) not in visited):
                
                visited.add((new_row, new_col))
                queue.append((new_row, new_col))
    
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

# ================================================================
# PATTERN 1: SINGLE-SOURCE BFS (SHORTEST PATH/LEVEL ORDER)
# PATTERN EXPLANATION: Starting from a single source node or cell, explore outward level by level.
# BFS visits nodes in order of increasing distance from the source, guaranteeing that the first time a node is reached, it's via the shortest path. Process can be organized by levels or simply track distance.
#
# TYPICAL STEPS:
# 1. Initialize queue with starting node/cell
# 2. Mark start as visited
# 3. While queue not empty:
#    - Dequeue current node
#    - Process/check current node
#    - Add unvisited neighbors to queue
#    - Mark neighbors as visited
# 4. Track distance/level if needed
#
# Applications: Shortest path, minimum depth, level order traversal, nearest exit, minimum steps.
# ================================================================

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class SingleSourceBFS: # PART A: TREE BFS
    """
    Problem: Given the root of a binary tree, return the level order traversal of its nodes' values (i.e., from left to right, level by level).
    
    TC: O(n) - visit each node exactly once
    SC: O(w) - queue stores nodes at widest level w (worst case n/2 for complete tree)
    
    How it works:
    1. Use queue for BFS, process nodes level by level
    2. Capture level_size = len(queue) to know how many nodes in current level
    3. Process exactly that many nodes before moving to next level
    4. Children of current level become the next level
    """
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]: # LC 102
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
                level.append(node.val) # Append "level_size" nodes to curr lvl
                
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
sol = SingleSourceBFS()
tree_root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print("Level order:", sol.levelOrder(tree_root))  # [[3], [9,20], [15,7]]

class SingleSourceBFS2: # PART B: GRID BFS (SHORTEST PATH)
    """
    Problem: Given an n x n binary matrix grid, return the length of the shortest clear path from top-left (0,0) to bottom-right (n-1,n-1). A clear path has all cells = 0.
    
    You can move in 8 directions (horizontal, vertical, diagonal).
    If no path exists, return -1.
    
    TC: O(n²) - visit each cell at most once
    SC: O(n²) - queue and visited tracking
    
    How it works:
    1. Start BFS from (0,0) with distance 1
    2. Explore all 8 directions from current cell
    3. First arrival at destination = shortest path (BFS guarantee)
    4. Mark visited by modifying grid (or use visited set)
    """
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int: # LC 1091
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
                if (0 <= new_row < n and 
                    0 <= new_col < n and 
                    grid[new_row][new_col] == 0): # 0 -> unvisited
                    
                    grid[new_row][new_col] = 1  # Mark visited
                    queue.append((new_row, new_col, dist + 1))
        
        return -1  # No path found

sol = SingleSourceBFS2()
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


# ================================================================
# PATTERN 2: MULTI-SOURCE BFS
# PATTERN EXPLANATION: Begin BFS exploration from multiple starting points simultaneously rather than a single source. All sources start at the same initial distance/time and spread outward together in sync.

# Used when you need to find the minimum distance to ANY of several sources, or when multiple origins spread/affect their surroundings at the same rate.

# TYPICAL STEPS:
# 1. Initialize queue with ALL source nodes/cells
# 2. Mark all sources as visited
# 3. Process BFS level by level (each level = one unit of distance/time)
# 4. Spread from all current positions simultaneously
# 5. Track what changes or count what's affected
#
# Applications: Rotting oranges, walls and gates, fire spreading, infection spread, 01 matrix.
# ================================================================

class MultiSourceBFS: 
    """
    Problem: You are given an m x n grid where:
    - 0 = empty cell
    - 1 = fresh orange
    - 2 = rotten orange
    
    Every minute, fresh oranges adjacent (4-directionally) to rotten oranges become rotten.
    Return minimum minutes until no fresh oranges remain. Return -1 if impossible.
    
    TC: O(rows * cols) - visit each cell once
    SC: O(rows * cols) - queue can contain all cells
    
    How it works:
    1. Add ALL initially rotten oranges to queue (multi-source start)
    2. Count fresh oranges initially
    3. BFS spreads rot level by level (each level = 1 minute)
    4. Decrease fresh count as oranges rot
    5. Check if any fresh oranges remain unreachable
    """
    def orangesRotting(self, grid: List[List[int]]) -> int: # LC 994
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        
        # Initialize: find all rotten oranges and count fresh
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))  # Multi-source initialization
                elif grid[r][c] == 1:
                    fresh_count += 1 # Initial num of fresh oranges
        
        # Edge case: no fresh oranges
        if fresh_count == 0:
            return 0
        
        minutes = 0 # Track minutes elapsed
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # BFS: process level by level (each level = 1 minute)
        while queue and fresh_count > 0:
            minutes += 1
            level_size = len(queue)  # Process entire level at once
            
            for _ in range(level_size):
                row, col = queue.popleft()
                
                # Spread rot to 4 adjacent cells
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    
                    if (0 <= new_row < rows and 
                        0 <= new_col < cols and 
                        grid[new_row][new_col] == 1):  # Fresh orange
                        
                        grid[new_row][new_col] = 2  # Make rotten
                        fresh_count -= 1 # Decrease fresh oranges
                        queue.append((new_row, new_col))
        
        return minutes if fresh_count == 0 else -1 

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


# ================================================================
# PATTERN 3: BFS WITH EXTENDED STATE
# PATTERN EXPLANATION: Track more than just position - include additional information as part of the state.
# State becomes a tuple like (position, extra_data) where extra_data might be keys collected, obstacles broken, moves remaining, etc. The visited set must track the COMPLETE state, not just position, because arriving at the same position with different additional information represents different scenarios.
#
# TYPICAL STEPS:
# 1. Define state as tuple: (position, additional_info)
# 2. Initialize queue with starting state
# 3. Use visited set that tracks FULL state tuple
# 4. When generating neighbors:
#    - Update position AND additional info
#    - Check if new state already visited
# 5. Process until goal state reached or queue exhausted
#
# Applications: Lock combinations, collecting keys, obstacle elimination, turn limits, resource tracking.
# ================================================================

class ExtendedState:
    """
    Problem: You have a lock with 4 circular wheels (each 0-9).
    Lock starts at "0000". Each move turns one wheel up or down by 1. You are given a list of combinations that are "deadends" (forbidden - can't pass through).
    
    Return minimum turns to reach target, or -1 if impossible.
    
    TC: O(10^4 * 8) - at most 10,000 states, each generates 8 neighbors
    SC: O(10^4) - visited set stores all possible combinations
    
    How it works:
    1. Treat each 4-digit combination as a node
    2. State = (combination, turns) - track both position and distance
    3. Generate 8 neighbors per state (turn each of 4 wheels up/down)
    4. BFS finds shortest path from "0000" to target
    5. Skip deadends and already-visited combinations
    """
    def openLock(self, deadends: List[str], target: str) -> int: # LC 752
        # Edge Cases
        if "0000" in deadends: # Starting combo in deadends
            return -1
        if target == "0000": # Starting combo is target
            return 0
        
        dead = set(deadends) # Turn deadends to set for 0(1) lookup
        visited = {"0000"} # Mark starting position in visited set
        queue = deque([("0000", 0)])  # (combination, turns)
        
        def get_neighbors(combo):
            """Generate all 8 possible next combinations"""
            neighbors = []
            for i in range(4):  # Iterate over 4 wheels
                digit = int(combo[i])
                
                # Turn wheel up (9 wraps to 0)
                up = str((digit + 1) % 10)
                neighbors.append(combo[:i] + up + combo[i+1:])
                
                # Turn wheel down (0 wraps to 9)
                down = str((digit - 1) % 10)
                neighbors.append(combo[:i] + down + combo[i+1:])
            
            return neighbors
        
        while queue:
            combo, turns = queue.popleft()
            
            # Iterate over 8 next combos -> call fn, return list
            for next_combo in get_neighbors(combo): # of 8 combos
                # Skip if deadend or already visited
                if next_combo in dead or next_combo in visited:
                    continue # Do not add neighbor -> BFS blocked
                
                # Check if reached target
                if next_combo == target:
                    return turns + 1
                
                # Add to queue for exploration with extended state
                visited.add(next_combo)
                queue.append((next_combo, turns + 1))
        
        return -1  # Target unreachable

# Lock wheels: [0][0][0][0]
# Target: "0202"
# Deadends: ["0201", "0101", "0102", "1212", "2002"]
#
# Path: 0000 → 1000 → 1100 → 1200 → 1201 → 1202 → 0202
# Turns: 6

sol = ExtendedState()
print(sol.openLock(["0201","0101","0102","1212","2002"], "0202"))  # 6
print(sol.openLock(["8888"], "0009"))  # 1
print(sol.openLock(["8887","8889","8878","8898","8788","8988","7888","9888"], "8888"))  # -1


# ================================================================
# PATTERN 4: IMPLICIT GRAPH BFS
# PATTERN EXPLANATION: The graph structure is not explicitly provided. Instead, generate neighbors/next states on-the-fly based on problem rules. Each state is treated as a node, and transitions between states form edges. This transforms problems into graph traversal where you define what "neighbors" means for your problem domain.
#
# TYPICAL STEPS:
# 1. Define what constitutes a "state" in your problem
# 2. Define rules for generating valid next states (neighbors)
# 3. Implement get_neighbors() function based on problem rules
# 4. Run standard BFS treating states as nodes
# 5. Track visited states to avoid cycles
#
# Applications: Word transformation, sliding puzzles, DNA mutation, string transformations, state machines.
# ================================================================

class GraphBFS:
    """
    Problem: A gene string is an 8-character string from 'A', 'C', 'G', 'T'.
    To mutate from startGene to endGene, change one character at a time.
    Each intermediate mutation must be in the bank. Return minimum mutations needed, or -1.

    Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
    Output: 2
    
    TC: O(N * M * 4) where N = bank size, M = gene length (8)
        For each gene, try 4 possible characters at each position
    SC: O(N) - visited set and queue store genes from bank
    
    How it works:
    1. Treat each gene as a node in implicit graph
    2. Generate neighbors by changing one character to A/C/G/T
    3. Only consider neighbors that exist in bank
    4. BFS finds shortest path from start to end gene
    5. Return number of mutations (path length - 1)
    """
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int: # LC 433
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
            neighbors = []
            for i in range(len(gene)):  # Try mutating each position
                for char in genes:  # Try each possible character
                    if char != gene[i]:  # Skip if no actual change
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
            
            # Explore all valid next states (one mutation away)
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
