# 415. Add Strings

# Topics: Math, String, Simulation

# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

# Example 1:
# Input: num1 = "11", num2 = "123"
# Output: "134"

# Example 2:
# Input: num1 = "456", num2 = "77"
# Output: "533"

# Example 3:
# Input: num1 = "0", num2 = "0"
# Output: "0"

#
# Strategy:
# - Use two pointers starting from the end of each string (least significant digit)
# - Initialize a carry variable to handle digit sums over 9
# - Loop while either pointer is valid or there's a carry:
#     - Convert current characters to integers using ord(char) - ord('0')
#     - Add both digits and the carry
#     - Store the last digit of the sum (sum % 10) in the output
#     - Update carry (carry = sum // 10)
# - Join the digits in reverse order to form the result string
#
# Time Complexity: O(max(n, m)), where n = len(num1), m = len(num2)
#   - Each digit from both strings is processed once
#
# Space Complexity: O(max(n, m))
#   - The output list stores one digit per processed character
#   - No additional data structures grow with input size beyond that


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        output = []  # Output array for return statement
        carry = 0  # Carry for addition
        idx_1, idx_2 = len(num1) - 1, len(num2) - 1  # Start pointers at end

        while idx_1 >= 0 or idx_2 >= 0 or carry: # if there is a carry go one more loop
            digit1 = ord(num1[idx_1]) - ord('0') if idx_1 >= 0 else 0 # if idx less than 1, digit is zero
            digit2 = ord(num2[idx_2]) - ord('0') if idx_2 >= 0 else 0

            addition = digit1 + digit2 + carry
            carry = addition // 10  # Correct carry update
            output.insert(0, str(addition % 10))  # Only insert the last digit

            idx_1 -= 1
            idx_2 -= 1

        return ''.join(output)  # Return as string, not int


sol = Solution()
print(sol.addStrings("11", "123"))
print(sol.addStrings("456", "77"))
print(sol.addStrings("0", "0"))
print(sol.addStrings("9", "9")) # test "or carry"
