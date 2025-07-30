# 258. Add Digits

# Topics: Math, Simulation, Number Theory

# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

# Example 1:
# Input: num = 38
# Output: 2
# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2 
# Since 2 has only one digit, return it.

# Example 2:
# Input: num = 0
# Output: 0

# How to Solve:
    # Step 1: Keep looping while num is more than one digit (i.e., num >= 10)
    # Step 2: Convert num to string and iterate over its characters (digits)
    # Step 3: Sum the digits and assign the result back to num
    # Step 4: Repeat until num becomes a single digit
    # Step 5: Return num

# TC - Worst-case time is O(log n) because each iteration reduces the number closer to a single-digit number. For example, a 3-digit number (999) becomes 27 → 9 in two steps.

# SC - O(1) constant space. We only store a few integer variables and use string conversion temporarily, which doesn't depend on the input size in a significant way.

class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:  # Loop til num becomes a single digit
            added_digits = 0 # Track the added digits of the num and reset each loop
            for n in str(num):
                added_digits += int(n) # Add the digits
            num = added_digits  # Update num to the added digits for the next loop
        return num  # Once num is a single digit, return it


sol = Solution()
print(sol.addDigits(38))
print(sol.addDigits(0))