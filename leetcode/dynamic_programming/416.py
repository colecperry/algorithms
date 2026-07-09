# 416. Partition Equal Subset Sum

# Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

# Example 1:
# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].

# Example 2:
# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.

class Solution(object):
    def canPartition(self, nums):
        """
        - TC: Loop through each num -> O(n), loop through each target sum -> O(target), total = O(n * target) where target = sum(nums) / 2
        - SC: Create a DP array for each potential target sum -> O(target)
        """
        total = sum(nums)
        if total % 2 != 0: # If total sum is odd, can't partition
            return False
        
        target = total // 2 # Find target num for each partition
        dp = [False] * (target + 1) # dp[i] -> Can we make sum "i"?
        dp[0] = True # base case -> can always make sum 0

        # For each num, update which sums are now achievable
        for num in nums: 
            # Backwards prevents using num twice (ensures 0/1 property)
            for i in range(target, num - 1, -1):
                if dp[i - num]: # If we could make (i - num) before
                    dp[i] = True # Then we can make i now (add num)
                    
        return dp[target]

sol = Solution()
print(sol.canPartition([1,5,11,5])) # True
print(sol.canPartition([1,2,3,5])) # False

"""
WHY BACKWARDS?

Example with num = 5, initially dp = [T, F, F, F, F, F, F, F, F, F, F]

FORWARD (WRONG):
i=5:  dp[5] = True   (using dp[0])  <- Sets dp[5] to True
i=10: dp[10] = True  (using dp[5])  <- Uses the dp[5] we JUST set!
Result: Used 5 twice (5 + 5 = 10) - violates 0/1 knapsack ✗

BACKWARD (CORRECT):
i=10: dp[10] stays False (using OLD dp[5] = False)
i=5:  dp[5] = True       (using dp[0])
Result: Used 5 once ✓
"""