# 300. Longest Increasing Subsequence

# Given an integer array nums, return the length of the longest strictly increasing subsequence.

# Example 1:
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

# Example 2:
# Input: nums = [0,1,0,3,2,3]
# Output: 4

# Example 3:
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1

from typing import List

class Solution:
    """
    TC:
        - O(n)^2 for nested iteration
    SC:
        - O(n) for storing one num per index in DP
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] stores the length of the longest increasing subsequence that ends at index i
        dp = [1] * len(nums)
        
        # Build up solutions for each position
        for i in range(len(nums)):
            # Check all previous elements
            for j in range(i):
                # If we found a smaller element, we can extend its subsequence
                if nums[j] < nums[i]:
                    # We're checking multiple j values, so we want the longest subsequence
                    # dp[i]: current best (from previous j values we checked)
                    # dp[j] + 1: new option (extend subsequence at j by adding nums[i])
                    dp[i] = max(dp[i], dp[j] + 1)  # Keep the longest option
        
        return max(dp) # ans is max subsequence up to any index

sol = Solution()
print(sol.lengthOfLIS([10,9,2,5,3,7,101,18])) # 4
print(sol.lengthOfLIS([0,1,0,3,2,3])) # 4
print(sol.lengthOfLIS([7,7,7,7,7,7,7])) # 1
