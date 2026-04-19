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
    def maxProfitGreedy(self, prices):
        """
        - TC: O(n) -> One iteration through the prices array
        - SC: O(1) -> only track two variables regardless of input size
        """
        min_price = float('inf') # Best buy price seen so far
        max_profit = 0 # Best profit seen so far

        for price in prices:
            min_price = min(min_price, price) # Would it have been better to buy today?
            profit = price - min_price # If we sell today, what's our profit?
            max_profit = max(max_profit, profit) # Is today's profit the best we've seen?

        return max_profit

solution = Solution()
print(solution.maxProfitGreedy([7,1,5,3,6,4]))

