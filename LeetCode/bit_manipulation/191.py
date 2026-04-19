# 191. Number of 1 Bits

# Divide and Conquer, Bit Manipulation

# Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).

# Example 1:
# Input: n = 11
# Output: 3
# Explanation: 11 in binary is 1011, which has 3 set bits.

# Example 2:
# Input: n = 128
# Output: 1
# Explanation: 128 in binary is 10000000, which has 1 set bit.

# Example 3:
# Input: n = 2147483645
# Output: 30
# Explanation: 2147483645 in binary is 1111111111111111111111111111101, which has 30 set bits.


class Solution:

    def hammingWeight_shift(self, n: int) -> int:
        """
        Approach 1: Shift and Check
        - Check the least significant bit (LSB) each iteration, then shift right
        - TC: O(32) = O(1) — always loops exactly 32 times regardless of input
        - SC: O(1)
        - NOTE: integers are stored as 32 bits, so 1011 in binary is really 00000000000000000000000000001011, type bin(n) in the watch panel in the debugger to follow
        """
        count = 0 # count number of set bits (1's)

        for _ in range(32): # loop starts at the right most bit
            count += n & 1  # Check if LSB is set (1 & 1 = 1, 0 & 1 = 0)
            n >>= 1         # Shift whole binary number to the right & check the next bit

        return count
    

    def hammingWeight_trick(self, n: int) -> int:
        """
        Approach 2: n & (n - 1) Trick  ← preferred interview answer
        - n - 1 flips the lowest set bit (1) to 0, and any 0 bits below it to 1
        - ANDing n with n-1 clears the lowest set bit (1) and wipes out the noise below it
        - Loop until no set bits remain, res will equal # of set bits cleared
        - TC: O(k) where k is the number of set bits — faster in practice than approach 1
        - SC: O(1)

        Example: n = 1011 (11)
          1011 - 1 = 1010  ->  1011 & 1010 = 1010  (cleared lowest set bit)
          1010 - 1 = 1001  ->  1010 & 1001 = 1000  (cleared lowest set bit)
          1000 - 1 = 0111  ->  1000 & 0111 = 0000  (cleared lowest set bit)
          -> 3 iterations, 3 set bits

        NOTE: Logic for AND operation, type bin(n) in the watch panel in the debugger to follow

        1011
        1010
        ────
        1010

        """
        count = 0

        while n:
            n &= n - 1  # Subtract 1 from n + AND together n & n - 1 (clears lowest set bit)
            count += 1  # Each cleared bit was a set bit

        return count


my_solution = Solution()

# 11  -> 1011    -> 3 set bits
# 128 -> 10000000 -> 1 set bit
# 2147483645 -> 1111111111111111111111111111101 -> 30 set bits

print(my_solution.hammingWeight_shift(11))           # 3
print(my_solution.hammingWeight_shift(128))          # 1
print(my_solution.hammingWeight_shift(2147483645))   # 30

print(my_solution.hammingWeight_trick(11))           # 3
print(my_solution.hammingWeight_trick(128))          # 1
print(my_solution.hammingWeight_trick(2147483645))   # 30