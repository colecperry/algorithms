# 91. Decode Ways

# You have intercepted a secret message encoded as a string of numbers. The message is decoded via the following mapping:

# "1" -> 'A'
# "2" -> 'B'
# ...
# "25" -> 'Y'
# "26" -> 'Z'

# However, while decoding the message, you realize that there are many different ways you can decode the message because some codes are contained in other codes ("2" and "5" vs "25").

# For example, "11106" can be decoded into:

# "AAJF" with the grouping (1, 1, 10, 6)
# "KJF" with the grouping (11, 10, 6)
# The grouping (1, 11, 06) is invalid because "06" is not a valid code (only "6" is valid).
# Note: there may be strings that are impossible to decode.

# Given a string s containing only digits, return the number of ways to decode it. If the entire string cannot be decoded in any valid way, return 0.

# The test cases are generated so that the answer fits in a 32-bit integer.

# Example 1:
# Input: s = "12"
# Output: 2
# Explanation:
# "12" could be decoded as "AB" (1 2) or "L" (12).

# Example 2:
# Input: s = "226"
# Output: 3
# Explanation:
# "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

# Example 3:
# Input: s = "06"
# Output: 0
# Explanation:
# "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06"). In this case, the string is not a valid encoding, so return 0.

class Solution:
    def numDecodings(self, s: str) -> int:
        """
        TC: O(n)
            - Single loop through n characters
            - Each iteration: O(1) operations

        SC: O(n)
            - DP array: n + 1 elements
            - Can optimize to O(1) by keeping only last 2 values
        """
        n = len(s)
        dp = [0] * (n + 1) # dp[i] = number of ways I can decode the string up to "i"
        dp[0] = 1 

        for i in range(1, n + 1):
            # One digit condition -> cannot decode zero
            if s[i-1] != '0':  # Single digit must not be '0'
                dp[i] += dp[i-1]
            # Two digit condition -> valid range 10-26
            if i >= 2:  # Make sure we have at least 2 digits
                two_digit = int(s[i-2:i]) # get last two digits
                if 10 <= two_digit <= 26:  # Valid two-digit decode
                    dp[i] += dp[i-2]

        return dp[n]


sol = Solution()
print(sol.numDecodings("12")) # "AB", "L"
print(sol.numDecodings("226")) # "BZ", "VF", "BBF"
print(sol.numDecodings("06")) # 0

# ============================================================================
#                    EXAMPLE TRACE: s = "226"
# ============================================================================

"""
Setup:
------
s = "12"
Position:  0   1   2
String:    |   1   2

Decoding reference:
'A'=1, 'B'=2, ..., 'L'=12, ..., 'Z'=26

dp = [1,  0,  0]
      0   1   2

dp[0] = 1 (base case: empty string has 1 way to decode it - do nothing)


==================== i = 1 (decoding "1") ====================
Current character: s[0] = '1'

Option 1: Decode '1' as a single digit
  - Is '1' != '0'? YES ✓
  - Can decode '1' as 'A'
  - How many ways exist at position 0 (before '1')? dp[0] = 1
  - Extend those ways by adding 'A'
  - dp[1] += dp[0] = 0 + 1 = 1

Option 2: Decode two digits together
  - i >= 2? NO (only have 1 character so far)
  - Skip this option

Result: dp[1] = 1
Ways to decode "1": ["A"]

dp = [1,  1,  0]
      0   1   2


==================== i = 2 (decoding "12") ====================
Current character: s[1] = '2'

Option 1: Decode '2' as a single digit
  - Is '2' != '0'? YES ✓
  - Can decode '2' as 'B'
  - How many ways exist at position 1 (before '2')? dp[1] = 1
  - Extend those ways by adding 'B'
  - dp[2] += dp[1] = 0 + 1 = 1
  - This takes the 1 way to decode "1" (which was "A") and adds 'B' → "AB"

Option 2: Decode '12' as two digits together
  - i >= 2? YES ✓
  - two_digit = int(s[0:2]) = int("12") = 12
  - Is 10 <= 12 <= 26? YES ✓
  - Can decode '12' as 'L'
  - How many ways exist at position 0 (before '12')? dp[0] = 1
  - Extend those ways by adding 'L'
  - dp[2] += dp[0] = 1 + 1 = 2
  - This takes the 1 way to decode "" (empty) and adds 'L' → "L"

Result: dp[2] = 2
Ways to decode "12": ["AB", "L"]
  - "AB": Extended from dp[1] = 1 way ("A") by adding 'B'
  - "L": Extended from dp[0] = 1 way (empty) by adding 'L'

dp = [1,  1,  2]
      0   1   2


==================== Key Insight ====================
We don't add "+1" to dp[i].
We add "how many ways existed at the earlier position" to dp[i].

- If decoding 1 digit: add dp[i-1] (ways from 1 position back)
- If decoding 2 digits: add dp[i-2] (ways from 2 positions back)

This is because we're EXTENDING all the previous valid decodings
by adding our new digit(s) to them.
"""