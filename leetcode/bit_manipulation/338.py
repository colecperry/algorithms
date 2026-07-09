# 338. Counting Bits

# Dynamic Programming, Bit Manipulation

# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

# Example 1:
# Input: n = 2
# Output: [0, 1, 1]
# Explanation: 0 -> 0, 1 -> 1, 10 -> 1

# Example 2:
# Input: n = 5
# Output: [0, 1, 1, 2, 1, 2]
# Explanation: 0 -> 0, 1 -> 1, 10 -> 1, 11 -> 2, 100 -> 1, 101 -> 2


class Solution:

    def countBits_brute(self, n: int) -> list[int]:
        """
        Approach 1: Brute Force — count set bits for each number individually
        - For each i in [0..n], count its set bits using the n & (n-1) trick
        - TC: O(n * k) where k is the average number of set bits per number
        - SC: O(n) for the output array
        """
        def count_set_bits(num):
            count = 0
            while num:
                num &= num - 1  # Sub 1 from n + AND together n & n - 1 (clears lowest set bit)
                count += 1
            return count

        result = []
        for i in range(n + 1):
            result.append(count_set_bits(i))
        return result

    def countBits_shift(self, n: int) -> list[int]:
        """
        Approach 2: DP with Right Shift  ← clean and intuitive
        - Key insight: i >> 1 (right shift) is just i with its last bit removed
        - So: set_bits(i) = set_bits(i >> 1) + the last bit of i
        - We already computed set_bits(i >> 1) earlier in the array, so reuse it
        - TC: O(n) — one pass, O(1) work per element
        - SC: O(n) for the output array
        - NOTE: put bin(i) and bin(i >> 1) as WATCH variable

        Example: n = 5
          i=0: 0  >> 1 = 0  -> dp[0] + (0 & 1) = 0 + 0 = 0   (0    -> 0 set bits)
          i=1: 1  >> 1 = 0  -> dp[0] + (1 & 1) = 0 + 1 = 1   (1    -> 1 set bit)
          i=2: 10 >> 1 = 1  -> dp[1] + (2 & 1) = 1 + 0 = 1   (10   -> 1 set bit)
          i=3: 11 >> 1 = 1  -> dp[1] + (3 & 1) = 1 + 1 = 2   (11   -> 2 set bits)
          i=4: 100 >> 1 = 2 -> dp[2] + (4 & 1) = 1 + 0 = 1   (100  -> 1 set bit)
          i=5: 101 >> 1 = 2 -> dp[2] + (5 & 1) = 1 + 1 = 2   (101  -> 2 set bits)
          -> [0, 1, 1, 2, 1, 2]
        """
        dp = [0] * (n + 1) # number of 1's at i's binary represenation

        for i in range(1, n + 1):
            i_without_last_bit = i >> 1         # drop the last bit
            last_bit = i & 1                    # check if the last bit is 1 or 0
            dp[i] = dp[i_without_last_bit] + last_bit # look up answer for i without it's last bit, then just add whether the last bit was a 1 or 0

        return dp


my_solution = Solution()

# n=2 -> [0, 1, 1]
# n=5 -> [0, 1, 1, 2, 1, 2]

print(my_solution.countBits_brute(2))    # [0, 1, 1]
print(my_solution.countBits_brute(5))   # [0, 1, 1, 2, 1, 2]

print(my_solution.countBits_shift(2))   # [0, 1, 1]
print(my_solution.countBits_shift(5))   # [0, 1, 1, 2, 1, 2]
