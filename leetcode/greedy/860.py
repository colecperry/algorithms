# 860. Lemonade Change

# Topics: Array, Greedy

# At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

# Note that you do not have any change in hand at first.

# Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.

# Example 1:

# Input: bills = [5,5,5,10,20]
# Output: true
# Explanation: 
# From the first 3 customers, we collect three $5 bills in order.
# From the fourth customer, we collect a $10 bill and give back a $5.
# From the fifth customer, we give a $10 bill and a $5 bill.
# Since all customers got correct change, we output true.

# Example 2:
# Input: bills = [5,5,10,10,20]
# Output: false
# Explanation: 
# From the first two customers in order, we collect two $5 bills.
# For the next two customers in order, we collect a $10 bill and give back a $5 bill.
# For the last customer, we can not give the change of $15 back because we only have two $10 bills.
# Since not every customer received the correct change, the answer is false.

# How to Solve
    # Approach: Greedy algorithm - simulate the lemonade stand transaction process
    # We need to give correct change for each customer in order they arrive
    # Key insight: We only need to track $5 and $10 bills since those are used for change
    # - $5 bills: needed for change when customer pays $10 or $20
    # - $10 bills: can only be used for $20 customers (need $15 change)
    # - $20 bills: never used for change, so don't need to track them
    #
    # Change strategies:
    # - Customer pays $5: No change needed, just collect the bill
    # - Customer pays $10: Must give one $5 (only option - no choice to make)
    # - Customer pays $20: Need $15 change - THIS IS WHERE THE GREEDY CHOICE HAPPENS:
    #   Two valid options exist:
    #   1. Give one $10 + one $5 (GREEDY CHOICE - use the $10 first when possible because $5 bills are more versatile - helps for both $10 and $20 customers)
    #   2. Give three $5 bills (fallback when no $10 available)
    #
    #
    # Time Complexity: O(n) - single pass through the bills array
    # Space Complexity: O(1) - only using two integer counters regardless of input size

from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # Create variables to store our change (no need to track twenties)
        fives, tens = 0, 0
        
        # Iterate through the array
        for bill in bills:
            # If the bill is $5, store the change
            if bill == 5:
                fives += 1
            # If the bill is $10, store the change, check if we have a five to give back
            elif bill == 10:
                tens += 1
                if fives:
                    fives -= 1
                else:
                    return False  # No five available, can't make change
            # If the bill is $20, store the change, try two strategies for giving change
            elif bill == 20:
                # First try: give one ten and one five (preferred)
                if fives and tens:
                    fives -= 1
                    tens -= 1
                # Otherwise try: give three fives
                elif fives >= 3:
                    fives -= 3
                else:
                    return False

sol = Solution()
print(sol.lemonadeChange([5,5,5,10,20])) # True
print(sol.lemonadeChange([5,5,10,10,20])) # False