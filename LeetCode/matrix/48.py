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
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        
        # transpose matrix
        for i in range(n):
            for j in range(i + 1, n): # start at i + 1 so we don't swap twice
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # reverse rows
        for i in range(n):
            for j in range(n // 2): # only need to go halfway to reverse a row
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]

    def rotate(self, matrix: List[List[int]]) -> None: # Simpler
        rows, cols = len(matrix), len(matrix[0])

        # Step 1: Transpose matrix: [i][j] -> [j][i]
        for i in range(rows):
            for j in range(i + 1, cols):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for i in range(rows):
            matrix[i].reverse()


sol = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
sol.rotate()
print(matrix)


