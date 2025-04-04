# Coin change: Bottom Up Approach
    # Initialize DP array for for each possible amount
    # Iterate through the coins array
        # Iterate through each possible amount 
        # Store in the DP array the min of the current DP value for that amount or take the remaining amount after using the current coin -> (i - coin), find the minimum number of coins to make that amount -> (dp[i - coin]), and add one for the current coin we're using
    # Return the min number of coins for that specific amount (stored in memo table)


    # Time Complexity: O(amount × n)
    # - We iterate over each coin (n coins)
    # - For each coin, we loop from coin value up to the target amount → O(amount)
    # - Total time = O(n × amount)

    # Space Complexity: O(amount)
    # - We use a single DP array of size (amount + 1) to store the minimum number of coins

# Bottom Up
def coin_change_bottom_up(coins, amount):
    dp = [float('inf')] * (amount + 1) # Initialize DP array
    dp[0] = 0 # Set index 0 to 0 -> amount 0 requires 0 coins
    
    for coin in coins: # Iterate through coins
        for i in range(coin, amount + 1): # For each possible amount
            dp[i] = min(dp[i], dp[i - coin] + 1) # DP value is the min of curr val in DP array or the number of coins needed to make amount i - coin plus one (the current coin we're using)
    
    return dp[amount] if dp[amount] != float('inf') else -1

# Example usage:
coins = [1, 2, 5]
amount = 11
print(f"Minimum coins needed to make amount {amount} =", coin_change_bottom_up(coins, amount))


# Coin change: Top Down Approach
    # Create a memo dict -> amount to min coins needed for that amount
    # Call recursive helper function with amount
        # Base case 1 -> If remaining amount = 0, no more coins needed, return 0
        # Base case 2 -> If remaining amount is negative, we overshot the amount, return inf
        # Memo check -> Check if subproblem is already solved and instantly return min coins
        # Store min coins for this amount
        # Loop through each coin
            # Find and store the result (min coins needed) for the remaining amount after using the coin recursively
            # Update min coins needed -> add one for coin we just used
        # Memoize the min number of coins for that amount

    # Time Complexity: O(amount × n)
    # - In the worst case, we may try every coin for every sub-amount (amount values)
    # - Memoization ensures each subproblem is solved only once → O(amount)
    # - Each subproblem tries up to n coins → O(n)
    # - Total time = O(n × amount)

    # Space Complexity: O(amount)
    # - Memoization table stores one entry per sub-amount → O(amount)
    # - Recursion call stack can go as deep as amount → O(amount)


# Top Down Approach
def coin_change_top_down(coins, amount):
    memo = {} # Create a memoization table to store results of subproblems
    
    # Helper function to perform the recursive calculation
    def dp(remaining_amount):

        if remaining_amount == 0: # Base case 1 -> no more coins needed
            return 0

        if remaining_amount < 0: # Base case 2 -> coin overshot amount
            return float('inf')
        
        if remaining_amount in memo: # If subproblem already solved
            return memo[remaining_amount] # Return the # of coins
        
        # Try each coin and calculate the result
        min_coins = float('inf') # Store min coins for each amount
        for coin in coins: # For each coin at this amount
            result = dp(remaining_amount - coin) # Find min coins for remaining amount after using coin
            if result != float('inf'):
                min_coins = min(min_coins, result + 1) # Track min coins for this call stack (coin and amt), ++ res for current coin
        
        # Memoize min number of coins for the current remaining amount
        memo[remaining_amount] = min_coins
        return min_coins # Return min number of coins for that amount
    
    # Get the result from the recursive helper function for final return
    result = dp(amount) # Recursive call with amount passed in starts recursion
    
    # If the result is infinity, it means we can't form the amount with the given coins
    return result if result != float('inf') else -1

# Example usage:
coins = [1, 2, 5]
amount = 11
result = coin_change_top_down(coins, amount)
print(f"Minimum coins required: {result}")

# Coin change: Bottom Up with Traceback
    # Before we were focused on how many coins to give, now we want to determine which extact coins were used to get the amount
    # Big Idea:
        # Maintain an array where array[i] represents the minimum number of coins needed to make the amount i
        # Additionally, maintain a coin_used array to keep track of the last coin used to make that amount
        # After filling the first array, we trace back from array[amount] using the coin_used array to determine the actual coins used


def coin_change_bottom_up_traceback(coins, amount):
    # Initialize dp array to store the minimum number of coins for each amount
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # No coins are needed to make the amount 0
    
    # Initialize array to track the last coin used after making dp[i - coin]
    coin_used = [-1] * (amount + 1)  # -1 means no coin was used for that amount
    
    # Build up the dp array
    for coin in coins: # Try each coin
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]: # Check if we can make the amount with less coins
                dp[i] = dp[i - coin] + 1 # Update min coins for that amt
                coin_used[i] = coin  # Track the coin used for amount i
    
    # If dp[amount] is still infinity, it's not possible to make the amount
    if dp[amount] == float('inf'):
        return -1, [] # We never found a valid way to build "amount"
    
    # Traceback to find which coins were used to get current amount
    coins_used = [] # Array to display coins used to make amount
    current_amount = amount # Track current amount -> starts at current amount and decreases after using each coin
    while current_amount > 0:
        coin = coin_used[current_amount] # Get last coin used for amt
        if coin == -1:
            break  # This should never happen if dp[amount] is not infinity
        coins_used.append(coin) # Add that coin to the list
        current_amount -= coin # Subtract coin from current_amount to get new current amount
    
    # Return the minimum number of coins and the list of coins used
    return dp[amount], coins_used

# Example usage:
coins = [1, 2, 5]
amount = 11
min_coins, coins_used = coin_change_bottom_up_traceback(coins, amount)
print(f"Minimum coins required: {min_coins}")
print(f"Coins used: {coins_used}")
