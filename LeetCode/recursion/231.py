# 231. Power of Two

# Topics: Math, Bit Manipulation, Recursion

# Given an integer n, return true if it is a power of two. Otherwise, return false.

# An integer n is a power of two, if there exists an integer x such that n == 2x.

# Example 1:

# Input: n = 1
# Output: true
# Explanation: 2^0 = 1

# Example 2:
# Input: n = 16
# Output: true
# Explanation: 2^4 = 16

# Example 3:
# Input: n = 3
# Output: false

# How to Solve:
    # Base Cases:
        # 1: n <= 0 -> False, powers of two are always positive
        # 2: n = 1 -> True, 2^0 = 1
        # 3: n is odd -> False, odd numbers cannot be powers of two
        # n is even -> cannot answer immediately

    # What do we need to know? (Recursive Step)
        # Need to return a Boolean

    # How do I combine the answers?
        # No combining, just return what the helper tells us

    # Time Complexity: O(log n) -> we divide n by 2 each recursive call until we reach 1 or an invalid case

    # Space Complexity: O(log n) -> Each recursive call adds a new frame to the call stack

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Base case 1 -> boundary
        if n <= 0:
            return False
        
        # Base case 2 -> trivial answer
        if n == 1:
            return True
    
        # Base case 3 -> odd number
        if n % 2 != 0:
            return False

        # Recursive case: check if n/2 is a power of 2
        return self.isPowerOfTwo(n // 2)

sol = Solution()
print(sol.isPowerOfTwo(1)) # 2^0 = 1, True
print(sol.isPowerOfTwo(16)) # 2^4 = 16, True
print(sol.isPowerOfTwo(3)) # 2^? = 3, False