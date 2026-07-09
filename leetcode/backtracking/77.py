# 77. Combinations

# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

# You may return the answer in any order.

# Example 1:
# Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
# Explanation: There are 4 choose 2 = 6 total combinations.
# Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

# Example 2:
# Input: n = 1, k = 1
# Output: [[1]]
# Explanation: There is 1 choose 1 = 1 total combination.

from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]: # LC 77
        """
        TC: O(C(n,k) * k) 
            - C(n,k) = n!/(k!(n-k)!) number of combinations exist for "n choose k"
            - O(k) work per combination -> each combination takes O(k) to copy to result (each combination is exactly k elements)
            - Example: C(4,2) = 6, so O(6 * 2) = O(12)
    
        SC: O(k)
            - O(k) recursion depth - we add one element at a time until we have k elements
            - O(k) path storage - path only ever holds k elements max
        """
        result = []  # Store all complete combinations
        
        def backtrack(start, path):
            """
            Build combinations one element at a time.
            
            Args:
                start: First number to consider (prevents going backwards)
                path: Current combination being built (e.g., [1,2])
            """
            # BASE CASE: Combination complete when we have k elements
            if len(path) == k:
                result.append(path[:])  # Save shallow copy -> new list with eles
                return    # at this moment in time & return to prev callstack
            
            # RECURSIVE CASE: Try adding each number from start to n
            # Key: start from 'start', not from 1! This prevents duplicates
            for i in range(start, n + 1):
                # STEP 1: MAKE CHOICE - add number i
                path.append(i)
                
                # STEP 2: EXPLORE - build rest starting from i+1
                backtrack(i + 1, path)
                
                # STEP 3: UNDO CHOICE (BACKTRACK)
                path.pop()
        
        # Start at 1, empty path
        backtrack(1, [])
        return result

# ============================================
# VISUALIZATION FOR COMBINATIONS: n=4, k=2
# ============================================
#
#                           backtrack(start=1, path=[])
#                      /          |            |           \
#                  TRY 1        TRY 2         TRY 3       TRY 4
#                    /            |            |             \
#              path=[1]       path=[2]      path=[3]        path=[4]
#              start=2        start=3       start=4         start=5
#             /  |   \          /  \           |        (k not reached)
#         TRY   TRY   TRY     TRY   TRY      TRY 4
#          2     3     4       3     4         |
#          |     |     |       |     |         |
#       [1,2]  [1,3] [1,4]   [2,3] [2,4]     [3,4]
#         ✓      ✓     ✓       ✓     ✓         ✓
#       SAVE   SAVE  SAVE    SAVE   SAVE     SAVE
#
# Result: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
#
# Key: start index prevents going backwards
#   After choosing 1, can only try 2,3,4 (not 1 again)
#   After choosing 2, can only try 3,4 (not 1 or 2)
#   After choosing 3, can only try 4 (not 1,2, or 3)
        
sol = Solution()
print(sol.combine(4, 2))
print(sol.combine(1, 1))