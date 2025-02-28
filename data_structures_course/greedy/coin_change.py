"""
Greedy Algorithm for US Coin Change Problem

This algorithm finds the minimum number of coins needed to make a given amount using standard US coin denominations: [25, 10, 5, 1] (quarters, dimes, nickels, pennies) -> only works for US denominations, if other denominations greedy may not work

Approach:
1. Start with the highest denomination and use as many of that coin as possible.
2. Move to the next lower denomination and repeat until the amount is zero.
3. This greedy approach works optimally for US coin denominations due to their specific structure.

Time Complexity: O(n) where n is the number of denominations.
"""

def greedy_coin_change(amount):
    """
    Function to determine the minimum number of coins needed for a given amount.
    :param amount: The amount in cents (integer)
    :return: Dictionary with coin denominations and their respective counts
    """
    # US coin denominations in cents
    coins = [25, 10, 5, 1]  # Quarters, Dimes, Nickels, Pennies
    coin_count = {}  # Dictionary to store the count of each coin

    for coin in coins:
        if amount >= coin:
            coin_count[coin] = amount // coin  # Number of coins of this denomination
            amount %= coin  # Reduce the amount by the used coins
    
    return coin_count

# Test input
if __name__ == "__main__":
    test_amount = 87  # Example: 87 cents
    
    print(f"Amount: {test_amount} cents")
    result = greedy_coin_change(test_amount)
    print("Coin Breakdown:", result)