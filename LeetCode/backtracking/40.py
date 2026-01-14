# 40. Combination Sum II

# Topics: Array, Backtracking

# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

# Example 1:
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]

# Example 2:
# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]

from typing import List

class Solution:
    """
    TC: 2^n -> starting with each ele in the candaites array, and looping over each other ele in the candidates array, choose to include it or not include it
    SC: O(n) where n is the number of candidates - each recursive call increments the index by 1 at least 1, so the max recursion decpth is n
    """
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
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
                # !!! PREVENT DUPLICATES AT THE SAME LEVEL OF RECURSION !!! (DON'T ADD)
                if candidates[i] == candidates[i - 1] and i > start: 
                    continue
                # PRUNING OPTIMIZATION: (DON'T ADD)
                # Since array is sorted, if adding candidates[i] exceeds target, 
                # all remaining will too, so we break early instead of continuing loop
                if current_sum + candidates[i] > target:
                    break  # Not 'continue' - everything after is also too big!
                
                # STEP 1: MAKE CHOICE - add candidate if sum smaller than target
                path.append(candidates[i])
                
                # STEP 2: EXPLORE - recurse with NEXT index i (not i!) & update curr sum
                # This does not allows reusing same element multiple times
                backtrack(i + 1, path, current_sum + candidates[i])
                
                # STEP 3: UNDO CHOICE (BACKTRACK)
                path.pop()
        
        # Start at index 0, empty path, sum=0
        backtrack(0, [], 0)
        return result
    
sol = Solution()
print(sol.combinationSum2([10,1,2,7,6,1,5], 8)) 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# print(sol.combinationSum2([2,5,2,1,2], 5))
# # [
# # [1,2,2],
# # [5]
# # ]

# Sorted input: [1, 1, 2], target = 2
# Indices:       0  1  2


#                                       []
#                                     sum=0
#                                    start=0
#                                    ───────
#                            i=0: pick 1 → recurse
#                            i=1: SKIP (1==1 & 1>0)
#                            i=2: pick 2 → recurse
#                           /                     \
#                          /                       \
#                       [1]                        [2]
#                     sum=1                       sum=2
#                    start=1                     start=3
#                    ───────                     ───────
#              i=1: pick 1 → recurse        i=3: out of bounds
#                 i=2: PRUNED (1+2>2)         sum==target ✓
#                       |                           |
#                       |                           ▼
#                     [1,1]                    SAVE [[2]]
#                     sum=2
#                    start=2
#                    ───────
#                i=2: out of bounds
#                   sum==target ✓
#                       |
#                       ▼
#                 SAVE [[1,1]]


# Final result: [[1,1], [2]]