# 766. Toeplitz Matrix

# Topics: Array, Matrix

# Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

# Example 1:
# Input: matrix = [[1,2,3,4],
#                  [5,1,2,3],
#                  [9,5,1,2]]

# Output: true
# Explanation:
# In the above grid, the diagonals are:
# "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
# In each diagonal all elements are the same, so the answer is True.

# Example 2:
# Input: matrix = [[1,2],
#                  [2,2]]
# Output: false
# Explanation:
# The diagonal "[1, 2]" has different elements.

# How to Solve (High Level):
    # Iterate through the matrix starting from the second row and second column
    # For each element, compare it with its top-left diagonal neighbor
    # If any element does not match its top-left neighbor, return False
    # If all such comparisons pass, return True

    # Time Complexity: O(m * n), where m is the number of rows and n is the number of columns
    # Space Complexity: O(1), since no additional data structures are used

from typing import List

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(1, len(matrix)): # Start on list 1 (zero indexed)
            for j in range(1, len(matrix[0])): # Start on second ele
                if matrix[i][j] == matrix[i-1][j-1]: # Compare to top left neighbor
                    continue
                else:
                    return False # Return false if we find two values !=
        return True # Return true if all ele's compared are ==

sol = Solution()
print(sol.isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))
print(sol.isToeplitzMatrix([[1,2],[2,2]]))
