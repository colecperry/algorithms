# 322. Coin Change

# Topics: Array, Dynamic Programming, Breadth-First Search

# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

# Example 1:
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1

# Example 2:
# Input: coins = [2], amount = 3
# Output: -1

# Example 3:
# Input: coins = [1], amount = 0
# Output: 0

# -----------------------
# 💡 How to Solve:
# -----------------------

# Use Dynamic Programming to build up a solution from amount 0 to the target amount

# Initialize a DP array of size (amount + 1), where dp[i] = minimum coins to make amount i

# Set dp[0] = 0 (base case) because 0 coins are needed to make amount 0
# Set all other entries to infinity initially, meaning unreachable

# For each coin:
#   - Loop through every amount from coin to target amount
#   - At each step i, try to improve dp[i] by taking the minimum of:
#       - current dp[i]
#       - dp[i - coin] + 1 (1 extra coin added to amount i - coin)

# After filling the dp array, check dp[amount]
# If it's still infinity, return -1 (impossible to make amount)
# Otherwise, return dp[amount] (minimum coins needed)

# -----------------------
# ⏱️ Time Complexity:
# -----------------------

# O(amount * len(coins))
# - For each coin, we loop through up to 'amount' entries in the DP array

# -----------------------
# 📦 Space Complexity:
# -----------------------

# O(amount)
# - We use a one-dimensional DP array of size (amount + 1)


from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1) # init DP arr -> dp[i] = min coins to make amount i
        dp[0] = 0 # Base case -> 0 coins to make amount 0

        for coin in coins: 
            for i in range(coin, amount + 1): # loop from coin to target amt (coin can't make improve dp arr for any values less than it)
                dp[i] = min(dp[i], dp[i - coin] + 1) # try to improve dp[i] by taking min of curr dp[i] and the remainder after using the coin (add one for the current coin)
        
        return dp[amount] if dp[amount] != float('inf') else -1 # return the best dp arr value for "amount", if it's a float it was impossible to make that amount, so return -1

sol = Solution()
print(sol.coinChange([1,2,5], 11)) # 3
print(sol.coinChange([2], 3)) # -1
print(sol.coinChange([1], 0)) # 0