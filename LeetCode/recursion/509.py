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

class Solution: # without DP 
    """
    TC: O(2^n) - each call branches into two calls (doubles in size at each level)
    SC: O(n) - each recursive call adds one frame to the call stack -> fib(5) calls fib(4), ...
    """
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)
    
class Solution2: # with top down DP
    """
    TC: O(n) - each subproblem (O to n) computed once
    SC: O(n) - memo stores n values + recursion stack depth
    """
    memo = {}
    def fib2(self, n: int) -> int:
        if n == 0: # Base Cases
            return 0
        if n == 1:
            return 1
        
        if n in self.memo: # Check cache for already computed results
            return self.memo[n]
        
        # Recursive calls & memo assignment
        self.memo[n] = self.fib2(n - 1) + self.fib2(n - 2) 

        return self.memo[n]
    
class Solution3: # with bottom up DP
    """
    TC: O(n) - single pass from 2 to n, each iteration O(1)
    SC: O(n) - dp array stores n+1 values
    """
    def fib(self, n: int) -> int:       
        # Edge cases: base cases for fib sequence
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        # dp[i] = ith fibonacci number's value
        dp = [0] * (n + 1)
        dp[1] = 1
        
        # Build up from smallest subproblems: fib(i) = fib(i-1) + fib(i-2)
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]


sol = Solution()
print(sol.fib(2)) # F(2) = F(1) + F(0) = 1 + 0 = 1.
print(sol.fib(3)) # F(3) = F(2) + F(1) = 1 + 1 = 2.
print(sol.fib(4)) # F(4) = F(3) + F(2) = 2 + 1 = 3.