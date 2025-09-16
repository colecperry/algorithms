# 994. Rotting Oranges

# Topics: Array, BFS, Matrix

# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

# Example 1
#
#         Minute 0         Minute 1         Minute 2         Minute 3           Minute 4
#        [[2, 1, 1],      [[2, 2, 1],      [[2, 2, 2],      [[2, 2, 2],        [[2, 2, 2],
#         [1, 1, 0],       [2, 1, 0],       [2, 2, 0],       [2, 2, 0],         [2, 2, 0]
#         [1, 0, 1]]       [1, 0, 1]]       [1, 0, 1]]       [2, 0, 1]]         [2, 0, 2]]
#
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4

# Example 2:
# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

# Example 3:
# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        
        # Add all initially rotten oranges to queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
        
        max_time = 0   # Track max time elapsed to spread rot to max area
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Matrix BFS goes 4 directions
        
        # BFS to spread rot
        while queue:
            row, col, time = queue.popleft()
            max_time = max(max_time, time)
            
            for dr, dc in directions:
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

sol = Solution()
print(sol.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])) # 4
print(sol.orangesRotting([[2,1,1],[0,1,1],[1,0,1]])) # -1
print(sol.orangesRotting([[0,2]])) # 0
