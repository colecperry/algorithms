# 67. Add Binary

# Topics: Math, String, Bit Manipulation

# Given two binary strings a and b, return their sum as a binary string.

# Example 1:
# Input: a = "11", b = "1"
# Output: "100"

# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"

# Step 1: Initialize carry and result list
# 'carry' stores overflow from each bit addition
# 'result' stores the binary sum as a list of characters
# 'a_ptr' and 'b_ptr' are pointers to the end of each string (least significant bits)

# Step 2: While both pointers are valid (a_ptr >= 0 and b_ptr >= 0):
#   - Add corresponding bits from a and b and the carry
#   - Compute bit_sum (0 or 1) using % 2
#   - Compute new carry using // 2
#   - Insert bit_sum at the beginning of the result list
#   - Decrement both pointers to move leftward

# Step 3: Process remaining bits in 'a' (if a is longer than b)
#   - Add the bit from 'a' and the carry
#   - Compute bit_sum and update carry
#   - Insert the bit at the front of the result list
#   - Move pointer left

# Step 4: Process remaining bits in 'b' (if b is longer than a)
#   - Same as step 3, but for string 'b'

# Step 5: If there's a remaining carry after all bits are processed
#   - Insert the final carry at the front of the result list

# Step 6: Join the result list into a string and return it as the final binary sum

# -----------------------------------
# Time Complexity: O(n)
# - We process each bit of the longer string exactly once

# Space Complexity: O(n)
# - We store the resulting bits in a list of length up to max(len(a), len(b)) + 1


class Solution: # Add bits manually
    def addBinary(self, a: str, b: str) -> str:
        carry = 0 # Variable for the carry
        result = [] # Store the result string in list
        a_ptr, b_ptr = len(a) - 1, len(b) - 1 # Start ptrs at ends of strings a & b
        while a_ptr >= 0 and b_ptr >= 0:
            sum = int(a[a_ptr]) + int(b[b_ptr]) + carry # Calc the sum of each addition step
            bit_sum = sum % 2 # Convert sum to bit sum
            carry = sum // 2 # Update carry every step
            result.append(str(bit_sum)) 
            a_ptr -= 1
            b_ptr -= 1
        while a_ptr >= 0: # Leftovers if "a" string is longer
            sum = int(a[a_ptr]) + carry
            bit_sum = sum % 2
            carry = sum // 2
            result.append(str(bit_sum))
            a_ptr -= 1
        while b_ptr >= 0: # Leftovers from "b"
            sum = int(b[b_ptr]) + carry
            bit_sum = sum % 2
            carry = sum // 2
            result.append(str(bit_sum))
            b_ptr -= 1
        if carry: # If we have a final carry
            result.append(str(carry))
        return ''.join(reversed(result))

def addBinary2(a: str, b: str) -> str: 
    i, j = len(a) - 1, len(b) - 1
    carry = 0
    result = []

    # Difference is the single while loop that runs no matter what and sets digits to 0 when necessary
    while i >= 0 or j >= 0 or carry:
        digit_a = int(a[i]) if i >= 0 else 0
        digit_b = int(b[j]) if j >= 0 else 0

        total = digit_a + digit_b + carry
        bit_sum = total % 2
        result.append(str(bit_sum)) 
        carry = total // 2

        i -= 1
        j -= 1

    return ''.join(reversed(result))

sol = Solution()
print(sol.addBinary("11", "1"))
print(sol.addBinary("1010", "1011"))
"1 1" "carry"
" 1010"
" 1011"
"10101" "res"