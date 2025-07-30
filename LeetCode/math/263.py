# 263. Ugly Number

# Topics: Math

# An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5.

# Given an integer n, return true if n is an ugly number.

# Example 1:
# Input: n = 6
# Output: true
# Explanation: 6 = 2 × 3

# Example 2:
# Input: n = 1
# Output: true
# Explanation: 1 has no prime factors.

# Example 3:
# Input: n = 14
# Output: false
# Explanation: 14 is not ugly since it includes the prime factor 7.

# How to Solve
# An ugly number is a positive number whose only prime factors are 2, 3, or 5. If a number has no other prime factors, then:
    # Every piece of that number can eventually be factored out using only 2s, 3s, or 5s.
    # Once all the 2s, 3s, and 5s are divided out, the number becomes 1.

# Step 1: Check if the number is positive. If it's zero or negative, it's not ugly.

# Step 2: Use a loop to divide the number by 2, 3, and 5 as many times as possible. This removes all allowed prime factors from the number.

# Step 3: After removing all 2s, 3s, and 5s, check what's left of the number. If the result is 1, then all its prime factors were 2, 3, or 5 — so it's ugly. If the result is not 1, then it has some other prime factor (like 7 or 11), so it's not ugly.

# Time Complexity: O(log n)
# Because each division reduces the number, and we perform at most log n
# divisions.

# Space Complexity: O(1)
# We use a constant amount of memory regardless of the size of the input.


class Solution: # Ugly numbers are positive numbers whose only prime factors are 2, 3, or 5.
    def isUgly(self, n: int) -> bool:
        if n <= 0: # Negative numbers and 0 are not considered ugly
            return False
        for factor in [2, 3, 5]: # Loop through each allowed prime factor
            while n % factor == 0: # Keep dividing n by the factor as long as it is divisible
                n = n / factor # Divide n by the factor
        return n == 1 # If the result is 1, then all prime factors were only 2, 3, or 5


sol = Solution()
print(sol.isUgly(6)) # True
print(sol.isUgly(1)) # True
print(sol.isUgly(14)) # False