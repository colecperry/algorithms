# 171. Excel Sheet Column Number

# Topics: Math, String

# Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

# For example:

# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...

# Example 1:

# Input: columnTitle = "A"
# Output: 1
# Example 2:

# Input: columnTitle = "AB"
# Output: 28
# Example 3:

# Input: columnTitle = "ZY"
# Output: 701

# -------------------------------
# Notes on How to Solve:
# -------------------------------
# 1. This problem is similar to converting a string representation of a number in base-26 to a decimal 
#    number.
#    Think of Excel columns like a number system where 'A' is 1, 'B' is 2, ..., 'Z' is 26.
#    "AB" = (1 * 26^1) + (2 * 26^0) = 26 + 2 = 28
#
# 2. You process each character from left to right:
#    - For each character, convert it to a value between 1 and 26 using `ord(char) - ord('A') + 1`.
#    - Multiply the current result by 26 (shifting left in base-26), then add the current character's 
#      value.
#
# 3. This is analogous to how you convert numbers in base-10:
#    E.g., 123 = (1 * 10^2) + (2 * 10^1) + (3 * 10^0)

# -------------------------------
# Key Insights:
# -------------------------------
# - You do not need a dictionary; use `ord()` for direct conversion.
# - Excel column titles are like numbers in base-26 without a zero digit (i.e., 'A' = 1, not 0).
# - Each character's position contributes based on powers of 26, like digits in any positional number
#   system.

# -------------------------------
# Time Complexity (TC): O(n)
# -------------------------------
# - Where n = length of the input string columnTitle.
# - We process each character exactly once.

# -------------------------------
# Space Complexity (SC): O(1)
# -------------------------------
# - Only a constant amount of space is used (variables: result, value).

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0 # Initialize result to store the computed column number
        for char in columnTitle:
            value = ord(char) - ord('A') + 1 # Convert char into it's ASCII number
            result = result * 26  # Shift current result to the left in base-26
            result += value # Add value of the current character
        return result
    
sol = Solution()
print(sol.titleToNumber("A"))
print(sol.titleToNumber("AB"))
print(sol.titleToNumber("ZY"))



