# 46. Permutations

# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]

# Example 3:
# Input: nums = [1]
# Output: [[1]]

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []  # Store all complete permutations
        
        def backtrack(path, used):
            """
            Build permutations one element at a time.
            - path: current permutation being built
            - used: boolean array tracking which elements are in path
            """
            # BASE CASE: Permutation complete when all n elements used
            if len(path) == len(nums):
                result.append(path[:])  # Save copy (not reference!)
                return
            
            # RECURSIVE CASE: Try adding each unused element
            for i in range(len(nums)):
                # PRUNING: Skip if element already in current permutation
                if used[i]:
                    continue
                
                # STEP 1: MAKE CHOICE - add element to permutation
                path.append(nums[i])
                used[i] = True  # Mark as used
                
                # STEP 2: EXPLORE - recursively build rest
                backtrack(path, used)
                
                # STEP 3: UNDO CHOICE (BACKTRACK) - restore state
                path.pop()       # Remove element
                used[i] = False  # Mark as unused
        
        # Start with empty path, nothing used
        backtrack([], [False] * len(nums))
        return result
    



# ============================================
# VISUALIZATION FOR PERMUTATIONS: nums=[1,2]
# ============================================
#
#                     backtrack(path=[], used=[F,F])
#                           /                \
#                      TRY 1                  TRY 2
#                        /                      \
#               path=[1]                      path=[2]
#             used=[T,F]                    used=[F,T]
#                  /    \                      /    \
#              TRY 1  TRY 2                TRY 1  TRY 2
#              (skip)   |                    |    (skip)
#                       |                    |
#                   path=[1,2]           path=[2,1]
#                   used=[T,T]           used=[T,T]
#                       ✓                     ✓
#                     SAVE                  SAVE
#
# Result: [[1,2], [2,1]]
#



# ============================================
# VISUALIZATION FOR PERMUTATIONS: nums=[1,2,3]
# ============================================   
# 
#                         path = []
#                 /          |          \     
#                /           |           \
#               1            2            3    
#         path=[1]        path=[2]        path=[3]   
#        /      |        |       |        |       \
#       /       |        |       |        |        \
#      2        3        1       3        1         2
#   [1,2]     [1,3]    [2,1]   [2,3]    [3,1]      [3,2]
#     |         |        |       |        |          |
#     3         2        3       1        2          1
#  [1,2,3]   [1,3,2]  [2,1,3] [2,3,1]  [3,1,2]    [3,2,1]

sol = Solution()
print(sol.permute([1,2])) # [[1,2],[2,1]]
print(sol.permute([1,2,3])) # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]