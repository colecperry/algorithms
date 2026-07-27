# 304. Range Sum Query 2D - Immutable

# Given a 2D matrix matrix, handle multiple queries of the following type:

# Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

# Implement the NumMatrix class:
    # - NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
    # - int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

# You must design an algorithm where sumRegion works on O(1) time complexity.

# Example:
#         matrix = [[3,0,1,4,2],
#                   [5,6,3,2,1],
#                   [1,2,0,1,5],
#                   [4,1,0,1,7],
#                   [1,0,3,0,5]]

# Input
# ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
# [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]

# Output
# [null, 8, 11, 12]

# Explanation
# NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
# numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
# numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
# numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)

# Brute Force: loop from row to row, col to col, add up the sum O(n^2)

from typing import List

class Solution:
    """
    """
    def __init__(self, matrix: List[List[int]]):  # LC 304 - Range Sum Query 2D Immutable
        rows, cols = len(matrix), len(matrix[0])
        # each value in the prefix sum matrix is the sum of the rectangle from the top left corner to (r,c)
        self.prefix = [[0] * (cols + 1) for _ in range(rows + 1)] # 1 row and col extra for prefix sum

        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                self.prefix[r][c] = ( # prefix sum up to this point equals
                    matrix[r-1][c-1] # this cells value
                    + self.prefix[r-1][c] # + everything above
                    + self.prefix[r][c-1] # + everything to the left
                    - self.prefix[r-1][c-1] # - corner (counted twice above)
                )

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int: # now calculate a submatrix sum from (r1, c1) to (r2, c2)
        """
        TC: O(1) per query (O(m*n) build in __init__)
        SC: O(1)
        """
        return (
            self.prefix[r2+1][c2+1]   # A: big rectangle from origin down to the region's bottom-right
            - self.prefix[r1][c2+1]   # B: subtract the strip ABOVE the region
            - self.prefix[r2+1][c1]   # C: subtract the strip LEFT of the region
            + self.prefix[r1][c1]     # D: add back the top-left corner (removed twice)
        )
    
    #         matrix = [[3,0,1,4,2],
    #                   [5,6,3,2,1],
    #                   [1,2,0,1,5],
    #                   [4,1,0,1,7],
    #                   [1,0,3,0,5]]

    # Trace: matrix = [[1,2],[3,4]]
    # prefix = [[0, 0, 0],
    #           [0, 1, 3],
    #           [0, 4, 10]]
    #
    # sumRegion(0,0,1,1): prefix[2][2] - prefix[0][2] - prefix[2][0] + prefix[0][0]
    #                   = 10 - 0 - 0 + 0 = 10  (1+2+3+4) ✓
    # sumRegion(0,1,1,1): prefix[2][2] - prefix[0][2] - prefix[2][1] + prefix[0][1]
    #                   = 10 - 0 - 4 + 0 = 6   (2+4) ✓

nm = Solution([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]])
print(nm.sumRegion(2, 1, 4, 3))  # 8
print(nm.sumRegion(1, 1, 2, 2))  # 11