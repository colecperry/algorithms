# 48. Rotate Image

# Topics: Array, Math, Matrix

# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

# Ex. 1

# Matrix:
# [               [
#   [1, 2, 3],      [7, 4, 1],
#   [4, 5, 6],   -> [8, 5, 2],
#   [7, 8, 9],      [9, 6, 3],
# ]                ]

from typing import List

class Solution:
    """
    TC: O(n²) — typically we say this is O(n^2) where n is the dimension (rows or columns/side length), if we have n rows and n columns, total operations = n * n. BUT we only touch each element a constant number of times.
    SC: swap in-place, just a few temp variables for swapping.
    """
    def rotate(self, matrix: List[List[int]]) -> None: # Simpler
        rows, cols = len(matrix), len(matrix[0])

        # Transpose matrix: row[i] becomes col[i] -> [i][j] -> [j][i]
        for i in range(rows):
            for j in range(i + 1, cols):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for i in range(rows):
            matrix[i].reverse()

# Why i+1? If you swap entire matrix, each pair gets swapped twice (undoing itself). Starting j at i+1 ensures each pair only swapped once
#
# [1, 2, 3]     Upper triangle = 2, 3, 6
# [4, 5, 6]  →  Swap with their mirrors below diagonal
# [7, 8, 9]
#
# i=0, j=1: Swap (0,1)=2 ↔ (1,0)=4
# i=0, j=2: Swap (0,2)=3 ↔ (2,0)=7
# i=1, j=2: Swap (1,2)=6 ↔ (2,1)=8
# Diagonal (1,5,9) unchanged
#
# Result:
# [1, 4, 7]
# [2, 5, 8]
# [3, 6, 9]

sol = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
sol.rotate(matrix)
print(matrix)


