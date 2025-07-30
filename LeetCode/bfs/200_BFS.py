# 200. Number of Islands 

# Topics: Array, Depth-First Search, Breadth-First Search, Union Find, Matrix

# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

# Example 2:
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

# -----------------------
# 💡 How to Solve:
# -----------------------

# Use Breadth-First Search (BFS) to count the number of islands in the 2D grid
# An island is defined as a group of horizontally or vertically connected '1's

# 1. Initialize a counter to track the number of islands
# 2. Use a set to keep track of visited cells to avoid processing the same land multiple times
# 3. Iterative over each cell in the grid:
#     - If it's a '1' (land) and not visited:
#         - Start BFS from that cell to mark all connected land as visited
#         - After BFS finishes, increment the island count by 1
# 4. In BFS:
#     - Use a queue to explore all connected '1's in up/down/left/right directions
#     - Skip any cell that's out of bounds, already visited, or water ('0')

# -----------------------
# ⏱️ Time Complexity:
# -----------------------

# O(n * m)
# - Each cell is visited once at most, and each neighbor is processed in constant time

# -----------------------
# 📦 Space Complexity:
# -----------------------

# O(n * m)
# - The visited set may store every cell in the grid in the worst case (all land)
# - The queue can also hold up to O(n * m) elements during BFS

from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: # edge case -> empty grid
            return 0

        num_rows, num_cols = len(grid), len(grid[0]) # track num of rows and cols for OOB checks
        visited = set() # track visited elements so we don't revisit eles -> infinite loop caused by continuing to explore elements we have already explored and adding their neighbors over and over
        island_count = 0 # output

        def bfs(start_row, start_col): # Nested fn keeps exploring neighbors until island disconnects
            queue = deque([(start_row, start_col)]) # append the first ele (tuple of rows and cols)
            visited.add((start_row, start_col)) # add curr ele to visited set (tuple of rows and cols)

            directions = [(-1, 0), (1, 0), (0, 1), (0, -1)] # up, down, left, right (tuples of rows and cols)

            while queue:
                current_row, current_col = queue.popleft() # pop the ele & get it's row and col

                for d_row, d_col in directions: # iterate through each direction (adj neighbors)
                    neighbor_row = current_row + d_row # update row to neighbor's row
                    neighbor_col = current_col + d_col # update col to neighbor's col

                    if (
                        0 <= neighbor_row < num_rows and # if row in bounds
                        0 <= neighbor_col < num_cols and # if col in bounds
                        grid[neighbor_row][neighbor_col] == '1' and # if we find a 1 (island continues) 
                        (neighbor_row, neighbor_col) not in visited # and it's not already visited
                    ):
                        queue.append((neighbor_row, neighbor_col)) # append neighbor to the queue to keep exploring adj neighbors
                        visited.add((neighbor_row, neighbor_col)) # add the node to visited

        for row in range(num_rows): # iterate through each ele in the matrix ([row][col])
            for col in range(num_cols):
                if grid[row][col] == '1' and (row, col) not in visited: # if we find a connected component and it hasn't been visited already
                    bfs(row, col) # explore it's neighbors
                    island_count += 1

        return island_count
    
sol = Solution()
print(sol.numIslands([
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
])) # 1

print(sol.numIslands(
    [["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
])) # 3