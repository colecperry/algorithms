# 240. Search a 2D Matrix II

# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.

# Example 1:
# Input: matrix = [[1,  4,  7,  11, 15],
#                  [2,  5,  8,  12, 19],
#                  [3,  6,  9,  16, 22],
#                  [10, 13, 14, 17, 24]]
#                  [18, 21, 23, 26, 30]]

# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
# Output: true

# Example 2:
# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
# Output: false

# Key Insights:

# MATRIX PROPERTIES:
# - Rows sorted left to right, columns sorted top to bottom
# - NOT flattened sorted (can't treat as 1D like LC 74)

# KEY INSIGHT - START FROM TOP-RIGHT CORNER:
# - From matrix[0][col-1]: left = smaller, down = larger
# - This gives decisive elimination power each step

# ELIMINATION LOGIC:
# - If current > target: move left (eliminate entire right column)
# - If current < target: move down (eliminate entire top row)
# - Never need to backtrack or check both directions

# WHY OTHER CORNERS DON'T WORK:
# - Top-left/Bottom-right: both directions could contain target
# - Bottom-left also works: up = smaller, right = larger

# STAIRCASE PATTERN:
# - Move in L-shaped path, eliminating rows/columns
# - At most visit m (num of rows) + n (num of cols) elements total

# Time Complexity: O(m + n) - visit at most one element per row/column
# Space Complexity: O(1) - only using two pointer variables

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = 0, len(matrix[0]) - 1 # start at the top right
    
        while row < len(matrix) and col >= 0: # Row OOB below and Col OOB left
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1  # Move left
            else:
                row += 1  # Move down
        return False
    
sol = Solution()
print(sol.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5)) # True
print(sol.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20)) # False
print(sol.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 10)) # True



