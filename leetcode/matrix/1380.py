# 1380. Lucky Numbers in a Matrix

# Topics: Array, Matrix

# Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

# A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.


# Example 1:
# Input: matrix = [[3,  7,  8],
#                  [9,  11, 13],
#                  [15, 16, 17]]
# Output: [15]
# Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.

# Example 2:
# Input: matrix =  [[1,  10, 4,  2],
#                   [9,  3,  8,  7],
#                   [15, 16, 17, 12]]
# Output: [12]
# Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.

# Example 3:
# Input: matrix = [[7,8],
#                  [1,2]]
# Output: [7]
# Explanation: 7 is the only lucky number since it is the minimum in its row and the maximum in its column.

# How to Solve
    # 1. Loop through each row of the matrix
    # 2. For each row, find the minimum value and its column index
    # 3. Check if this value is the maximum in its column with another loop using 
    #    that minimum column index we found
    #    - If yes, it's a lucky number (min in row and max in column)
    # 4. Return the lucky number if found (as a list), else return empty list

    # Time Complexity:
    # - Finding min in each row: O(n) per row → O(m * n)
    # - Finding max in the corresponding column: O(m) per row → O(m * m)
    # - Total Time = O(m * n + m²)

    # Space Complexity:
    # - Uses constant extra space → O(1)

from typing import List

class Solution:
    class Solution:
        def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
            result = []  # collect all lucky numbers
            for i in range(len(matrix)):  # loop over the rows
                min_row_el = float('inf')
                min_col_index = -1
                for j in range(len(matrix[i])):  # find min element and its column index
                    if matrix[i][j] < min_row_el:
                        min_row_el = matrix[i][j]
                        min_col_index = j
                max_col_el = float('-inf')
                for k in range(len(matrix)):  # find max in that column
                    max_col_el = max(matrix[k][min_col_index], max_col_el)
                if max_col_el == min_row_el:
                    result.append(min_row_el)  # collect it instead of returning immediately
            return result  # return all lucky numbers


sol = Solution()
print(sol.luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]))
print(sol.luckyNumbers([[1,10,4,2],[9,3,8,7],[15,16,17,12]]))
print(sol.luckyNumbers([[7,8],[1,2]]))