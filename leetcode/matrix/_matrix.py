"""
=================================================================
MATRIX COMPLETE GUIDE
=================================================================

WHAT IS A MATRIX?
-----------------
A Matrix is a 2D array (grid) of elements arranged in rows and columns. In programming, it's typically represented as a list of lists (Python) or array of arrays. Matrices are fundamental for grid-based problems, image processing, game boards, and graph representations.

Key characteristics:
- 2D structure: matrix[row][column] or matrix[i][j]
- Dimensions: m * n (m rows, n columns)
- Zero-indexed: first element is matrix[0][0]
- Can be square (m = n) or rectangular (m ≠ n)
- Common operations: traverse, search, transform, modify

Matrix representation in Python:
```
matrix = [
    [1, 2, 3],    # Row 0
    [4, 5, 6],    # Row 1
    [7, 8, 9]     # Row 2
]
# Access: matrix[row][col]
# matrix[0][0] = 1, matrix[1][2] = 6, matrix[2][2] = 9
```

When to use Matrix:
- Grid-based problems (game boards, maps, images)
- Graph representation (adjacency matrix)
- Dynamic programming on 2D space
- Image/signal processing
- Pathfinding and traversal problems

Common Matrix problem types:
- Traversal patterns (spiral, diagonal, zigzag)
- DFS/BFS on grid (islands, flood fill, paths)
- Matrix transformations (rotate, flip, transpose)
- Search in sorted matrix
- Grid DP (paths, minimum sum)
- Simulation (Game of Life, cellular automata)
- In-place modifications

MATRIX CORE TEMPLATES
======================
"""

from typing import List
from collections import deque

# ================================================================
# BASIC MATRIX TRAVERSAL TEMPLATE
# ================================================================
def matrix_traversal_template(matrix):
    """
    Basic patterns for traversing a matrix
    TC: O(m * n) - visit each cell once
    SC: O(1) - no extra space
    """
    if not matrix or not matrix[0]: # Edge case: empty matrix or empty first row
        return
    
    rows, cols = len(matrix), len(matrix[0])
    
    # 1. Row-major order (left to right, top to bottom)
    for r in range(rows):
        for c in range(cols):
            print(matrix[r][c], end=' ')
    
    # 2. Column-major order (top to bottom, left to right)
    for c in range(cols):
        for r in range(rows):
            print(matrix[r][c], end=' ')
    
    # 3. Diagonal traversal (top-left to bottom-right)
    for d in range(rows + cols - 1):
        for r in range(rows):
            c = d - r
            if 0 <= c < cols:
                print(matrix[r][c], end=' ')

# ================================================================
# MATRIX DFS TEMPLATE
# ================================================================
def matrix_dfs_template(matrix):
    """
    DFS traversal in 4 directions, only visiting non-zero cells.
    TC: O(m * n) - visit each cell once
    SC: O(m * n) - visited set stores each cell once, stack holds at most 4 * (m * n) items (pushes 4 neighbors per cell without pre-visit check)
    """
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = set()
    stack = [(0, 0)] # Tuple of (row, col), stack for LIFO DFS -> O(1) pops

    while stack:
        r, c = stack.pop() # DFS: LIFO order

        if (r < 0 or r >= rows or c < 0 or c >= cols or # Rows/cols out of bounds
            (r, c) in visited or matrix[r][c] == 0): # Already visited or cell is zero (not valid)
            continue

        visited.add((r, c)) # Mark current cell as visited

        for dr, dc in directions: # Explore 4 directions
            stack.append((r + dr, c + dc)) # Add neighbors to stack for DFS


# ================================================================
# MATRIX BFS TEMPLATE
# ================================================================
def matrix_bfs_template(matrix):
    """
    BFS traversal in 4 directions, only visiting non-zero cells.
    TC: O(m * n) - visit each cell once
    SC: O(m * n) - visited set stores each cell once, queue holds at most O(m + n) items at once (only the current frontier)
    """
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = set()
    queue = deque([(0, 0)]) # Tuple of (row, col), Queue for popleft BFS -> O(1) pops

    while queue:
        r, c = queue.popleft() # BFS: FIFO order

        if (r < 0 or r >= rows or c < 0 or c >= cols or # Rows/cols out of bounds
            (r, c) in visited or matrix[r][c] == 0): # Already visited or cell is zero (not valid)
            continue

        visited.add((r, c)) # Mark current cell as visited

        for dr, dc in directions: # Explore 4 directions
            queue.append((r + dr, c + dc)) # Add neighbors to queue for BFS
"""
MATRIX COMPLEXITY REFERENCE
=============================

+---------------------------+------------------+------------------+
| Pattern                   | Time             | Space            |
+---------------------------+------------------+------------------+
| Basic Traversal           | O(m * n)         | O(1)             |
| DFS Grid                  | O(m * n)         | O(m * n)         |
| BFS Grid                  | O(m * n)         | O(m * n)         |
| Spiral Order              | O(m * n)         | O(m * n)         |
| Matrix Rotation (90°)     | O(m * n)         | O(1) in-place    |
| Matrix Search (sorted)    | O(m + n)         | O(1)             |
| Binary Search in Matrix   | O(log(m * n))    | O(1)             |
| Grid DP                   | O(m * n)         | O(m * n)         |
+---------------------------+------------------+------------------+

m = number of rows
n = number of columns

WHAT EACH PATTERN IS:
- Basic Traversal: walking through every cell in a fixed order (row by row, column by
  column, or diagonally) — just a systematic way to visit each square once.
- DFS Grid: starting at a cell and diving as deep as possible into a neighbor before
  backtracking, marking cells visited so you don't loop — used to explore a connected
  blob of cells, like an island.
- BFS Grid: starting at a cell and exploring outward one ring of neighbors at a time
  using a queue — used when you need the shortest number of steps to reach a cell.
- Spiral Order: walking the outer edge of the grid, then peeling that ring away and
  walking the next ring in, spiraling inward until every cell is visited.
- Matrix Rotation (90°): turning the grid without building a new one, by mirroring it
  across the diagonal (swap rows/columns) and then reversing rows or columns.
- Matrix Search (sorted): starting at a corner where one direction is guaranteed
  bigger and the other guaranteed smaller, then using that fact to rule out an entire
  row or column with every step instead of checking cells one by one.
- Binary Search in Matrix: treating the sorted grid as if it were one long sorted
  list and binary searching over it, converting back and forth between a single index
  and a (row, col) position.
- Grid DP: filling in the grid cell by cell, where each cell's answer is built from
  the answers already computed in the cells above and to the left of it.

NOTES:
- DFS/BFS are O(m * n) space due to recursion stack / queue
- Spiral is O(m * n) space only because of the output list — extra space is O(1)
- Matrix search O(m + n): start at top-right corner, each step eliminates a row or column
- Binary search O(log(m*n)): only works if entire matrix is sorted row-by-row end-to-end
- Grid DP can be optimized to O(n) space by keeping only the previous row
"""

"""
===============
MATRIX PATTERNS
===============
"""

"""
================================================================
PATTERN 1: MATRIX DFS/BFS (FLOOD FILL & CONNECTED COMPONENTS)
PATTERN EXPLANATION: Use DFS or BFS to explore connected cells in a grid. Mark visited
cells to avoid infinite loops. For DFS, recursively explore neighbors. For BFS, use queue
for level-by-level exploration. Track visited with set or modify matrix in-place. Common
for counting islands, flood fill, and finding connected regions.

Applications: Number of islands, flood fill, surrounded regions, word search.
================================================================
"""

class MatrixDFSBFS:
    """
    Problem: Given an m x n 2D binary grid which represents a map of '1's (land) and
    '0's (water), return the number of islands. An island is surrounded by water and
    formed by connecting adjacent lands horizontally or vertically.

    Example:
        Input: grid = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ]
        Output: 3

    Giveaway: "return the number of islands" formed by connecting adjacent '1's is
    asking you to count separate connected blobs in a grid — needing to fully mark
    off one blob before moving to the next unvisited land cell is what signals
    DFS/BFS with a visited set rather than a simple per-cell scan.

    Steps:
    1. Iterate through every cell in the grid
    2. When an unvisited '1' is found, increment the island count
    3. Run DFS from that cell:
       a. Skip if out of bounds, already visited, or cell is '0'
       b. Mark cell as visited
       c. Push all 4 neighbors onto the stack
    4. Return the total island count
    """
    def numIslands(self, grid: List[List[str]]) -> int:  # LC 200 - DFS
        """
        - TC: O(m * n) - visit each cell at most once
        - SC: O(m * n) - visited set; stack holds at most 4 * (m * n) items (pushes 4 neighbors per cell without pre-visit check)
        """
        if not grid or not grid[0]: # Edge case: empty grid or empty first row
            return 0

        num_rows, num_cols = len(grid), len(grid[0]) 
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        visited = set() # Track visited cells to avoid cycles
        island_count = 0 # Count of islands found

        def dfs(start_row, start_col):
            stack = [(start_row, start_col)]
            visited.add((start_row, start_col))

            while stack:
                current_row, current_col = stack.pop()  # LIFO order

                for d_row, d_col in directions:
                    neighbor_row = current_row + d_row 
                    neighbor_col = current_col + d_col

                    if (
                        0 <= neighbor_row < num_rows and # Row and col bounds check
                        0 <= neighbor_col < num_cols and
                        grid[neighbor_row][neighbor_col] == '1' and # Only visit land
                        (neighbor_row, neighbor_col) not in visited # Land not visited
                    ):
                        stack.append((neighbor_row, neighbor_col)) # Add unvisted land
                        visited.add((neighbor_row, neighbor_col)) # to explore & mark

        for row in range(num_rows): # Iterate through each cell in the grid
            for col in range(num_cols):
                if grid[row][col] == '1' and (row, col) not in visited: # Unvisited land
                    dfs(row, col) # Explore entire island and mark visited
                    island_count += 1 # Increment island count 

        return island_count

    # Example trace:
    # grid = [["1","1","0","0","0"],
    #         ["1","1","0","0","0"],
    #         ["0","0","1","0","0"],
    #         ["0","0","0","1","1"]]
    #
    # (0,0): '1' found, island_count=1, DFS marks (0,0),(0,1),(1,0),(1,1) → visited
    # (0,1): already visited → skip
    # (0,2): '0' → skip
    # ... continue ...
    # (2,2): '1' found, island_count=2, DFS marks (2,2) → visited
    # ... continue ...
    # (3,3): '1' found, island_count=3, DFS marks (3,3),(3,4) → visited
    #
    # Output: 3

    def orangesRotting(self, grid: List[List[int]]) -> int:  # LC 994 - BFS
        """
        Problem: Given an m x n grid where 0 = empty, 1 = fresh orange, 2 = rotten orange.
        Every minute, any fresh orange adjacent (4 directions) to a rotten orange becomes rotten. Return the minimum number of minutes until no fresh oranges remain, or -1 if impossible.

        Example:
            Minute 0      Minute 1      Minute 2      Minute 3       Minute 4
           [[2, 1, 1],   [[2, 2, 1],   [[2, 2, 2],   [[2, 2, 2],   [[2, 2, 2],
            [1, 1, 0],    [2, 1, 0],    [2, 2, 0],    [2, 2, 0],    [2, 2, 0]
            [1, 0, 1]]    [1, 0, 1]]    [1, 0, 1]]    [2, 0, 1]]    [2, 0, 2]]

            Output: 4

        - TC: O(m * n) - every cell is added to the queue at most once
        - SC: O(m * n) - queue holds at most O(m + n) items at once (current frontier only)
        """
        rows, cols = len(grid), len(grid[0])
        queue = deque()

        # Add all initially rotten oranges to queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0)) # Each orange is a tuple (row, col, time_elapsed)

        max_time = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            row, col, time = queue.popleft()
            max_time = max(max_time, time) # Update max time

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                if (0 <= new_row < rows and
                    0 <= new_col < cols and
                    grid[new_row][new_col] == 1): # Fresh orange found  

                    grid[new_row][new_col] = 2 # Mark as rotten
                    queue.append((new_row, new_col, time + 1)) # Add to queue with incremented time

        # After BFS, check if any fresh oranges remain
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1

        return max_time

    # Example trace (orangesRotting):
    # grid = [[2,1,1],
    #         [1,1,0],
    #         [0,1,1]]
    #
    # Init: queue = [(0,0,t=0)]  ← only rotten orange
    #
    # t=0: pop (0,0) → rot (0,1) and (1,0) → queue = [(0,1,1),(1,0,1)]
    # t=1: pop (0,1) → rot (0,2) and (1,1) → queue = [(1,0,1),(0,2,2),(1,1,2)]
    # t=1: pop (1,0) → (1,1) already rotten → queue = [(0,2,2),(1,1,2)]
    # t=2: pop (0,2) → no fresh neighbors → queue = [(1,1,2)]
    # t=2: pop (1,1) → rot (2,1)          → queue = [(2,1,3)]
    # t=3: pop (2,1) → rot (2,2)          → queue = [(2,2,4)]
    # t=4: pop (2,2) → no fresh neighbors → queue = []
    #
    # No fresh oranges remain → return max_time = 4 ✓

sol = MatrixDFSBFS()
print("Number of Islands:", sol.numIslands([["1","1","0"],["1","1","0"],["0","0","1"]]))  # 2
print(sol.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])) # 4

"""
================================================================
PATTERN 2: MATRIX TRANSFORMATION (IN-PLACE)
PATTERN EXPLANATION: Complex matrix transformations can be decomposed into two primitive operations: transpose (swap matrix[i][j] with matrix[j][i] across the diagonal) and flip (reverse rows or columns). Any rotation can be expressed as a combination of these two primitives, allowing O(1) space in-place modification without creating a new matrix.

Rotation cheatsheet:
90° clockwise         = transpose + reverse each row
90° counter-clockwise = transpose + reverse each column
180°                  = reverse each row + reverse each column

Applications: Rotate Image (LC 48), Transpose Matrix (LC 867),
flipping/mirroring images, any problem requiring in-place matrix rotation.
================================================================
"""

class MatrixTransformation:
    """
    Problem: You are given an n x n 2D matrix representing an image. Rotate the image
    by 90 degrees clockwise in-place.

    Example:
        Input: matrix = [[1,2,3],
                         [4,5,6],
                         [7,8,9]]

        Key insight: 90° clockwise = Transpose + Reverse each row

        After transpose:        After reverse rows:
        [[1,4,7],               [[7,4,1],
         [2,5,8],                [8,5,2],
         [3,6,9]]                [9,6,3]]

    - TC: O(n²) - touch each cell once for transpose, once for reverse
    - SC: O(1) - in-place transformation

    Giveaway: "rotate the image by 90 degrees... in-place" rules out building a new
    matrix, and a rotation being expressible as mirroring across the diagonal plus
    reversing rows is the specific insight that turns "rotate" into the
    transpose-then-reverse recipe rather than a from-scratch coordinate remap.

    Steps:
    1. Transpose the matrix in-place:
       a. Iterate over the upper triangle only (i from 0 to n, j from i+1 to n)
       b. Swap matrix[i][j] with matrix[j][i]
    2. Reverse each row in-place:
       a. For each row i, call matrix[i].reverse()
    """
    def rotate(self, matrix: List[List[int]]) -> None:  # LC 48
        n = len(matrix)

        # Step 1: Transpose — swap across the diagonal (upper triangle only)
        for i in range(n):
            for j in range(i + 1, n): # start j at i+1 to avoid swapping pairs twice
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for i in range(n):
            matrix[i].reverse()

    # Example trace:
    # matrix = [[1,2,3],
    #           [4,5,6],
    #           [7,8,9]]
    #
    # Step 1: Transpose (upper triangle swaps only)
    # i=0, j=1: 2 ↔ 4 → [[1,4,7],[2,5,8],[3,6,9]]  (conceptually building)
    # i=0, j=2: 3 ↔ 7
    # i=1, j=2: 6 ↔ 8
    # Result: [[1,4,7],
    #          [2,5,8],
    #          [3,6,9]]
    #
    # Step 2: Reverse each row
    # Row 0: [1,4,7] → [7,4,1]
    # Row 1: [2,5,8] → [8,5,2]
    # Row 2: [3,6,9] → [9,6,3]
    #
    # Final: [[7,4,1],
    #         [8,5,2],
    #         [9,6,3]] ✓

sol = MatrixTransformation()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(sol.rotate(matrix)) # [[7,4,1],[8,5,2],[9,6,3]]

"""
================================================================
PATTERN 3: MATRIX SEARCH (SORTED MATRIX)
PATTERN EXPLANATION: When a matrix has independently sorted rows and columns, start from the top-right corner (or bottom-left) and eliminate one row or column per step. If the current value is too large, move left to eliminate that column. If too small, move down to eliminate that row. This works because the corner is the unique position where one direction is guaranteed larger and one is guaranteed smaller, giving you a clear decision at every step.

Corner cheatsheet:
Top-right:    value too big → move left (c -= 1), too small → move down (r += 1)
Bottom-left:  value too big → move up (r -= 1),  too small → move right (c += 1)

Applications: Search a 2D Matrix II (LC 240), find k-th smallest in sorted matrix
(LC 378), count elements less than target, any search on row/col sorted matrix.
================================================================
"""

class MatrixSearch:
    """
    Problem: Search for a target in an m x n matrix where each row is sorted
    left to right and each column is sorted top to bottom.

    Example:
        Input: matrix = [[1,  4,  7,  11, 15],
                         [2,  5,  8,  12, 19],
                         [3,  6,  9,  16, 22],
                         [10, 13, 14, 17, 24],
                         [18, 21, 23, 26, 30]]
            target = 5

        Start at top-right (15):
        15 > 5 → move left  → 11
        11 > 5 → move left  → 7
        7  > 5 → move left  → 4
        4  < 5 → move down  → 5
        5 == 5 → found!

        Output: True

    - TC: O(m + n) - each step eliminates one row or column
    - SC: O(1)

    Giveaway: "each row is sorted left to right and each column is sorted top to
    bottom" (rather than the whole matrix being one sorted sequence) is the specific
    detail that rules out binary search and instead points to starting at a corner
    where every step can confidently eliminate a whole row or column.

    Steps:
    1. Start at top-right corner: r=0, c=cols-1
    2. While r < rows and c >= 0:
       a. If matrix[r][c] == target, return True
       b. If matrix[r][c] > target, move left (c -= 1) — entire column eliminated
       c. If matrix[r][c] < target, move down (r += 1) — entire row eliminated
    3. Return False if target not found
    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:  # LC 240
        if not matrix or not matrix[0]: # Edge case: empty matrix or empty first row
            return False

        rows, cols = len(matrix), len(matrix[0])
        r, c = 0, cols - 1  # Start at top-right corner

        while r < rows and c >= 0: # While within bounds
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                c -= 1  # Eliminate this column — everything below is also too large
            else:
                r += 1  # Eliminate this row — everything left is also too small

        return False

    # Example trace (target=5):
    # r=0, c=4 → value=15: 15 > 5, c=3
    # r=0, c=3 → value=11: 11 > 5, c=2
    # r=0, c=2 → value=7:   7 > 5, c=1
    # r=0, c=1 → value=4:   4 < 5, r=1
    # r=1, c=1 → value=5:   5 == 5, return True ✓

sol = MatrixSearch()
print("Search Matrix II:", sol.searchMatrix(
    [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5))  # True

"""
================================================================
PATTERN 4: GRID DYNAMIC PROGRAMMING (PATH PROBLEMS)
PATTERN EXPLANATION: Use DP on grid where each cell's value depends on neighboring cells (typically top, left, or diagonal). Build solution from top-left to bottom-right. Each cell represents optimal solution to reach that position. Common for counting paths, finding minimum/maximum path sums, or optimization with movement constraints.

Applications: Unique paths, minimum path sum, dungeon game, triangle paths.
================================================================
"""

class GridDP:
    """
    Problem: Given an m x n grid filled with non-negative numbers, find a path from
    top-left to bottom-right which minimizes the sum of numbers along the path.
    You can only move down or right at each step.

    Example:
        grid = [[1,3,1],
                [1,5,1],
                [4,2,1]]

        Minimum path: 1→3→1→1→1 = 7
        (Not 1→1→4→2→1 = 9 or 1→1→5→1→1 = 9)

        DP table shows minimum sum to reach each cell:
        [[1, 4, 5],
         [2, 7, 6],
         [6, 8, 7]]

        Output: 7

    TC: O(m * n) - fill entire grid once
    SC: O(m * n) - DP table (can optimize to O(min(m,n)))

    Giveaway: "find a path... which minimizes the sum" with movement restricted to
    only down or right means every cell's best value depends only on the cell above
    and the cell to the left — that top-left-to-bottom-right dependency is what
    signals filling a grid DP table instead of exploring every path with DFS.

    Steps:
    1. Create a dp table of the same size as grid
    2. Set dp[0][0] = grid[0][0] as the base case
    3. Fill the first row: dp[0][c] = dp[0][c-1] + grid[0][c] (can only come from left)
    4. Fill the first column: dp[r][0] = dp[r-1][0] + grid[r][0] (can only come from top)
    5. Fill the rest: dp[r][c] = grid[r][c] + min(dp[r-1][c], dp[r][c-1]) (choose min path from top or left)
    6. Return dp[rows-1][cols-1]
    """
    def minPathSum(self, grid: List[List[int]]) -> int:  # LC 64
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        
        # Create DP table
        dp = [[0] * cols for _ in range(rows)] 
        
        # Base case: top-left corner filled with grid value
        dp[0][0] = grid[0][0]
        
        # Fill first row (can only come from left)
        for c in range(1, cols): # Fix index 0 for row
            dp[0][c] = dp[0][c-1] + grid[0][c] # Previous dp cost + current grid cost
        
        # Fill first column (can only come from top)
        for r in range(1, rows): # fix index 0 for row
            dp[r][0] = dp[r-1][0] + grid[r][0] # Previous dp cost + current grid cost
        
        # Fill rest of table
        for r in range(1, rows):
            for c in range(1, cols):
                # Current value + minimum of coming from top or left
                dp[r][c] = grid[r][c] + min(dp[r-1][c], dp[r][c-1])
        
        return dp[rows-1][cols-1]

# Example trace:
# grid = [[1,3,1],
#         [1,5,1],
#         [4,2,1]]
#
# Initialize: dp[0][0] = 1
#
# First row:
# dp[0][1] = 1 + 3 = 4
# dp[0][2] = 4 + 1 = 5
# dp = [[1,4,5],
#       [0,0,0],
#       [0,0,0]]
#
# First column:
# dp[1][0] = 1 + 1 = 2
# dp[2][0] = 2 + 4 = 6
# dp = [[1,4,5],
#       [2,0,0],
#       [6,0,0]]
#
# Fill rest:
# dp[1][1] = 5 + min(4, 2) = 5 + 2 = 7
# dp[1][2] = 1 + min(5, 7) = 1 + 5 = 6
# dp[2][1] = 2 + min(6, 7) = 2 + 6 = 8
# dp[2][2] = 1 + min(6, 8) = 1 + 6 = 7
# 
# Final: dp = [[1,4,5],
#              [2,7,6],
#              [6,8,7]]
#
# Output: dp[2][2] = 7

sol = GridDP()
print("Minimum Path Sum:", sol.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))  # 7
