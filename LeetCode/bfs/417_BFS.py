# 417. Pacific Atlantic Water Flow

# Topics: Array, DFS, BFS, Matrix

# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

# The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

# Ex. 1
# Input: heights = [     Pacific
#                    [1, 2, 2, 3, 5],
#                    [3, 2, 3, 4, 4],
#            Pacific [2, 4, 5, 3, 1], Atlantic
#                    [6, 7, 1, 4, 5],
#                    [5, 1, 1, 2, 4]
# ]                      Atlantic

# Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
# Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
# [0,4]: [0,4] -> Pacific Ocean 
#        [0,4] -> Atlantic Ocean
# [1,3]: [1,3] -> [0,3] -> Pacific Ocean 
#        [1,3] -> [1,4] -> Atlantic Ocean
# [1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
#        [1,4] -> Atlantic Ocean
# [2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
#        [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
# [3,0]: [3,0] -> Pacific Ocean 
#        [3,0] -> [4,0] -> Atlantic Ocean
# [3,1]: [3,1] -> [3,0] -> Pacific Ocean 
#        [3,1] -> [4,1] -> Atlantic Ocean
# [4,0]: [4,0] -> Pacific Ocean 
#        [4,0] -> Atlantic Ocean
# Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.

# Example 2:

# Input: heights = [[1]]
# Output: [[0,0]]
# Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.

# How to Solve: (Brute Force)
    # - Use BFS from each cell to explore all valid downhill paths
    # - Use a visited set to avoid revisiting cells during BFS
    # - Stop early if both oceans are reached during traversal
    # - Use directions array to move in 4 cardinal directions if next cell is valid

# Time complexity: O(m * n)^2
# - We perform a BFS from each cell: O(m * n) cells total
# - Each BFS can visit up to O(m * n) cells in the worst case
# - So the total time complexity is O((m * n)^2), which may TLE on large grids

# Space complexity: O(m * n)
# - At any given time, the BFS queue and visited set can hold up to O(m * n) entries
# - The final result list can also store up to O(m * n) entries in the worst case


from typing import List
from collections import deque

class Solution: # Brute Force
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]: # Edge case -> empty input
            return []

        rows, cols = len(heights), len(heights[0]) # Get dimensions of the grid
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)] # Directions for BFS
        result = []

        def bfs(r, c): # BFS helper fn to check if water can flow to both oceans
            queue = deque([(r, c)])
            visited = set() # Track visited set so we don't keep adding previously
            visited.add((r, c)) # visited squares & get stuck in infinite loop

            pacific = False # Flags to track whether we reached each ocean
            atlantic = False

            while queue:
                row, col = queue.popleft()

                # Check if we've reached Pacific or Atlantic
                if row == 0 or col == 0:
                    pacific = True
                if row == rows - 1 or col == cols - 1:
                    atlantic = True

                if pacific and atlantic: # If we reached both oceans, stop BFS early
                    return True

                for dr, dc in directions: # Explore all four directions if:
                    new_r, new_c = row + dr, col + dc
                    if (
                        0 <= new_r < rows and # row is in bounds
                        0 <= new_c < cols and # col is in bounds
                        (new_r, new_c) not in visited and # square not visited
                        heights[new_r][new_c] <= heights[row][col] # height of neighbor <
                    ):
                        visited.add((new_r, new_c)) # continue & update search
                        queue.append((new_r, new_c))

            return False # return false if we finish BFS and don't reach both oceans

        # Try from every cell
        for r in range(rows):
            for c in range(cols):
                if bfs(r, c): # If result is True (touched both oceans)
                    result.append([r, c]) # append square to result

        return result
    
    # =============================
    # 📌 HIGH-LEVEL STRATEGY
    # =============================

    # The brute-force approach would simulate water flow from every cell to both oceans, which is too slow (O((m * n)^2)). Instead, we reverse the problem:
    # ✅ Instead of checking if water from each cell can reach the oceans, we check which cells the oceans can reach by flowing "uphill".
    # ✅ Start BFS from all cells adjacent to the Pacific Ocean (top row and left column) and mark all cells reachable from there using BFS/DFS where we only move to neighbors of greater or equal height.
    # ✅ Do the same BFS from all Atlantic-border cells (bottom row and right column).
    # ✅ The final answer is the intersection of the two reachable cell sets —
    # the cells that can reach both oceans via reverse flow.

    # =============================
    # ⏱️ TIME COMPLEXITY
    # =============================

    # Let m = number of rows, n = number of columns.

    # Each BFS traversal visits at most m * n cells.
    # Even though we start BFS from all the edges, we only visit each cell once per ocean (think we have one visited set per ocean vs one for every cell in brute force)
    # The total time complexity is: => O(m * n) + O(m * n) = O(m * n)

    # This is much faster than simulating flow from every cell individually.

    # =============================
    # 📦 SPACE COMPLEXITY
    # =============================

    # We use:
    # - Two visited sets: O(m * n) total
    # - Two BFS queues, each can hold up to O(m * n) cells in worst case

    # Therefore, total space complexity is:
    #   => O(m * n)

    # This includes space for the result list, visited sets, and queues.


    def pacificAtlantic2(self, heights: List[List[int]]) -> List[List[int]]: # Optimal
        # Edge case: empty grid
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0]) # Get dimensions of the grid

        # Queues for BFS starting points (cells touching each ocean)
        pacific_queue = deque()
        atlantic_queue = deque()

        # Add all cells in the first and last columns
        for r in range(rows):
            pacific_queue.append((r, 0))          # Left column (Pacific)
            atlantic_queue.append((r, cols - 1))  # Right column (Atlantic)

        # Add all cells in the first and last rows
        for c in range(cols):
            pacific_queue.append((0, c))          # Top row (Pacific)
            atlantic_queue.append((rows - 1, c))  # Bottom row (Atlantic)

        # BFS function to find all cells reachable from a given ocean
        def bfs(queue):
            visited = set()
            directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]  # up, down, right, left

            while queue:
                r, c = queue.popleft() # get current row and col
                visited.add((r, c))

                for dr, dc in directions: # For each direction
                    nr, nc = r + dr, c + dc # get neighbor row and col 

                    if (
                        0 <= nr < rows and # check neighbor row in rounds
                        0 <= nc < cols and # check neighbor col in rounds
                        (nr, nc) not in visited and # check square not visited
                        heights[nr][nc] >= heights[r][c] # check where water could have come from (reverse logic)
                    ):
                        queue.append((nr, nc)) # Add next square to be explored

            return visited # returns cells from which water can flow to each ocean

        # Run BFS from Pacific and Atlantic starting points
        pacific_reachable = bfs(pacific_queue) # returns visited set from pacific edges
        atlantic_reachable = bfs(atlantic_queue) # returns visited set from atl edges

        # Final result: cells reachable from both oceans
        result = []

        # Loop through all cells and check if they are able to reach both oceans
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific_reachable and (r, c) in atlantic_reachable:
                    result.append([r, c])

        return result


sol = Solution()
print(sol.pacificAtlantic2([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))