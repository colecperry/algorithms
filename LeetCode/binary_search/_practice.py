from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        # Binary search to find row -> 0, 11
        l, r = 0, rows * cols - 1

        while l <= r:
            mid = l + (r - l) // 2 
            row = mid // cols
            col = mid % cols
            val = matrix[row][col]
            
            if val == target:
                return True
            
            elif val < target: # Value is too small
                l = mid + 1 # Search right half

            else: # Value too large
                r = mid - 1 # Search right half
            
        return False


sol = Solution()
print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)) # True
print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13)) # 5
