# 78. Subsets

# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Example 2:
# Input: nums = [0]
# Output: [[],[0]]

from typing import List

class Solution: # LC 78: Subsets
    """
    TC: O(2^n * n)
        - 2^n subsets - Each element has 2 choices: in or out, each subset can be up to n elements long
        - O(n) copy - It takes O(n) to copy each subset in worst case
    
    SC: O(n)
        - Recursion depth: O(n) - maximum n ele deep (including every element: []→[1]→[1,2]→[1,2,3])
        - Path storage: O(n) - current subset being built -> path never exceeds n elements
        - O(n) + O(n) = O(n)
    
    Key insight:
    - CRITICAL difference from combinations: save at EVERY level!
    - Combinations: save only when len(path) == k
    - Subsets: save immediately on entering function
    - Empty subset [] is valid, as are all partial builds [1], [1,2], etc.
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []  # Store all subsets
        
        def backtrack(start, path):
            """
            Build subsets incrementally, saving at every step.
            
            Args:
                start: Index to start considering elements from
                path: Current subset being built (e.g., [1,2])
            """
            # KEY INSIGHT: Save current subset at EVERY level!
            # This is the main difference from combinations pattern
            # [] is a valid subset, [1] is valid, [1,2] is valid, etc.
            result.append(path[:])  # Save copy of current state
            
            # RECURSIVE CASE: Try adding each remaining element
            # Note: No explicit base case needed!
            # When start >= len(nums), loop doesn't run, function returns naturally
            for i in range(start, len(nums)):
                # STEP 1: MAKE CHOICE - include nums[i] in subset
                path.append(nums[i])
                
                # STEP 2: EXPLORE - build subsets with nums[i] included
                # Pass i+1 to avoid reusing same element
                backtrack(i + 1, path)
                
                # STEP 3: UNDO CHOICE (BACKTRACK) - exclude nums[i]
                # Remove to try subsets without this element once loop ends
                path.pop()
        
        # Start at index 0, empty path
        backtrack(0, [])
        return result

# ============================================
# VISUALIZATION FOR SUBSETS: nums=[1,2,3]
# ============================================
#
#                              backtrack(start=0, path=[])
#                                💾 SAVE [] → result=[[]]
#                            /              |              \
#                        TRY 1            TRY 2           TRY 3
#                          /                |                \
#                   path=[1]             path=[2]            path=[3]
#                 start=1                start=2             start=3
#             💾 SAVE [1]                💾 SAVE [2]          💾 SAVE [3]
#              /       \                    |             (no more elements)
#         TRY 2       TRY 3               TRY 3
#           /            \                  |
#       path=[1,2]     path=[1,3]       path=[2,3]
#       start=2        start=3          start=3
#    💾 SAVE [1,2]   💾 SAVE [1,3]    💾 SAVE [2,3]
#         |            (no more)        (no more)
#       TRY 3
#         |
#    path=[1,2,3]
#    start=3
# 💾 SAVE [1,2,3]
# (no more elements)
#

sol = Solution()
print(sol.subsets([1,2,3])) # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
print(sol.subsets([0])) # [[],[0]]