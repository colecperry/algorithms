# 326. Power of Three

# Topics: Math, Recursion

# Given an integer n, return true if it is a power of three. Otherwise, return false.

# An integer n is a power of three, if there exists an integer x such that n == 3x.

# Example 1:
# Input: n = 27
# Output: true
# Explanation: 27 = 3^3

# Example 2:
# Input: n = 0
# Output: false
# Explanation: There is no x where 3^x = 0.

# Example 3:
# Input: n = -1
# Output: false
# Explanation: There is no x where 3^x = (-1).

# How to Solve (Recursive)
    # Base Cases
        # 1. n <= 0 -> False
            # No power of three can ever be 0 or negative
            # 3^k is never 0 or a negative number
        # 2. n == 1 -> True
            # 3^0 = 1, this is the smallest valid power of three
        # 3. n % 3 != 0 -> False
            # If n isn't divisible by three, it will never reach 1 by repeated division
    # Recusive Case
        # If n is divisible by 3 and greater than 1, then n might be a power of 3.
        # Eventually, one of two things will happen:
            # The number reduces all the way down to 1 → ✅ we return True.
            # At some point, n is no longer divisible by 3 → ❌ we return False. (ex. 6)

    # Time Complexity:
    #   - Worst case: O(log_3 n), since we divide n by 3 each recursive step 
    #     until we reach 1 (at most ~19 steps for 32-bit integers).
    #   - Best case: O(1), if n <= 0 or n % 3 != 0 right away.
    #   - Average case: O(log_3 n), but many numbers exit early if not divisible by 3.
    #
    # Space Complexity:
    #   - O(log_3 n), due to recursion depth (one stack frame per recursive call).
    #   - In practice ≤ ~19 frames for 32-bit inputs.

class Solution:
    def isPowerOfThreeRecursive(self, n: int) -> bool: # Recursive
        # Base cases
        if n <= 0: # nothing can solve 3^? = 0 or negative num
            return False
        if n == 1: # 3^0 = 1
            return True
        if n == 3: # 3^1 = 3
            return True

        return self.isPowerOfThree(n//3) # keep dividing, will end up as 3 -> use integer division to avoid floats
    

    
    def isPowerOfThreeIterative(self, n: int) -> bool:
        if n <= 0: # Power of three cannot be 0 or negative
            return False
        while n % 3 == 0: # If n is divisible by three,
            n //= 3 # Continue to divide by three until you can't
        return n == 1 # If n is a power of three, it will be 1 after continual dividing
    
sol = Solution()
print(sol.isPowerOfThree(27))
print(sol.isPowerOfThree(0))
print(sol.isPowerOfThree(-1))