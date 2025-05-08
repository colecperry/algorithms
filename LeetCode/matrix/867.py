# 867. Transpose Matrix

# Topics: Array, Matrix, Simulation

# Given a 2D integer array matrix, return the transpose of matrix.

# The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices. 

# Example 1:
# Input: matrix = [[1,2,3],
#                  [4,5,6],
#                  [7,8,9]]
# Output: [[1,4,7],
#          [2,5,8],
#          [3,6,9]]

# Example 2:
# Input: matrix = [[1,2,3],
#                  [4,5,6]]
# Output: [[1,4],
#          [2,5],
#          [3,6]]

# How to Solve:
    # Initialize a result matrix with dimensions n x m (transpose of original m x n matrix)
    # Loop through each element in the original matrix
    # For each element at (i, j), place it in position (j, i) in the result matrix
    # Return the transposed result matrix

# Time Complexity: O(m * n) — each element is visited once
# Space Complexity: O(m * n) — a new matrix of the same total size is created

from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # Step 1: Initialize a new matrix of size n x m (columns become rows)
        # The original matrix is m x n → result should be n x m
        result = [[0] * len(matrix) for _ in range(len(matrix[0]))]

        # Step 2: Loop through each cell in the original matrix
        for i in range(len(matrix)): # m rows
            for j in range(len(matrix[0])): # n columns
                result[j][i] = matrix[i][j] # flip row and col
        
        return result
    
sol = Solution()
print(sol.transpose([[1,2,3],
                     [4,5,6],
                     [7,8,9]]))

print(sol.transpose([[1,2,3],
                     [4,5,6]]))