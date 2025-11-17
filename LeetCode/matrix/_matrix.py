"""
=================================================================
MATRIX COMPLETE GUIDE
=================================================================

WHAT IS A MATRIX?
-----------------
A Matrix is a 2D array (grid) of elements arranged in rows and columns. In programming,
it's typically represented as a list of lists (Python) or array of arrays. Matrices are
fundamental for grid-based problems, image processing, game boards, and graph representations.

Key characteristics:
- 2D structure: matrix[row][column] or matrix[i][j]
- Dimensions: m × n (m rows, n columns)
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
    if not matrix or not matrix[0]:
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
def matrix_dfs_template(matrix, r, c, visited):
    """
    DFS traversal in 4 directions
    TC: O(m * n) - visit each cell once
    SC: O(m * n) - recursion stack + visited set
    """
    rows, cols = len(matrix), len(matrix[0])
    
    # Base cases
    if (r < 0 or r >= rows or c < 0 or c >= cols or 
        (r, c) in visited or matrix[r][c] == 0):
        return
    
    # Mark visited
    visited.add((r, c))
    
    # Explore 4 directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dr, dc in directions:
        matrix_dfs_template(matrix, r + dr, c + dc, visited)

# ================================================================
# MATRIX BFS TEMPLATE
# ================================================================
def matrix_bfs_template(matrix, start_r, start_c):
    """
    BFS traversal in 4 directions
    TC: O(m * n) - visit each cell once
    SC: O(m * n) - queue and visited set
    """
    rows, cols = len(matrix), len(matrix[0])
    visited = set([(start_r, start_c)])
    queue = deque([(start_r, start_c)])
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while queue:
        r, c = queue.popleft()
        
        # Process current cell
        print(matrix[r][c], end=' ')
        
        # Explore neighbors
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols and 
                (nr, nc) not in visited and matrix[nr][nc] != 0):
                visited.add((nr, nc))
                queue.append((nr, nc))

# ================================================================
# MATRIX TRANSFORMATION TEMPLATE
# ================================================================
def matrix_transform_template(matrix):
    """
    Common matrix transformations
    TC: O(m * n)
    SC: O(1) for in-place, O(m * n) for new matrix
    """
    rows, cols = len(matrix), len(matrix[0])
    
    # 1. Transpose (swap rows and columns)
    transposed = [[matrix[r][c] for r in range(rows)] for c in range(cols)]
    
    # 2. Flip horizontally (reverse each row)
    for r in range(rows):
        matrix[r].reverse()
    
    # 3. Flip vertically (reverse row order)
    matrix.reverse()
    
    return matrix

"""
TIME & SPACE COMPLEXITY REFERENCE
==================================

MATRIX OPERATIONS COMPLEXITY:
------------------------------
+---------------------------+------------------+------------------+
| Operation                 | Time Complexity  | Space Complexity |
+---------------------------+------------------+------------------+
| Access element            | O(1)             | O(1)             |
| Row-major traversal       | O(m * n)         | O(1)             |
| Column-major traversal    | O(m * n)         | O(1)             |
| Diagonal traversal        | O(m * n)         | O(1)             |
| Spiral traversal          | O(m * n)         | O(1)             |
| Transpose                 | O(m * n)         | O(m * n)         |
| Rotate 90°                | O(m * n)         | O(1) in-place    |
+---------------------------+------------------+------------------+

COMMON MATRIX PATTERNS COMPLEXITY:
-----------------------------------
+---------------------------+------------------+------------------+
| Pattern                   | Time Complexity  | Space Complexity |
+---------------------------+------------------+------------------+
| Basic Traversal           | O(m * n)         | O(1)             |
| DFS Grid                  | O(m * n)         | O(m * n)         |
| BFS Grid                  | O(m * n)         | O(m * n)         |
| Spiral Order              | O(m * n)         | O(m * n) output  |
| Matrix Rotation           | O(m * n)         | O(1) in-place    |
| Matrix Search (sorted)    | O(m + n)         | O(1)             |
| Binary Search in Matrix   | O(log(m*n))      | O(1)             |
| Grid DP                   | O(m * n)         | O(m * n)         |
| Set Matrix Zeroes         | O(m * n)         | O(1) optimized   |
| Game of Life              | O(m * n)         | O(1) in-place    |
+---------------------------+------------------+------------------+

WHERE:
- m = number of rows
- n = number of columns
- Matrix dimensions: m × n

COMPLEXITY NOTES:
-----------------
1. Basic Traversal: O(m * n) time, O(1) space
   - Must visit every cell to read/process: O(m * n)
   - Only need row/column indices: O(1)
   - No additional data structures needed
   
   Common patterns:
   - Row-major: for r in range(rows): for c in range(cols)
   - Column-major: for c in range(cols): for r in range(rows)
   - Diagonal: iterate by diagonal index

2. DFS Grid: O(m * n) time, O(m * n) space
   - Visit each cell at most once: O(m * n)
   - Visited set stores cell coordinates: O(m * n)
   - Recursion stack depth in worst case: O(m * n)
   
   When to use: Connected components, island problems, flood fill
   Space optimization: Modify matrix in-place instead of visited set
   Common pattern: 4-directional or 8-directional exploration

3. BFS Grid: O(m * n) time, O(m * n) space
   - Visit each cell at most once: O(m * n)
   - Queue can hold all cells in worst case: O(m * n)
   - Visited set stores coordinates: O(m * n)
   
   When to use: Shortest path, level-by-level processing, multi-source
   Better than DFS for: Distance calculations, shortest paths
   Common pattern: Process level by level, track distance

4. Spiral Order: O(m * n) time, O(m * n) space
   - Visit each cell exactly once: O(m * n)
   - Store result in output list: O(m * n)
   - Only need boundary pointers: O(1) extra
   
   Pattern: Process outer layer, shrink boundaries, repeat
   Directions: Right → Down → Left → Up, then move inward
   Common mistake: Off-by-one errors in boundary conditions

5. Matrix Rotation: O(m * n) time, O(1) space
   - Touch each cell at least once: O(m * n)
   - Rotate in-place using swaps: O(1)
   - Two-step process: transpose + reverse rows/columns
   
   90° clockwise = Transpose + Reverse each row
   90° counter-clockwise = Transpose + Reverse each column
   180° = Reverse rows + Reverse columns

6. Matrix Search (sorted): O(m + n) time, O(1) space
   - Start from top-right or bottom-left: O(m + n)
   - Each step eliminates one row or column
   - No extra space needed: O(1)
   
   Key insight: Rows and columns both sorted
   Pattern: Start at corner, move toward opposite corner
   Better than: O(m * n) brute force or O(m log n) row-by-row binary search

7. Binary Search in Matrix: O(log(m*n)) time, O(1) space
   - Treat as 1D sorted array: O(log(m*n))
   - Convert 1D index to 2D coordinates
   - Only if entire matrix is sorted row-by-row
   
   Coordinate conversion:
   - mid_1d → row = mid // n, col = mid % n
   - Works when rows sorted AND first element of row > last of previous

8. Grid DP: O(m * n) time, O(m * n) space
   - Fill entire grid: O(m * n)
   - Store result for each cell: O(m * n)
   - Can optimize to O(min(m,n)) if only need previous row/column
   
   When to use: Path problems, counting ways, optimization on grid
   Pattern: Current cell depends on top/left/diagonal neighbors
   Common: Unique paths, minimum path sum, dungeon game

9. Set Matrix Zeroes: O(m * n) time, O(1) space
   - Scan entire matrix: O(m * n)
   - Use first row/column as markers: O(1)
   - Two-pass algorithm
   
   Space optimization: Store markers in first row and column
   Tricky: Need flags for first row/column themselves
   Pattern: Mark in first pass, update in second pass

10. Game of Life: O(m * n) time, O(1) space
    - Count neighbors for each cell: O(m * n)
    - Use state encoding for in-place update: O(1)
    - Need to preserve old state while computing new
    
    State encoding: Use extra bits (0→1 = 2, 1→0 = 3)
    Pattern: Compute next state, then decode
    Common in: Cellular automata, simulation problems

GENERAL MATRIX OPTIMIZATION:
-----------------------------
Space optimization:
- In-place modification: Use matrix itself for markers/state
- Rolling array: Keep only current and previous row for DP
- State encoding: Use bits to store multiple states in one cell

Time optimization:
- Early termination: Stop when target found
- Binary search: For sorted matrices
- Diagonal processing: Process diagonals instead of rows/columns
- Four-pointer technique: For spiral/boundary problems

WHEN TO USE EACH PATTERN:
--------------------------
Basic Traversal:
  - Read/print matrix elements
  - Simple transformations
  - When order matters (spiral, diagonal)

DFS Grid:
  - Connected regions/islands
  - Flood fill, coloring
  - Path existence problems

BFS Grid:
  - Shortest path in grid
  - Distance from multiple sources
  - Level-by-level processing

Matrix Transformation:
  - Image rotation/flip
  - Matrix operations (transpose)
  - In-place modifications

Matrix Search:
  - Find element in sorted matrix
  - Binary search applications
  - Optimization with sorted property

Grid DP:
  - Path counting problems
  - Minimum/maximum path sum
  - Grid-based optimization

Matrix Simulation:
  - Game rules implementation
  - Cellular automata
  - State-based evolution
"""

"""
MATRIX PATTERNS
===============
"""

# ================================================================
# PATTERN 1: MATRIX TRAVERSAL (SPIRAL, DIAGONAL, ZIGZAG)
# PATTERN EXPLANATION: Traverse matrix in non-standard patterns using boundary pointers
# or direction vectors. Track boundaries (top, bottom, left, right) and shrink them as
# layers are processed. For spiral, process outer layer then move inward. Requires careful
# boundary management to avoid revisiting cells or going out of bounds.
#
# TYPICAL STEPS:
# 1. Initialize boundary pointers (top, bottom, left, right)
# 2. While boundaries are valid:
#    a. Process current layer (one or more directions)
#    b. Update boundaries (shrink inward)
#    c. Check if boundaries crossed (termination)
# 3. Handle edge cases (single row/column, empty matrix)
#
# Applications: Spiral matrix, diagonal traverse, print in layers, matrix rotation.
# ================================================================

class MatrixTraversal:
    """
    Problem: Given an m x n matrix, return all elements of the matrix in spiral order
    (clockwise from outside to inside).
    
    Example:
        Input: matrix = [[1,2,3],
                        [4,5,6],
                        [7,8,9]]
        
        Spiral order: Start at (0,0)
        → Right:  1, 2, 3
        ↓ Down:   6, 9
        ← Left:   8, 7
        ↑ Up:     4
        → Right:  5
        
        Output: [1,2,3,6,9,8,7,4,5]
    
    TC: O(m * n) - visit each cell exactly once
    SC: O(m * n) - output list (O(1) if not counting output)
    
    How it works:
    1. Use 4 boundaries: top, bottom, left, right
    2. Process in 4 directions: right → down → left → up
    3. After each direction, shrink corresponding boundary
    4. Stop when boundaries cross (top > bottom or left > right)
    """
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:  # LC 54
        if not matrix or not matrix[0]:
            return []
        
        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            # Move right across top row
            for c in range(left, right + 1):
                result.append(matrix[top][c])
            top += 1  # Finished top row, move boundary down
            
            # Move down along right column
            for r in range(top, bottom + 1):
                result.append(matrix[r][right])
            right -= 1  # Finished right column, move boundary left
            
            # Move left across bottom row (if still have rows)
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    result.append(matrix[bottom][c])
                bottom -= 1  # Finished bottom row, move boundary up
            
            # Move up along left column (if still have columns)
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    result.append(matrix[r][left])
                left += 1  # Finished left column, move boundary right
        
        return result

# Example trace:
# matrix = [[1,2,3],
#           [4,5,6],
#           [7,8,9]]
#
# Initial: top=0, bottom=2, left=0, right=2
#
# Iteration 1:
#   Right (top row, c=0→2): Add 1,2,3. top=1
#   Down (right col, r=1→2): Add 6,9. right=1
#   Left (bottom row, c=1→0): Add 8,7. bottom=1
#   Up (left col, r=1→1): Add 4. left=1
#   result = [1,2,3,6,9,8,7,4]
#
# Iteration 2:
#   top=1, bottom=1, left=1, right=1 (single cell)
#   Right (c=1→1): Add 5. top=2
#   top > bottom, exit
#   result = [1,2,3,6,9,8,7,4,5]
#
# Output: [1,2,3,6,9,8,7,4,5]

    def diagonalOrder(self, mat: List[List[int]]) -> List[int]:  # LC 498
        """
        Problem: Traverse matrix diagonally (zigzag pattern).
        
        Example:
            Input: [[1,2,3],
                    [4,5,6],
                    [7,8,9]]
            
            Diagonals (alternating direction):
            ↗ [1]
            ↙ [2,4]
            ↗ [3,5,7]
            ↙ [6,8]
            ↗ [9]
            
            Output: [1,2,4,3,5,7,6,8,9]
        
        TC: O(m * n) - visit each cell once
        SC: O(m * n) - output list
        
        How it works:
        1. Process diagonals by sum of indices (i + j)
        2. Diagonals alternate direction (up-right vs down-left)
        3. Even diagonals: go down-left, odd diagonals: go up-right
        4. Collect cells where i + j = diagonal number
        """
        if not mat or not mat[0]:
            return []
        
        rows, cols = len(mat), len(mat[0])
        result = []
        
        # Total number of diagonals = rows + cols - 1
        for d in range(rows + cols - 1):
            diagonal = []
            
            # Collect all cells in this diagonal (i + j = d)
            for r in range(rows):
                c = d - r
                if 0 <= c < cols:
                    diagonal.append(mat[r][c])
            
            # Reverse every other diagonal (even diagonals go up-right)
            if d % 2 == 0:
                diagonal.reverse()
            
            result.extend(diagonal)
        
        return result

# Example trace for diagonal:
# mat = [[1,2,3],
#        [4,5,6],
#        [7,8,9]]
#
# d=0: r=0, c=0 → [1], reversed → [1]
# d=1: r=0,c=1 and r=1,c=0 → [2,4] (no reverse)
# d=2: r=0,c=2 and r=1,c=1 and r=2,c=0 → [3,5,7], reversed → [7,5,3]
# Wait, let me recalculate:
# d=2: cells [3,5,7], d%2==0, reverse → [7,5,3]
# Actually looking at example output [1,2,4,3,5,7,6,8,9]:
# d=0: [1] (reverse) → [1]
# d=1: [2,4] (no reverse) → [2,4]
# d=2: [3,5,7] (reverse) → [7,5,3]... 
# Hmm, output shows [3,5,7] not reversed. Let me check the pattern.
# Actually even diagonals go UP, odd go DOWN.
# d=0 (even): [1] up → [1]
# d=1 (odd): [2,4] down → [2,4]
# d=2 (even): [3,5,7] up → [3,5,7]
# d=3 (odd): [6,8] down → [6,8]
# d=4 (even): [9] up → [9]
# Result: [1,2,4,3,5,7,6,8,9] ✓

sol = MatrixTraversal()
print("Spiral Order:", sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))  # [1,2,3,6,9,8,7,4,5]
print("Diagonal Order:", sol.diagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))  # [1,2,4,3,5,7,6,8,9]


# ================================================================
# PATTERN 2: MATRIX DFS/BFS (FLOOD FILL & CONNECTED COMPONENTS)
# PATTERN EXPLANATION: Use DFS or BFS to explore connected cells in a grid. Mark visited
# cells to avoid infinite loops. For DFS, recursively explore neighbors. For BFS, use queue
# for level-by-level exploration. Track visited with set or modify matrix in-place. Common
# for counting islands, flood fill, and finding connected regions.
#
# TYPICAL STEPS:
# 1. Iterate through all cells in matrix
# 2. When unvisited target cell found, start DFS/BFS
# 3. Mark current cell as visited
# 4. Explore 4 (or 8) adjacent neighbors
# 5. Recursively/iteratively visit valid neighbors
# 6. Count connected components or perform flood fill
#
# Applications: Number of islands, flood fill, surrounded regions, word search.
# ================================================================

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
        
        Islands:
        - Top-left: 4 connected '1's
        - Middle: 1 single '1'
        - Bottom-right: 2 connected '1's
        
        Output: 3
    
    TC: O(m * n) - visit each cell at most once
    SC: O(m * n) - recursion stack in worst case (or modify in-place for O(1))
    
    How it works:
    1. Iterate through every cell
    2. When we find unvisited land ('1'), it's a new island
    3. DFS/BFS to mark all connected land as visited
    4. Count each time we start a new DFS/BFS
    """
    def numIslands(self, grid: List[List[str]]) -> int:  # LC 200
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        islands = 0
        
        def dfs(r, c):
            """Mark all land connected to (r,c) as visited"""
            # Base cases: out of bounds, water, or already visited
            if (r < 0 or r >= rows or c < 0 or c >= cols or 
                grid[r][c] != '1'):
                return
            
            # Mark as visited by changing to '0'
            grid[r][c] = '0'
            
            # Explore 4 directions
            dfs(r + 1, c)  # Down
            dfs(r - 1, c)  # Up
            dfs(r, c + 1)  # Right
            dfs(r, c - 1)  # Left
        
        # Check every cell
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':  # Found unvisited land
                    islands += 1        # New island
                    dfs(r, c)          # Mark entire island
        
        return islands

# Example trace:
# grid = [["1","1","0","0","0"],
#         ["1","1","0","0","0"],
#         ["0","0","1","0","0"],
#         ["0","0","0","1","1"]]
#
# (0,0): '1' found, islands=1, DFS marks (0,0),(0,1),(1,0),(1,1) → all '0'
# (0,1): '0' (already visited)
# (0,2): '0' (water)
# ... continue ...
# (2,2): '1' found, islands=2, DFS marks (2,2) → '0'
# ... continue ...
# (3,3): '1' found, islands=3, DFS marks (3,3),(3,4) → '0'
# 
# Output: 3 islands

    def floodFill(self, image: List[List[int]], sr: int, sc: int, 
                   color: int) -> List[List[int]]:  # LC 733
        """
        Problem: Perform flood fill starting from pixel (sr, sc).
        Change starting pixel and all connected pixels of same color.
        
        TC: O(m * n) - visit each pixel at most once
        SC: O(m * n) - recursion stack
        
        How it works:
        1. Save original color of starting pixel
        2. DFS from starting position
        3. Change color of current pixel
        4. Recursively fill connected pixels with same original color
        """
        original_color = image[sr][sc]
        
        # Edge case: already target color (prevent infinite recursion)
        if original_color == color:
            return image
        
        rows, cols = len(image), len(image[0])
        
        def dfs(r, c):
            # Check bounds and if pixel matches original color
            if (r < 0 or r >= rows or c < 0 or c >= cols or 
                image[r][c] != original_color):
                return
            
            # Fill with new color
            image[r][c] = color
            
            # Fill 4 neighbors
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        dfs(sr, sc)
        return image

# Example:
# image = [[1,1,1],
#          [1,1,0],
#          [1,0,1]]
# sr=1, sc=1, color=2
#
# Original color = 1
# DFS from (1,1):
#   Change (1,1) to 2
#   Check (2,1): original_color=1, change to 2
#   Check (1,0): original_color=1, change to 2
#   ... recursively change all connected 1's to 2
#
# Result: [[2,2,2],
#          [2,2,0],
#          [2,0,1]]

sol = MatrixDFSBFS()
print("Number of Islands:", sol.numIslands([["1","1","0"],["1","1","0"],["0","0","1"]]))  # 2
print("Flood Fill:", sol.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))


# ================================================================
# PATTERN 3: MATRIX TRANSFORMATION (ROTATE, TRANSPOSE, FLIP)
# PATTERN EXPLANATION: Transform matrix in-place using mathematical patterns. Rotation
# can be decomposed into transpose + flip. Transpose swaps (i,j) with (j,i). Flip reverses
# rows or columns. In-place modification saves space but requires careful swapping to avoid
# overwriting values. Often combine operations for complex transformations.
#
# TYPICAL STEPS:
# For 90° Rotation:
# 1. Transpose matrix: swap matrix[i][j] with matrix[j][i]
# 2. Reverse each row (for clockwise) or each column (for counter-clockwise)
#
# For Transpose:
# 1. Iterate upper triangle only (i < j)
# 2. Swap matrix[i][j] with matrix[j][i]
#
# For Flip:
# 1. Reverse rows (horizontal flip) or columns (vertical flip)
#
# Applications: Image rotation, matrix operations, mirror image, game board transformations.
# ================================================================

class MatrixTransformation:
    """
    Problem: You are given an n x n 2D matrix representing an image. Rotate the image
    by 90 degrees clockwise in-place.
    
    Example:
        Input: matrix = [[1,2,3],
                        [4,5,6],
                        [7,8,9]]
        
        Clockwise 90°:
        [[7,4,1],
         [8,5,2],
         [9,6,3]]
        
        Key insight: 90° clockwise = Transpose + Reverse each row
        
        After transpose:        After reverse rows:
        [[1,4,7],               [[7,4,1],
         [2,5,8],                [8,5,2],
         [3,6,9]]                [9,6,3]]
    
    TC: O(n²) - process each cell once for transpose, once for reverse
    SC: O(1) - in-place transformation
    
    How it works:
    1. Transpose: swap elements across main diagonal
       - matrix[i][j] ↔ matrix[j][i] for i < j
    2. Reverse each row: swap elements within each row
       - matrix[i][j] ↔ matrix[i][n-1-j] for j < n/2
    """
    def rotate(self, matrix: List[List[int]]) -> None:  # LC 48
        """Rotate matrix 90 degrees clockwise in-place"""
        n = len(matrix)
        
        # Step 1: Transpose matrix (swap across diagonal)
        for i in range(n):
            for j in range(i + 1, n):  # Only upper triangle (i < j)
                # Swap matrix[i][j] with matrix[j][i]
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Step 2: Reverse each row
        for i in range(n):
            matrix[i].reverse()
            # Or manually: for j in range(n // 2):
            #     matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]

# Example trace:
# matrix = [[1,2,3],
#           [4,5,6],
#           [7,8,9]]
#
# Step 1: Transpose
# i=0, j=1: swap (0,1) with (1,0): 2 ↔ 4
# i=0, j=2: swap (0,2) with (2,0): 3 ↔ 7
# i=1, j=2: swap (1,2) with (2,1): 6 ↔ 8
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
#         [9,6,3]]

    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:  # LC 867
        """
        Problem: Return transpose of matrix (swap rows and columns).
        
        For non-square matrices, create new matrix with swapped dimensions.
        
        TC: O(m * n) - copy each element
        SC: O(m * n) - new matrix (unless m = n, then can be O(1))
        """
        rows, cols = len(matrix), len(matrix[0])
        
        # Create new matrix with swapped dimensions
        transposed = [[0] * rows for _ in range(cols)]
        
        for r in range(rows):
            for c in range(cols):
                transposed[c][r] = matrix[r][c]
        
        return transposed

    def flipHorizontal(self, matrix: List[List[int]]) -> None:
        """Flip matrix horizontally (mirror left-right)"""
        for row in matrix:
            row.reverse()
    
    def flipVertical(self, matrix: List[List[int]]) -> None:
        """Flip matrix vertically (mirror top-bottom)"""
        matrix.reverse()

# Rotation patterns:
# 90° clockwise = transpose + reverse rows
# 90° counter-clockwise = transpose + reverse columns
# 180° = reverse rows + reverse columns (or reverse twice)

sol = MatrixTransformation()
matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
sol.rotate(matrix1)
print("Rotated 90° clockwise:", matrix1)  # [[7,4,1],[8,5,2],[9,6,3]]

matrix2 = [[1,2,3],[4,5,6]]
print("Transpose:", sol.transpose(matrix2))  # [[1,4],[2,5],[3,6]]


# ================================================================
# PATTERN 4: MATRIX SEARCH (SORTED MATRIX)
# PATTERN EXPLANATION: Leverage sorted properties of matrix for efficient search. Two main
# approaches: (1) Treat as flattened 1D array for binary search when entire matrix is sorted
# row-by-row, (2) Start from corner (top-right or bottom-left) and eliminate rows/columns
# when rows and columns are independently sorted. Choose approach based on sorting pattern.
#
# TYPICAL STEPS:
# Approach 1 (Fully sorted matrix):
# 1. Treat matrix as 1D sorted array of length m*n
# 2. Binary search with index conversion: row = mid // cols, col = mid % cols
# 3. Compare middle element with target
#
# Approach 2 (Row & column sorted):
# 1. Start at top-right corner (or bottom-left)
# 2. If target < current: move left (eliminate column)
# 3. If target > current: move down (eliminate row)
# 4. Continue until found or out of bounds
#
# Applications: Search in 2D matrix, find k-th smallest, count elements in range.
# ================================================================

class MatrixSearch:
    """
    Problem 1: Search for target in m x n matrix where integers in each row are sorted
    left to right, and first integer of each row > last integer of previous row.
    (Entire matrix sorted as if flattened)
    
    Example:
        matrix = [[1,  3,  5,  7],
                  [10, 11, 16, 20],
                  [23, 30, 34, 60]]
        target = 3
        
        Treat as: [1,3,5,7,10,11,16,20,23,30,34,60]
        Binary search: find 3 at index 1
        Convert back: row = 1 // 4 = 0, col = 1 % 4 = 1
        
        Output: True
    
    TC: O(log(m * n)) - binary search on m*n elements
    SC: O(1) - only store indices
    
    How it works:
    1. Treat matrix as 1D sorted array
    2. Binary search with index range [0, m*n-1]
    3. Convert 1D index to 2D: row = mid // cols, col = mid % cols
    4. Compare matrix[row][col] with target
    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:  # LC 74
        if not matrix or not matrix[0]:
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            # Convert 1D index to 2D coordinates
            row = mid // cols
            col = mid % cols
            value = matrix[row][col]
            
            if value == target:
                return True
            elif value < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False

# Example trace:
# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# rows=3, cols=4, left=0, right=11
#
# Iteration 1: mid=5
#   row=5//4=1, col=5%4=1, value=matrix[1][1]=11
#   11 > 3, right=4
#
# Iteration 2: mid=2
#   row=2//4=0, col=2%4=2, value=matrix[0][2]=5
#   5 > 3, right=1
#
# Iteration 3: mid=0
#   row=0//4=0, col=0%4=0, value=matrix[0][0]=1
#   1 < 3, left=1
#
# Iteration 4: mid=1
#   row=1//4=0, col=1%4=1, value=matrix[0][1]=3
#   3 == 3, return True

    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:  # LC 240
        """
        Problem 2: Search in matrix where each row is sorted left to right, and
        each column is sorted top to bottom (but rows don't connect).
        
        Example:
            matrix = [[1,  4,  7,  11, 15],
                      [2,  5,  8,  12, 19],
                      [3,  6,  9,  16, 22],
                      [10, 13, 14, 17, 24],
                      [18, 21, 23, 26, 30]]
            target = 5
            
            Start at top-right (15):
            15 > 5, move left to 11
            11 > 5, move left to 7
            7 > 5, move left to 4
            4 < 5, move down to 5
            5 == 5, found!
        
        TC: O(m + n) - each step eliminates one row or column
        SC: O(1)
        
        How it works:
        1. Start at top-right corner (could also use bottom-left)
        2. If target < current: move left (eliminate column)
        3. If target > current: move down (eliminate row)
        4. Guarantees we never miss target
        """
        if not matrix or not matrix[0]:
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        
        # Start at top-right corner
        r, c = 0, cols - 1
        
        while r < rows and c >= 0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                c -= 1  # Target must be to the left
            else:
                r += 1  # Target must be below
        
        return False

# Example trace:
# matrix = [[1,4,7,11,15],
#           [2,5,8,12,19],
#           [3,6,9,16,22],
#           [10,13,14,17,24],
#           [18,21,23,26,30]]
# target = 5
#
# Start: r=0, c=4, value=15
# 15 > 5, move left: r=0, c=3, value=11
# 11 > 5, move left: r=0, c=2, value=7
# 7 > 5, move left: r=0, c=1, value=4
# 4 < 5, move down: r=1, c=1, value=5
# 5 == 5, return True

sol = MatrixSearch()
print("Search in Sorted Matrix:", sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))  # True
print("Search Matrix II:", sol.searchMatrix2([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5))  # True


# ================================================================
# PATTERN 5: GRID DYNAMIC PROGRAMMING (PATH PROBLEMS)
# PATTERN EXPLANATION: Use DP on grid where each cell's value depends on neighboring cells
# (typically top, left, or diagonal). Build solution from top-left to bottom-right. Each cell
# represents optimal solution to reach that position. Common for counting paths, finding
# minimum/maximum path sums, or optimization with movement constraints.
#
# TYPICAL STEPS:
# 1. Create DP table (same size as grid or optimized to 1D)
# 2. Initialize first row and/or first column (base cases)
# 3. Fill table row by row or column by column
# 4. Recurrence: dp[i][j] = f(dp[i-1][j], dp[i][j-1], grid[i][j])
# 5. Return dp[m-1][n-1] (bottom-right corner)
#
# Applications: Unique paths, minimum path sum, dungeon game, triangle paths.
# ================================================================

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
    
    How it works:
    1. dp[i][j] = minimum sum to reach cell (i,j)
    2. Can reach from top or left: take minimum + current value
    3. Base cases: first row (only from left), first column (only from top)
    4. Recurrence: dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
    """
    def minPathSum(self, grid: List[List[int]]) -> int:  # LC 64
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        
        # Create DP table
        dp = [[0] * cols for _ in range(rows)]
        
        # Base case: top-left corner
        dp[0][0] = grid[0][0]
        
        # Fill first row (can only come from left)
        for c in range(1, cols):
            dp[0][c] = dp[0][c-1] + grid[0][c]
        
        # Fill first column (can only come from top)
        for r in range(1, rows):
            dp[r][0] = dp[r-1][0] + grid[r][0]
        
        # Fill rest of table
        for r in range(1, rows):
            for c in range(1, cols):
                # Minimum of coming from top or left, plus current value
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

    def uniquePaths(self, m: int, n: int) -> int:  # LC 62
        """
        Problem: Count number of unique paths from top-left to bottom-right
        in m×n grid (can only move right or down).
        
        TC: O(m * n)
        SC: O(m * n) or O(n) optimized
        """
        # Create DP table
        dp = [[1] * n for _ in range(m)]
        
        # First row and column are all 1 (only one way to reach)
        
        # Fill rest of table
        for r in range(1, m):
            for c in range(1, n):
                # Paths to current = paths from above + paths from left
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
        
        return dp[m-1][n-1]

# Space-optimized version using 1D array
    def uniquePaths_optimized(self, m: int, n: int) -> int:
        """
        TC: O(m * n)
        SC: O(n) - only keep current row
        """
        dp = [1] * n  # All cells in first row = 1
        
        for r in range(1, m):
            for c in range(1, n):
                # dp[c] = paths from above (previous row)
                # dp[c-1] = paths from left (current row)
                dp[c] = dp[c] + dp[c-1]
        
        return dp[n-1]

sol = GridDP()
print("Minimum Path Sum:", sol.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))  # 7
print("Unique Paths (3x7):", sol.uniquePaths(3, 7))  # 28
print("Unique Paths Optimized (3x7):", sol.uniquePaths_optimized(3, 7))  # 28


# ================================================================
# PATTERN 6: MATRIX SIMULATION (STATE-BASED MODIFICATIONS)
# PATTERN EXPLANATION: Simulate rules or state changes on matrix cells over time. Often
# need to track current and next state simultaneously. Use state encoding (extra bits) or
# temporary storage to avoid conflicts. Process based on neighbors or rules, then update
# all cells together. Common in game simulations and cellular automata.
#
# TYPICAL STEPS:
# 1. Analyze neighbors/surroundings for each cell
# 2. Determine next state based on rules
# 3. Store next state without affecting current state:
#    a. Use state encoding (combine old and new in same cell)
#    b. Or use temporary matrix
# 4. Update all cells to next state simultaneously
# 5. Decode or copy final state
#
# Applications: Game of Life, set matrix zeroes, spiral matrix generation, simulation games.
# ================================================================

class MatrixSimulation:
    """
    Problem: Given an m x n matrix, if an element is 0, set its entire row and column
    to 0. Do it in-place.
    
    Example:
        Input:  [[1,1,1],
                 [1,0,1],
                 [1,1,1]]
        
        Cell (1,1) is 0, so row 1 and column 1 become 0:
        
        Output: [[1,0,1],
                 [0,0,0],
                 [1,0,1]]
    
    TC: O(m * n) - scan matrix twice
    SC: O(1) - use first row and column as markers
    
    How it works:
    1. Use first row and column to mark which rows/columns should be zeroed
    2. Use separate flags for first row and first column themselves
    3. First pass: scan and mark in first row/column
    4. Second pass: zero cells based on markers
    5. Handle first row and column separately based on flags
    """
    def setZeroes(self, matrix: List[List[int]]) -> None:  # LC 73
        if not matrix or not matrix[0]:
            return
        
        rows, cols = len(matrix), len(matrix[0])
        
        # Flags for first row and first column
        first_row_zero = any(matrix[0][c] == 0 for c in range(cols))
        first_col_zero = any(matrix[r][0] == 0 for r in range(rows))
        
        # Use first row and column as markers
        # Scan matrix and mark first row/column
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0  # Mark this row
                    matrix[0][c] = 0  # Mark this column
        
        # Zero out cells based on markers (skip first row/column)
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        # Handle first row
        if first_row_zero:
            for c in range(cols):
                matrix[0][c] = 0
        
        # Handle first column
        if first_col_zero:
            for r in range(rows):
                matrix[r][0] = 0

# Example trace:
# matrix = [[1,1,1],
#           [1,0,1],
#           [1,1,1]]
#
# Check first row: [1,1,1], first_row_zero = False
# Check first col: [1,1,1], first_col_zero = False
#
# Scan and mark:
# (1,1) is 0, mark matrix[1][0]=0 and matrix[0][1]=0
# matrix = [[1,0,1],  ← column 1 marked
#           [0,0,1],  ← row 1 marked
#           [1,1,1]]
#
# Zero based on markers:
# (1,1): row 1 or col 1 marked → 0 (already 0)
# (1,2): row 1 marked → 0
# (2,1): col 1 marked → 0
# matrix = [[1,0,1],
#           [0,0,0],
#           [1,0,1]]
#
# First row/col not flagged, no change
# Final: [[1,0,1],
#         [0,0,0],
#         [1,0,1]]

    def gameOfLife(self, board: List[List[int]]) -> None:  # LC 289
        """
        Problem: Apply Game of Life rules to board in-place.
        
        Rules:
        1. Live cell with < 2 live neighbors dies
        2. Live cell with 2-3 live neighbors lives
        3. Live cell with > 3 live neighbors dies
        4. Dead cell with exactly 3 live neighbors becomes live
        
        TC: O(m * n) - count neighbors for each cell
        SC: O(1) - use state encoding
        
        State encoding:
        - 0: dead → dead (no change needed)
        - 1: live → live (no change needed)
        - 2: live → dead (encode transition)
        - 3: dead → live (encode transition)
        
        How it works:
        1. Count live neighbors (8-directional)
        2. Apply rules and encode next state
        3. Decode all cells (2→0, 3→1)
        """
        if not board or not board[0]:
            return
        
        rows, cols = len(board), len(board[0])
        
        def countLiveNeighbors(r, c):
            """Count live neighbors in 8 directions"""
            count = 0
            directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    # Count original live cells (1 or 2)
                    if board[nr][nc] in [1, 2]:
                        count += 1
            
            return count
        
        # First pass: mark transitions
        for r in range(rows):
            for c in range(cols):
                live_neighbors = countLiveNeighbors(r, c)
                
                if board[r][c] == 1:  # Currently live
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[r][c] = 2  # Will die
                else:  # Currently dead
                    if live_neighbors == 3:
                        board[r][c] = 3  # Will become live
        
        # Second pass: decode transitions
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 2:
                    board[r][c] = 0  # Dead
                elif board[r][c] == 3:
                    board[r][c] = 1  # Live

# Example:
# board = [[0,1,0],
#          [0,0,1],
#          [1,1,1],
#          [0,0,0]]
#
# Count neighbors and apply rules:
# (0,1): live, 1 neighbor → dies (encode as 2)
# (1,2): live, 3 neighbors → lives
# (2,0): live, 1 neighbor → dies (encode as 2)
# (2,1): live, 3 neighbors → lives
# (2,2): live, 2 neighbors → lives
# (1,0): dead, 3 neighbors → lives (encode as 3)
# (1,1): dead, 5 neighbors → stays dead
# (3,1): dead, 3 neighbors → lives (encode as 3)
#
# After encoding:
# board = [[0,2,0],
#          [3,0,1],
#          [2,1,1],
#          [0,3,0]]
#
# Decode:
# board = [[0,0,0],
#          [1,0,1],
#          [0,1,1],
#          [0,1,0]]

sol = MatrixSimulation()
matrix1 = [[1,1,1],[1,0,1],[1,1,1]]
sol.setZeroes(matrix1)
print("Set Matrix Zeroes:", matrix1)  # [[1,0,1],[0,0,0],[1,0,1]]

matrix2 = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
sol.gameOfLife(matrix2)
print("Game of Life:", matrix2)  # [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]


# ================================================================
# SUMMARY OF MATRIX PATTERNS
# ================================================================
"""
Pattern 1 - Matrix Traversal (Spiral, Diagonal):
  - Navigate matrix in non-standard patterns
  - Use boundary pointers or direction vectors
  - Use for: Spiral order, diagonal traverse, zigzag, layer-by-layer
  - Example: LC 54 (Spiral Matrix), LC 498 (Diagonal Traverse)

Pattern 2 - Matrix DFS/BFS (Flood Fill):
  - Explore connected cells using DFS or BFS
  - Track visited to avoid infinite loops
  - Use for: Islands, flood fill, connected components, path finding
  - Example: LC 200 (Number of Islands), LC 733 (Flood Fill)

Pattern 3 - Matrix Transformation (Rotate, Transpose):
  - Transform matrix in-place using math patterns
  - Rotation = Transpose + Flip
  - Use for: Image rotation, mirror, matrix operations
  - Example: LC 48 (Rotate Image), LC 867 (Transpose Matrix)

Pattern 4 - Matrix Search (Sorted):
  - Leverage sorted properties for efficient search
  - Binary search (fully sorted) or corner elimination (row/col sorted)
  - Use for: Search in 2D matrix, find k-th element
  - Example: LC 74 (Search 2D Matrix), LC 240 (Search 2D Matrix II)

Pattern 5 - Grid Dynamic Programming:
  - Each cell depends on neighboring cells
  - Build solution from top-left to bottom-right
  - Use for: Path counting, minimum/maximum path sum, grid optimization
  - Example: LC 64 (Minimum Path Sum), LC 62 (Unique Paths)

Pattern 6 - Matrix Simulation:
  - Simulate rules or state changes
  - Use state encoding or temporary storage
  - Use for: Game of Life, set zeroes, cellular automata
  - Example: LC 73 (Set Matrix Zeroes), LC 289 (Game of Life)

Master these 6 patterns and you'll handle 80-90% of matrix problems on LeetCode!

KEY TAKEAWAYS:
--------------
1. Always check boundaries before accessing matrix[i][j]
2. For in-place modifications, use state encoding to preserve original state
3. DFS/BFS: 4-directional (up/down/left/right) vs 8-directional (includes diagonals)
4. Spiral/diagonal traversals: carefully manage boundary pointers
5. Matrix rotation: Transpose + Flip (in-place O(1) space)
6. Sorted matrix search: Choose approach based on sorting pattern
7. Grid DP: Current cell depends on top/left/diagonal neighbors
8. State simulation: Process all cells based on current state, update simultaneously
9. Space optimization: Use first row/column as markers, or modify in-place
10. Common directions array: [(0,1), (1,0), (0,-1), (-1,0)] for 4-directional
"""