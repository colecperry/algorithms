from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i] = max profit you can make by house i
        dp = [0] * (n + 1)
        dp[1] = nums[0] # only one house to choose from

        for i in range(2, n + 1):
            # Recurrence relation
            # Rob current house and take money from 2 houses ago
            rob = nums[i-1] + dp[i-2]
            # Skip this house and take money from prev house
            skip = dp[i-1]

            dp[i] = max(rob, skip)

        return dp[-1]

solution = Solution()
print(solution.rob([1,2,3,1])) # 4
print(solution.rob([2,7,9,3,1])) # 12
