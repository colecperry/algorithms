# 1162. As Far from Land as Possible

# Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1.

# The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

# Example 1:
# Input: grid = [
# [1,0,1],
# [0,0,0],
# [1,0,1]]
# Output: 2
# Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.

# Example 2:
# Input: grid = [
# [1,0,0],
# [0,0,0],
# [0,0,0]]
# Output: 4
# Explanation: The cell (2, 2) is as far as possible from all the land with distance 4.

# NOTE
# Why start from land, not water?
#   - From each water cell: W separate BFS traversals → O(n⁴)
#   - From all land at once: 1 BFS traversal → O(n²)

from typing import List
from collections import deque

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        """
        TC: O(m*n)
        - O(m*n) to loop through every cell and initialize queue
        - O(m*n) to process every cell in queue, O(1) to check 4 directions
        
        SC: O(m*n)
        - Queue: O(m*n) worst case (all land or all water at one level)
        - Visited set: O(m*n) to track every cell
        """
        if not grid or not grid[0]:
            return -1

        rows, cols = len(grid), len(grid[0])
        queue = deque([]) 
        visited = set([])
        max_distance = 0

        for r in range(rows): # Initialize BFS queue with all land cells
            for c in range(cols):
                if grid[r][c] == 1:
                    queue.append((r, c))
                    visited.add((r, c))
                
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            level = len(queue) # Process the whole level 
            found_water = False # See if we can find water 

            for _ in range(level): # Each cell in this level...
                row, col = queue.popleft()

                for dr, dc in directions: # ...checks 4 neighbors for water
                    new_row, new_col = row + dr, col + dc

                    if (0 <= new_row < rows and  # Row not OOB
                        0 <= new_col < cols and  # Col not OOB
                        (new_row, new_col) not in visited): # Not visited

                        visited.add((new_row, new_col)) # Mark new cell visited
                        queue.append((new_row, new_col)) # & add it to the queue to explore

                        if grid[new_row][new_col] == 0: # Check each time if
                            found_water = True          # we can find water

            if found_water == True: # If we find water during level processing
                max_distance += 1 # Update max distance
        
        if max_distance == 0: # If we never found land
            return -1
        else:
            return max_distance
    

sol = Solution()
print(sol.maxDistance([[1,0,1],[0,0,0],[1,0,1]])) # 2
print(sol.maxDistance([[1,0,0],[0,0,0],[0,0,0]])) # 4