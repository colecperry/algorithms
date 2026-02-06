# 121 - Best Time to Buy and Sell Stock

# Topics - Array, Dynamic Programming

# You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1: Input: prices = [7,1,5,3,6,4]
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example 2: Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

from typing import List

class Solution(object):
    def maxProfitDP(self, prices: List[int]) -> int:
        """
        TC: O(n) -> One iteration through prices
        SC: O(n) -> Track max profit for each day n where n = price on ith day
        """
        n = len(prices)
        dp = [0] * n # dp[i] = max profit you can make by day i
        min_price = float('inf') # min price we've seen so far

        for i in range(len(prices)):
            min_price = min(min_price, prices[i]) # Update min price we've seen
            # Recurrence relation -> don't sell today or sell today
            hold = dp[i-1]
            sell = prices[i] - min_price
            dp[i] = max(hold, sell) # which makes us more profit?

        return dp[-1]

    def maxProfitGreedy(self, prices):
        """
        - TC: O(n) -> One iteration through the prices array
        - SC: O(1) -> only need to track variables
        """
        min_price = float('inf') # Create variable to track min price
        max_profit = 0 # Create variable to track max profit

        for price in prices:
            min_price = min(min_price, price) # Update min price if current price is smaller
            profit = price - min_price # Calculate profit for each element(price)
            max_profit = max(max_profit, profit) # Update max profit

        return max_profit

solution = Solution()
print(solution.maxProfit2([7,1,5,3,6,4]))

