# 1351. Count Negative Numbers in a Sorted Matrix

# Topics: Array, Binary Search, Matrix

# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

# Example 1:

# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.
# Example 2:

# Input: grid = [[3,2],[1,0]]
# Output: 0

# Follow up: Could you find an O(n + m) solution?

# How to Solve (Binary Search) -> O(m * log n)
    # For each row in the grid:
    #   - Use binary search to find the index of the first negative number
    #   - Since the row is sorted, all elements to the right of this index are also 
    #     negative
    #   - Subtract the index from the row length to get the number of negatives in that  #     row
    #   - Accumulate this count across all rows

    # Binary search is used to reduce time from linear to logarithmic per row

    # Time Complexity: O(m * log n)
    #   - Each row is searched with binary search → O(log n) per row, and there are m rows

    # Space Complexity: O(1)
    #   - Only a counter variable is used; no additional space grows with input size

from typing import List

class Solution: # O(m * log n)
    def countNegatives(self, grid: List[List[int]]) -> int:
        negatives = 0 # Count the total number of negatives
        for g in grid: # Loop through each inner list
            l, r = 0, len(g) - 1 # Set l and r pointers for binary search
            while l <= r: # Perform binary search
                mid = (l + r) // 2
                if g[mid] >= 0:
                    l = mid + 1
                else:
                    r = mid -1
            negatives += len(g) - l # After loop, l is the idx of the first negative num

        return negatives
    
# How to Solve in O(n + m)
    # Start from the top-right corner of the grid
    # Initialize a counter to keep track of the total number of negative numbers

    # While we are within the bounds of the matrix:
    #   - If the current value is negative:
    #       - All elements below it in the same column are 
    #         also negative (since the column is sorted top to #         bottom in a non decreasing order)
    #       - So, add (number of remaining rows) to the count
    #       - Then move one column to the left
    #   - If the current value is non-negative:
    #       - Move down to the next row (to find smaller 
    #         numbers)

    # This approach ensures we only traverse each row and 
    # column once

    # Time Complexity: O(n + m)
    #   - n = number of rows, m = number of columns
    #   - At most, we move n steps down and m steps left

    # Space Complexity: O(1)
    #   - Uses a constant number of variables regardless of input size


    def countNegatives2(self, grid: List[List[int]]) -> int: # O(n + m)
        rows = len(grid) # count the num of rows
        cols = len(grid[0]) # count the num of columns
        row = 0
        col = cols - 1
        count = 0

        while row < rows and col >= 0:
            if grid[row][col] < 0: # If the value is negative, all values below in this column are also negative b/c matrix is non decreasing column wise
                count += rows - row 
                col -= 1  # Move left
            else:
                row += 1  # Move down if value is non-negative

        return count



sol = Solution()
print(sol.countNegatives2([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
print(sol.countNegatives([[3,2],[1,0]]))
