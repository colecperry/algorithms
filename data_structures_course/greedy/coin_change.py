"""
Cashier Algorithm - Greedy Approach for Making Change

This function calculates the minimum number of coins or bills needed to make change for a given amount using a provided list of denominations.

The algorithm follows a **greedy approach**, where it:
1. Always takes the largest available denomination first.
2. Determines how many times that denomination can fit into the remaining amount.
3. Updates the remaining amount accordingly.
4. Moves to the next largest denomination.

This method works optimally when the denominations are structured like standard currencies (e.g., US dollars, Euros) but may fail for arbitrary denominations.
"""

def cashier_algorithm(amount, denominations):
    """
    Computes the minimum number of coins/bills needed to make change for a given amount.
    :param amount: The total amount to make change for.
    :param denominations: A list of available coin/bill denominations (should be sorted in descending order).
    :return: A dictionary where keys are denominations and values are counts.
    """
    
    change = {}  # Dictionary to store the count of each denomination used
    
    for coin in denominations:
        if amount >= coin:
            count = amount // coin  # Determine how many of this coin/bill fit in the remaining amount (floor division)
            change[coin] = count  # Store the count of this denomination
            amount -= count * coin  # Reduce the remaining amount
    
    return change

# Example usage:
denominations = [100, 25, 10, 5, 1]  # Standard bill/coin denominations (sorted in descending order)
amount = 187  # Amount to be converted into change

print("Change for $", amount, ":", cashier_algorithm(amount, denominations))