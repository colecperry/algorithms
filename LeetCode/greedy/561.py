# 561. Array Partition

# Topics: Array, Greedy, Sorting, Counting Sort

# Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

# Example 1:
# Input: nums = [1,4,3,2]
# Output: 4
# Explanation: All possible pairings (ignoring the ordering of elements) are:
# 1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
# 2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
# 3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
# So the maximum possible sum is 4.

# Example 2:
# Input: nums = [6,2,6,5,1,2]
# Output: 9
# Explanation: The optimal pairing is (2, 1), (2, 5), (6, 6). min(2, 1) + min(2, 5) + min(6, 6) = 1 + 2 + 6 = 9.

"""
BIG PICTURE:
- We must pair up numbers and keep only the minimum from each pair
- Goal: maximize the sum of these minimums
- Key insight: pair each number with its closest neighbor so we only "waste" the min number possible

WHY GREEDY WORKS:
- Sort the array so similar numbers are adjacent
- Pair neighbors: (nums[0], nums[1]), (nums[2], nums[3]), etc.
- This ensures we keep the largest possible minimums (nums[0], nums[2], nums[4]...)
- Any other pairing forces us to keep smaller numbers

APPROACH:
1. Sort the array
2. Take every other element starting from index 0 (these are the minimums of optimal pairs)
3. Sum them up

TC: O(n log n) - we sort the array, then iterate through it once to build the ans
SC: O(n) for python's timsort's merge operations, although some interviewers consider this 0(1)
"""

from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(0, len(nums) - 1, 2):
            ans += nums[i] 
        return ans

sol = Solution()

print(sol.arrayPairSum([1,4,3,2])) # 4
print(sol.arrayPairSum([6,2,6,5,1,2])) # 9
