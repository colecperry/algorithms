# Knapsack problem: given an array consisting of n objects, where each object has a weight and a value, and a knapsack with a capacity, select the subset of items to put in the knapsack to maximize the total value of the knapsack without exceeding the weight limit. The knapsack problem can be: 
    # 0-1 Knapsack: Each item can either be fully included or excluded (we cannot take a fraction of an item)
    # Fractional Knapsack: We can take fractions of items -> Greedy

# How to Solve: (Code)
    # DP Table: Create a 2D array (matrix) to store the maximum value acheivable for different knapsack capacities and subsets of items. The rows typically represent the items, and the columns represent the knapsack capacities
    # Fill up the table: In the bottom up approach, the table is filled iteratively starting from the smallest subproblems (smaller capacities and fewer items). For each item and capacity, the algorithm considers two options:
        # Include the item: If the item's weight is less than or equal to the current capacity, check if including the item leads to a higher value than excluding it
        # Exclude the item: Consider the value obtained without including the current item
        # If the item can't fit at the current weight capacity, the best value we can get with the first "i" items is the same as the best value we could get with the first "i - 1" items, at the same capacity. So in other words, we skip the item entirely and we inherit the best answer we had at that capacity without it
    # Final solution: The max value that can be achieved with the given items and knapsack capacity is found in the bottom right cell of the DP table

# Bottom Up 0/1 Knapsack Problem
def knapsack(weights, values, W, n):
    # Create a 2D dp array where dp[i][w] represents the maximum value for the first i items with weight limit w -> row = # of items used, column = a knapsack with capacity w
    dp = [[0] * (W + 1) for _ in range(n + 1)] # Init matrix to zero

    # Fill dp table bottom up (row and column 0 = base case)
    for i in range(1, n + 1): # Loop thru # of items we're considering -> weight and val 
        for w in range(1, W + 1): # Loop thru weight capacities
            if weights[i-1] <= w: # check if item can fit into knapsack capacity at weight w
                exclude = dp[i - 1][w] # Value if we exlude the item
                remaining_capacity = w - weights[i - 1] # Remaining space after including current item
                include = values[i - 1] + dp[i - 1][remaining_capacity] # Value if we include current item (value plus best value for remaining capcaity)
                dp[i][w] = max(exclude, include) # Choose the better of the two
            else:
                # If the item can't be included, just carry forward the value from above
                dp[i][w] = dp[i-1][w]

    # The value in dp[n][W] will be the maximum value that can be obtained
    return dp[n][W]

# Example usage:
weights = [2, 3, 4, 5]   # Weights of the items
values = [3, 4, 5, 6]    # Values of the items
W = 5                    # Capacity of the knapsack
n = len(weights)         # Number of items

max_value = knapsack(weights, values, W, n)
print(f"Maximum value that can be obtained: {max_value}")


# Bottom Up 0/1 Knapsack Problem with Traceback
def knapsack(weights, values, W, n):
    # Initialize dp table where dp[i][w] will be the max value achievable with the first i items and weight w
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    # To track whether an item is included or not
    item_selected = [[False] * (W + 1) for _ in range(n + 1)]

    # Build the dp table in a bottom-up manner
    for i in range(1, n + 1): # number of items considered
        for w in range(1, W + 1): # diff weights considered
            if weights[i-1] <= w: # If cur item fits at weight "w"
                # if it fits, take val of cur item + best leftover
                include_item = values[i-1] + dp[i-1][w - weights[i-1]]
                # If we do not include the current item
                exclude_item = dp[i-1][w]

                # Take the maximum of including or excluding the item
                if include_item > exclude_item:
                    dp[i][w] = include_item # Set dp val
                    item_selected[i][w] = True  # Mark this item as selected -> we took the item
                else:
                    dp[i][w] = exclude_item # Set dp val
            else:
                dp[i][w] = dp[i-1][w]  # If the item can't be included, carry forward the value

    # The maximum value is at dp[n][W]
    max_value = dp[n][W]

    # Traceback to find which items were selected
    selected_items = [] # Store selected indexes
    w = W # Track remaining capacity as we move backwards
    for i in range(n, 0, -1): # Loop backwards through items "i"
        if item_selected[i][w]:
            selected_items.append(i-1)  # Store the index of the selected item (0-indexed)
            w -= weights[i-1]  # Reduce the remaining capacity of the knapsack after taking item

    selected_items.reverse()  # To get the selected items in the original order

    return max_value, selected_items

    # Traceback to find which items were selected to achieve the max value
    # We start from the bottom-right corner of the item_selected table: item_selected[n][W]
    # and move backward (i from n to 1) to check which items were included

    # Step-by-step example with W = 5 and n = 4:
    # i = 4, w = 5 → item_selected[4][5] = False → item 3 was not selected
    # i = 3, w = 5 → item_selected[3][5] = False → item 2 was not selected
    # i = 2, w = 5 → item_selected[2][5] = True  → item 1 was selected
    #       → append i-1 = 1 to selected_items (since weights/values are 0-indexed)
    #       → update w = 5 - weights[1] = 2
    # i = 1, w = 2 → item_selected[1][2] = True  → item 0 was selected
    #       → append i-1 = 0 to selected_items
    #       → update w = 2 - weights[0] = 0
    # Done! We stop since w == 0 (no more weight capacity left)

    # Reminder:
    # We append i - 1 because item i in the dp/item_selected table refers to weights[i-1]
    # This is due to using 1-based indexing in the dp table but 0-based indexing in the weights/values arrays


# Example usage:
weights = [2, 3, 4, 5]   # Weights of the items
values = [3, 4, 5, 6]    # Values of the items
W = 5                    # Capacity of the knapsack
n = len(weights)         # Number of items

max_value, selected_items = knapsack(weights, values, W, n)
print(f"Maximum value that can be obtained: {max_value}")
print(f"Items selected (0-indexed): {selected_items}")