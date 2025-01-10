# You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1: Input: prices = [7,1,5,3,6,4]
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example 2: Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

# Solution 1 -> O(n) time complexity
# Create variables for min price and max profit
# Iterate through prices array:
    # Update min price on each iteration
    # Calculate profit on each iteration
    # Update max profit on each iteration
class Solution(object):
    def maxProfit(self, prices):
        if not prices: # If the prices array is empty return 0
            return 0
        min_price = float('inf') # Create variable to track min price
        max_profit = 0 # Create variable to track max profit

        for price in prices:
            min_price = min(min_price, price) # Update min price if current price is smaller
            profit = price - min_price # Calculate profit for each element(price)
            max_profit = max(max_profit, profit) # Update max profit

        return max_profit


# Solution 2 -> O(n^2) will get time limit exceeded
# Step 1: Create the first "for" loop that loops through the array starting at index 0
# Step 2: Create a second "for" loop that loops through the array starting at index 1, and once it finishes it adds i+1 and loops through again
# Step 3: Since i is always one ahead in the j loop, subtract prices[j] - prices[i] in each loop
# Step 4: At the end of each loop, subtract the prices of the index that j is currently at minus the index that i is currently at. During the first loop, that would be prices[1] - prices[0]


    def maxProfit2(self, prices):
        x=0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                diff = prices[j] - prices[i]
                # print("diff", diff)
                x=max(x, diff)
        return x

solution = Solution()
print(solution.maxProfit2([7,1,5,3,6,4]))

# -- FASTER -- 
# class Solution(object):
#     def maxProfit(self, prices):
#         min_price = prices[0]
#         max_profit = 0

#         for price in prices:
#             profit = price - min_price
#             min_price = min(min_price, price)
#             max_profit = max(max_profit, profit)
#               print("profit", profit)
#               print("min_price", min_price)
#               print("max_profit", max_profit)
#         return max_profit

# solution = Solution()
# print(solution.maxProfit([7,1,5,3,6,4]))
