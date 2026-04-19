# 371. Sum of Two Integers

# Given two integers a and b, return the sum of the two integers without using the operators + and -.

# Example 1:
# Input: a = 1, b = 2
# Output: 3

# Example 2:
# Input: a = 2, b = 3
# Output: 5


class Solution(object):
    def getSum(self, a, b):
        """
        Approach: XOR + AND carry
        - XOR adds bits without carry  (1 ^ 1 = 0, carry handled separately)
        - AND finds carry bits         (1 & 1 = 1, only 1+1 produces a carry)
        - Shift carry left by 1        (carry affects the NEXT bit position)
        - Repeat until no carry remains
        - TC: O(1) — at most 32 iterations
        - SC: O(1)

        Example: a = 2 (010), b = 3 (011)
        step 1: carry = (010 & 011) = 010, 010 << 1 = 100  (carry first)
                a = 010 ^ 011 = 001             (then XOR)
                b = 100                         (carry becomes new b)
        step 2: carry = (001 & 100) = 000, 000 << 1 = 000  (no carry)
                a = 001 ^ 100 = 101             (then XOR)
                b = 000                         (carry becomes new b)
        b is 0, exit loop, return 101 = 5  ✓
        """
        while b:
            carry = (a & b) << 1  # find carry bits, shift left to next position
            a = a ^ b             # add bits without carry
            b = carry             # repeat with carry as new b

        return a


sol = Solution()
print(sol.getSum(1, 2))   # 3
print(sol.getSum(2, 3))   # 5