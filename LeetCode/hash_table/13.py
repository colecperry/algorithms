# 13. Roman to Integer

# Topics: Hash Table, Math, String

# Instructions
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II. Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
# - I can be placed before V(5) and X(10) to make 4 and 9
# - X can be placed before L (50) and C (100) to make 40 and 90. 
# - C can be placed before D (500) and M (1000) to make 400 and 900.
# - Given a roman numeral, convert it to an integer.

# How to solve:
# Larger value comes before smaller value: Add the two values
# Smaller value comes before larger value: Subtract the smaller value from the larger


class Solution:
    def romanToInt(self, s):
        """
        Converts a Roman numeral string to an integer.
        """

        # Step 1: Define a dictionary mapping Roman numerals to their integer values
        roman = {
            "I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000
        }

        # Step 2: Initialize the result variable
        result = 0

        # Step 3: Iterate through the string
        for i in range(len(s)):
            # If the current numeral is smaller than the next numeral, subtract it
            if i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:
                result -= roman[s[i]]
            else:
                result += roman[s[i]]

        return result

# Example Usage
solution = Solution()
print(solution.romanToInt("MCMXCIV"))  # Output: 1994
print(solution.romanToInt("XIV"))      # Output: 14