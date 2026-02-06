# 39. Combination Sum

# Topics: Array, Backtracking

# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

# Example 1:
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.

# Example 2:
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]

# Example 3:
# Input: candidates = [2], target = 1
# Output: []

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        TC: O(n^d) where n = len(candidates), d = target / min_candidate
            - Decision tree: up to n choices per node, d levels deep
            - d = longest possible combination (e.g., target=8, min=2 → [2,2,2,2] → d=4)
        
        SC: O(d)
            - O(d) recursion depth
            - O(d) path array (reused via backtracking)
        """
        result = []
        candidates.sort()  # Enable pruning optimization
        
        def backtrack(start, path, current_sum):
            """
            Build combinations that sum to target, allowing reuse.
            
            Args:
                start: Index to start considering candidates from
                path: Current combination being built (e.g., [2,2,3])
                current_sum: Sum of elements in path so far
            """
            # BASE CASE: Found valid combination!
            if current_sum == target:
                result.append(path[:])  # Save copy
                return
            
            # RECURSIVE CASE: Try adding each candidate
            for i in range(start, len(candidates)):
                # PRUNING OPTIMIZATION: Since array is sorted,
                # if adding candidates[i] exceeds target, all remaining will too, so we break early instead of continuing loop
                if current_sum + candidates[i] > target:
                    break  # Not 'continue' - everything after is also too big!
                
                # STEP 1: MAKE CHOICE - add candidate
                path.append(candidates[i])
                
                # STEP 2: EXPLORE - recurse with SAME index i (not i+1!)
                # This allows reusing same element multiple times
                # [2,2,3] is built by: add 2 at i=0, recurse with i=0, add 2 again
                backtrack(i, path, current_sum + candidates[i])
                
                # STEP 3: UNDO CHOICE (BACKTRACK)
                path.pop()
        
        # Start at index 0, empty path, sum=0
        backtrack(0, [], 0)
        return result
    
sol = Solution()
print(sol.combinationSum([2,3], 5)) # [[2,3]]
print(sol.combinationSum([2,3,6,7], 7)) # [[2,2,3],[7]]
print(sol.combinationSum([2,3,5], 8)) # [[2,2,2,2],[2,3,3],[3,5]]
print(sol.combinationSum([2], 1)) # []

# ═══════════════════════════════════════════════════════════════════
# DECISION TREE: combinationSum([2,3], target=5)
# ═══════════════════════════════════════════════════════════════════
#
#                                 [] 
#                               sum=0
#                              start=0
#                            /         \
#                        +2 /           \ +3
#                          /             \
#                       [2]               [3]
#                     sum=2               sum=3
#                    start=0             start=1
#                    /     \                |
#               +2 /        \ +3            | +3
#                 /          \              |
#             [2,2]         [2,3]           ✗
#             sum=4         sum=5         3+3=6>5
#            start=0       start=1        PRUNED
#              |              |
#              |              ▼
#         +2   ✗           ✓ SAVE
#        4+2=6>5         result=[[2,3]]
#        PRUNED