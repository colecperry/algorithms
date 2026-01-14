# 47. Permutations II

# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

# Example 1:
# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]

# Example 2:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()  # Sort to group duplicates together for easy skip logic
        
        def backtrack(path, used):
            # BASE CASE: Permutation complete when path has all elements
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            for i in range(len(nums)):  # Try all i (no start - permutations use all positions)
                # Skip if this element is already in the current path
                if used[i]:
                    continue
                
                # Skip duplicate: if current num equals previous AND previous wasn't used,
                # we should've picked the previous one first — skip to avoid duplicates
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                
                path.append(nums[i])      # Choose
                used[i] = True
                backtrack(path, used)     # Explore
                path.pop()                # Unchoose (backtrack)
                used[i] = False
        
        backtrack([], [False] * len(nums))
        return result

sol = Solution()

print(sol.permuteUnique([1,1,2]))
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]

print(sol.permuteUnique([1,2,3]))
# [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# DECISION TREE for nums = [1, 2, 2] (sorted)

#                                   []
#                            used=[F, F, F]
#                                ───────
#                       i=0: pick 1 → recurse
#                       i=1: pick 2 → recurse
#                       i=2: SKIP (2==2 & !used[1])
#                     /                            \
#                    /                              \
#                   /                                \
#                  /                                  \
#               [1]                                   [2]
#        used=[T, F, F]                         used=[F, T, F]
#           ───────                                 ───────
#     i=0: SKIP (used)                      i=0: pick 1 → recurse
#     i=1: pick 2 → recurse                 i=1: SKIP (used)
#     i=2: SKIP (2==2 & !used[1])           i=2: pick 2 → recurse
#             |                            /                     \
#             |                           /                       \
#             |                          /                         \
#           [1,2]                     [2,1]                       [2,2]
#     used=[T, T, F]              used=[T, T, F]             used=[F, T, T]
#          ───────                   ───────                     ───────
#     i=0: SKIP (used)           i=0: SKIP (used)           i=0: pick 1 → recurse
#     i=1: SKIP (used)           i=1: SKIP (used)           i=1: SKIP (used)
#     i=2: pick 2 → recurse      i=2: pick 2 → recurse      i=2: SKIP (used)
#             |                         |                          |
#             |                         |                          |
#         [1,2,2]                    [2,1,2]                    [2,2,1]
#     used=[T, T, T]             used=[T, T, T]             used=[T, T, T]
#          ───────                   ───────                    ───────
#     len(path)==3 ✓              len(path)==3 ✓             len(path)==3 ✓
#             |                         |                          |
#             ▼                         ▼                          ▼
#       SAVE [1,2,2]               SAVE [2,1,2]               SAVE [2,2,1]


# Final result: [[1,2,2], [2,1,2], [2,2,1]]

# SCENARIO 1: At root [], trying to pick i=2

#     path = []
#     used = [F, F, F]
#                 ↑
#             used[1] = False (first "2" is NOT in path)
    
#     Check: nums[2] == nums[1] and not used[1]
#                 2 == 2        and not False
#                 TRUE          and TRUE
#                          → SKIP
    
#     Why? The first "2" is available. If you want a "2", pick THAT one.
#          Picking the second "2" first would create a duplicate path later.


# SCENARIO 2: At [2], trying to pick i=2

#     path = [2]           ← we picked index 1 (the first "2")
#     used = [F, T, F]
#                 ↑
#             used[1] = True (first "2" IS in path)
    
#     Check: nums[2] == nums[1] and not used[1]
#                 2 == 2        and not True
#                 TRUE          and FALSE
#                          → DON'T SKIP (take it!)
    
#     Why? The first "2" is already used. We NEED the second "2" 
#          to build [2, 2, 1].