# 70. Climbing Stairs

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

class Solution:
    def climbStairs(self, n: int) -> int: # O(n) space
        """
        TC:
            - O(n) - only iterate once to fill out DP table, return last ele
        SC:
            - O(n) - must store dp for each ele in n
        """
        dp = [0] * (n + 1) # Number of ways to reach that step
        dp[0] = 1 # DP base cases -> 1 way to get to steps 1 & 2
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2] # Ways to get to curr step = ways from 1 step back + ways from 2 steps back
        return dp[-1]
    
    def climbStairs2(self, n: int) -> int: # O(1) space
        """
        TC: O(n) - single pass through n
        SC: O(1) - only storing two variables
        """
        if n <= 1:
            return 1
        
        prev2 = 1  # Ways to reach step i-2 (initially step 0)
        prev1 = 1  # Ways to reach step i-1 (initially step 1)
        
        for _ in range(2, n + 1):
            curr = prev1 + prev2  # Ways to reach current step
            prev2 = prev1  # Shift: old prev1 becomes new prev2
            prev1 = curr   # Shift: current becomes new prev1
        
        return prev1

sol = Solution()
print(sol.climbStairs(2)) # 2
print(sol.climbStairs(3)) # 3

print(sol.climbStairs2(2)) # 2
print(sol.climbStairs2(3)) # 3
