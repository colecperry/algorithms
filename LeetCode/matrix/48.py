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


import copy
from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        
        # transpose matrix
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # reverse rows
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]


sol = Solution()
print(sol.rotate([[1,2,3],[4,5,6],[7,8,9]]))


