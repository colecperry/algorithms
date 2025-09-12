# 509. Fibonacci Number

# Topics: Math, Dynamic Programming, Recursion, Memoization

# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).

# Example 1:

# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

# Example 2:
# Input: n = 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

# Example 3:
# Input: n = 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

# How to Solve (Recursively):
    # Base Cases:
        # If n == 0 -> return 0 because the problem gives this to us
        # If n == 1 -> return 1 because the problem gives this to us

    # What do we need to know?
        # The fibonaaci value for each recursive call F(n-1), F(n-2)

    # How do you combine these to get the answer?
        # Simple addition -> F(n) = F(n - 1) + F(n - 2)

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)

sol = Solution()
print(sol.fib(2)) # F(2) = F(1) + F(0) = 1 + 0 = 1.
print(sol.fib(3)) # F(3) = F(2) + F(1) = 1 + 1 = 2.
print(sol.fib(4)) # F(4) = F(3) + F(2) = 2 + 1 = 3.