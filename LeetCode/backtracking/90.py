# 90. Subsets II

# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:

# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()  # Sort to group duplicates together for easy skip logic

        def backtrack(start, path):
            # Every path (including empty) is a valid subset - save immediately
            result.append(path[:])

            for i in range(start, len(nums)):
                # Skip duplicates: if current element equals previous AND
                # we're past the first choice at this level (i > start),
                # then this branch would create a duplicate subset
                if i > start and nums[i] == nums[i - 1]: # Don't choose
                    continue
                
                path.append(nums[i])      # Choose
                backtrack(i + 1, path)    # Explore (move to next index)
                path.pop()                # Unchoose (backtrack)
        
        backtrack(0, [])
        return result


# DECISION TREE for nums = [1, 2, 2] (sorted)

#                                                    []
#                                                 start=0
#                                                SAVE [[]]
#                                                 ───────
#                                         i=0: pick 1 → recurse
#                                         i=1: pick 2 → recurse
#                                         i=2: SKIP (2==2 & 2>0)
#                                        /                       \
#                                       /                         \
#                                     [1]                         [2]
#                                   start=1                     start=2
#                                  SAVE [1]                    SAVE [2]
#                                   ───────                     ───────
#                           i=1: pick 2 → recurse         i=2: pick 2 → recurse
#                           i=2: SKIP (2==2 & 2>1)                 |
#                                     |                            |
#                                     |                            |
#                                   [1,2]                        [2,2]
#                                 start=2                       start=3
#                                SAVE [1,2]                    SAVE [2,2]
#                                 ───────                       ───────
#                         i=2: pick 2 → recurse              out of bounds
#                                    |
#                                    |
#                                 [1,2,2]
#                                 start=3
#                               SAVE [1,2,2]
#                                 ───────
#                              out of bounds


# KEY INSIGHT: The duplicate skip condition (i > start and nums[i] == nums[i-1])

#   - At start=0: choices are indices [0,1,2] → values [1,2,2]
#                 i=2 is SKIPPED because nums[2]==nums[1] and 2>0
#                 This prevents [] → [2] from happening twice

#   - At start=1 (inside [1]): choices are indices [1,2] → values [2,2]  
#                 i=2 is SKIPPED because nums[2]==nums[1] and 2>1
#                 This prevents [1] → [1,2] from happening twice

#   - At start=2: i=2 is NOT skipped because 2>2 is FALSE
#                 First occurrence at each level is always allowed!


# Final result: [[], [1], [1,2], [1,2,2], [2], [2,2]]