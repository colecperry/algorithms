# 64. Minimum Path Sum

# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

# Example 1:

# Input: 
# grid = [
    # [1,3,1],
    # [1,5,1],
    # [4,2,1]]

# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

# Example 2:
# Input: grid = 
    # [[1,2,3],
    # [4,5,6]]
# Output: 12

from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid) # "m" rows
        n = len(grid[0]) # "n" cols
        dp = [[0] * n for _ in range(m)] # Create dp matrix
        dp[0][0] = grid[0][0] # Min path sum

        for i in range(1, m): # base case col 1 -> iterate through rows and col stays 0
            dp[i][0] = dp[i-1][0] + grid[i][0] # min path sum = prev row sum + curr sum
        
        for i in range(1, n): # base case row 1 -> iterate through cols and row stays 0
            dp[0][i] = dp[0][i-1] + grid[0][i] # min path sum = prev col sum + curr sum
        
        for i in range(1, m):
            for j in range(1, n): # min path sum = min of top, left + curr
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j] 
        
        return dp[m-1][n-1]

sol = Solution()
print(sol.minPathSum([[1,3,1],[1,5,1],[4,2,1]])) # 7
print(sol.minPathSum([[1,2,3],[4,5,6]])) # 12