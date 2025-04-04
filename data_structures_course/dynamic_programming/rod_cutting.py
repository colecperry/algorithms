"""
Rod Cutting Problem - Dynamic Programming Solutions

The rod cutting problem is a classic example of optimization using Dynamic Programming.
The goal is to determine the maximum profit by cutting a rod of length `n` into smaller pieces, given a price list for each possible segment length.

This file presents three different solutions:
1. **Recursive Approach (Without Memoization)** - Exponential time complexity (O(2^n)).
2. **Top-Down DP (Memoization)** - Optimized recursion using a dictionary (O(n^2)).
3. **Bottom-Up DP (Tabulation)** - Iterative approach using a DP table (O(n^2)).
"""

# ----------------------
# 1. Recursive Approach (Without Memoization) - Exponential Complexity O(2^n)
# ----------------------
def rod_cutting_recursive(prices, n):
    """
    Compute the maximum obtainable value by recursively cutting a rod of length n.
    :param prices: List of prices for different rod lengths.
    :param n: Length of the rod.
    :return: Maximum value obtainable by cutting the rod.
    """
    
    # Base case: If rod length is 0, no value can be obtained
    if n == 0:
        return 0
    
    # Initialize max_value to a very low number (negative infinity) to ensure we correctly track the highest possible value
    max_value = float('-inf')
    
    # Try all possible ways to cut the rod
    for i in range(1, n + 1): 
        # Compute the best price by making a cut at length `i` which is equal to prices[i - 1], and solving the remaining rod n - i recursively
        max_value = max(max_value, prices[i - 1] + rod_cutting_recursive(prices, n - i))
    
    # Return the maximum profit possible for rod of length n
    return max_value

# Note -> For n = 5, we calculate the smallest cut (i = 1) and then the max val for the rest of the problem (n - i) which is the rest of the rod (4). When we recurse call stack for 4, we calculate the smallest cut (i = 1), and the max val for the rest of the problem again. Eventually we will reach a base case on the call when n = 0, so we go back to the call stack for n = 1 and return 0 for that recursive call and add prices[i-1] (prices[0] = 1) which returns 1 for n = 1. When we get back to n = 2, we return 1 iteration 1 and then for iteration 2 we calculate the price at index 1 (cut of length 2) plus the smaller problem rod_cutting_recursive(prices, n - i) -> n - i = 2 - 2 = 0

# ----------------------
# 2. Top-Down DP Approach (Memoization) - O(n^2) Complexity
# ----------------------
def rod_cutting_memoized(prices, n):
    """
    Optimized recursive approach using memoization to store computed values.
    :param prices: List of prices for different rod lengths.
    :param n: Length of the rod.
    :return: Maximum value obtainable.
    """
    memo = {}  # Dictionary to store computed results
    return rod_cutting_helper(prices, n, memo)

def rod_cutting_helper(prices, n, memo):
    """
    Helper function to implement memoization for recursive rod cutting.
    """
    if n == 0:
        return 0
    if n in memo:
        return memo[n]
    
    max_value = float('-inf')
    
    # Try all possible cut lengths
    for i in range(1, n + 1): # Make cut at "i" and solve rest recursively
        max_value = max(max_value, prices[i - 1] + rod_cutting_helper(prices, n - i, memo))
    
    memo[n] = max_value  # dict stores cut length -> max profit
    return max_value

    # Recursive breakdown for n = 5:
    # n = 5 -> Attempt cut at i = 1
    # n = 4 -> Attempt cut at i = 1
    # n = 3 -> Attempt cut at i = 1
    # n = 2 -> Attempt cut at i = 1
    # n = 1 -> Base case reached with cut at i = 1 -> returns prices[0] + 0 for max_val -> 1
        # memo[1] = 1 (stored result for future calls)
    
    # Returning to n = 2:
    # Unpauses and returns rod_cutting_helper(prices, 2 - 1, memo) = 1
    # max_val = prices[0] + 1 = 2
    # Now tries a larger cut:
    # n = 2 -> Attempt cut at i = 2 -> calls rod_cutting_helper(prices, 2 - 2, memo), which returns base case 0
        # max_val = prices[1] + 0 = 5
        # stores memo[2] = 5 (optimal value for length 2 stored)
    
    # Returning to n = 3:
    # i = 1 -> Unpauses and returns prices[0] + rod_cutting_helper(prices, 3 - 1, memo)
    # The value of rod_cutting_helper(prices, 2, memo) is already memoized (5), so:
        # max_val = prices[0] + 5 = 6
    # Now tries a larger cut:
    # n = 3 -> Attempt cut at i = 2 -> calls rod_cutting_helper(prices, 3 - 2, memo), which returns memo[1] = 1
        # max_val = max(6, prices[1] + 1) = max(6, 5 + 1) = 6
    # n = 3 -> Attempt cut at i = 3 -> calls rod_cutting_helper(prices, 3 - 3, memo), which returns base case 0
        # max_val = max(6, prices[2] + 0) = max(6, 8) = 8
        # memo[3] = 8
    
    # This process repeats up to n = 5, optimizing each step using memoization.


# ----------------------
# 3. Bottom-Up DP Approach (Tabulation) - O(n^2) Complexity
# ----------------------
def rod_cutting_bottom_up(prices, n):
    """
    Iterative approach using a DP table to compute the maximum profit.
    :param prices: List of prices for different rod lengths.
    :param n: Length of the rod.
    :return: Maximum value obtainable.
    """
    dp = [0] * (n + 1)  # Initialize DP table -> add 0 for idx 0
    # Iterate through all lengths 
    for length in range(1, n + 1): 
        max_value = float('-inf')
        
        # Try all possible cut positions for that length
        for cut in range(1, length + 1):
            max_value = max(max_value, prices[cut - 1] + dp[length - cut]) # Max val is the price at that cut plus the best val from DP array for the rest of the rod
        
        dp[length] = max_value  # Store best computed maximum profit for that rod length
    
    return dp[n]

# ----------------------
# Example Usage
# ----------------------
prices = [1, 5, 6, 7, 10]  # Price list
n = len(prices)  # Length of the rod

print(f"Recursive Solution: Maximum value for rod of length {n} =", rod_cutting_recursive(prices, n))
print(f"Top-Down DP (Memoization): Maximum value for rod of length {n} =", rod_cutting_memoized(prices, n))
print(f"Bottom-Up DP (Tabulation): Maximum value for rod of length {n} =", rod_cutting_bottom_up(prices, n))

"""
### Summary of Implementations:
- **Recursive Approach**: Explores all possible cuts but is inefficient (O(2^n)).
- **Top-Down DP (Memoization)**: Uses a dictionary to store results and improve efficiency (O(n^2)).
- **Bottom-Up DP (Tabulation)**: Iterative approach storing results in a DP table (O(n^2)).

### Choosing the Best Approach:
- **Use Memoization if recursion is preferred** and `n` is not extremely large.
- **Use Tabulation for an iterative, efficient approach** that avoids recursion depth limits.
"""