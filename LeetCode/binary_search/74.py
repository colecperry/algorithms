# 74. Search a 2D Matrix

# Topics: Array, Binary Search, Matrix

# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

# Ex. 1

# Matrix:
# [
#   [ 1,  3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 60]
# ]

# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

# Ex. 2

# Matrix:
# [
#   [ 1,  3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 60]
# ]

# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false

# How To Solve:
    # Treat the 2D matrix as a sorted 1D array to apply binary search
    # Set initial search boundaries as the start and end of the flattened array

    # While the search range is valid:
    #   - Calculate the middle index of the current range
    #   - Convert the 1D middle index into its corresponding 2D (row, column) position
    #   - Access the matrix value at that position
    #   - If the value matches the target, return True
    #   - If the value is less than the target, move the left boundary up
    #   - If the value is greater than the target, move the right boundary down

    # If the loop ends without finding the target, return False

    # Time Complexity: O(log(m * n))
    #   - The matrix has m * n elements, and binary search reduces the search space in   #     half each step
    # Space Complexity: O(1)
    #   - No additional space is used beyond a few pointers/variables


from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Get the number of rows and columns
        rows = len(matrix)
        cols = len(matrix[0])

        # Set initial binary search bounds for a "flattened" 2D matrix
        left = 0
        right = rows * cols - 1

        # Perform binary search
        while left <= right:
            mid = (left + right) // 2

            # Map the 1D mid index to 2D row and column
            row = mid // cols # Get the row of the middle index
            col = mid % cols # Get the column of the middle index
            value = matrix[row][col] # Get the val

            # Compare current value with the target
            if value == target:
                return True
            elif value < target:
                left = mid + 1
            else:
                right = mid - 1

        # Target not found
        return False
    
sol = Solution()
print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))