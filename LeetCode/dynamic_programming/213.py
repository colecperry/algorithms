# 213. House Robber II

# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

# Example 1:
# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

# Example 2:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        House Robber II - houses arranged in circle (can't rob first AND last)
        TC: O(n) - two passes through array for 2 function calls
        SC: O(n) - for dp array
        """
        # Edge case: only one house, just rob it
        if len(nums) == 1:
            return nums[0]
        
        def rob_range(start, end):
            """
            Rob houses from index start to end (exclusive)
            Example: rob_range(0, 3) means rob houses at indices 0, 1, 2
            """
            # Edge case: only one house in range
            if end - start == 1:
                return nums[start]
            
            # Number of houses in this range
            n = end - start
            
            # dp[i] = max money we can rob from first i houses in range
            dp = [0] * n
            
            # Base case 1: Rob first house in range
            dp[0] = nums[start]
            
            # Base case 2: Rob first or second house (whichever is bigger)
            dp[1] = max(nums[start], nums[start + 1])
            
            # For each remaining house in range
            for i in range(2, n):
                # Choice 1: Skip current house, take best from previous houses
                skip = dp[i-1]
                
                # Choice 2: Rob current house + best from houses before previous
                rob = dp[i-2] + nums[start + i]
                
                # Take the max of the two choices
                dp[i] = max(skip, rob)
            
            # Return max money from all houses in range
            return dp[-1]
        
        # Case 1: Skip last house (can rob first house)
        # Rob houses from index 0 to n-2 (stops before len - 1)
        skip_last = rob_range(0, len(nums) - 1) 
        
        # Case 2: Skip first house (can rob last house)
        # Rob houses from index 1 to n-1 (stops at len - 1)
        skip_first = rob_range(1, len(nums))
        
        # Return the better of the two strategies
        return max(skip_last, skip_first)

sol = Solution()
print(sol.rob([2,3,2])) # 3
print(sol.rob([1,2,3,1])) # 4