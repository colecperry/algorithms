# 139. Word Break

# Example 1:
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".

# Example 2:
# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.

# Example 3:
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        For each position i, try all possible split points j:
        - Left part: s[0:j] must be segmentable (dp[j] = True)
        - Right part: s[j:i] must be a valid word (in wordDict)
                            
        - TC: O(n^2) * m
            - O(n) -> Outer loop runs "n" times (from 1 to n)
            - O(n) -> Inner loop runs an average of "n/2" times per outer iteration
            - O(m) -> String slicing `s[j:i]` creates a new substring, cost O(i-j) ≈ O(m)
            - O(m) -> Set lookup `in word_set` requires hashing the substring, cost O(m)
            - Total per check: O(m) + O(m) = O(m)
            - Overall: O(n) * O(n) * O(m) = O(n^2 * m)

        - SC: O(n + k)
            - O(n) -> DP array stores n + 1 elements
            - O(k) -> Word set stores k words where k = len(wordDict)
        """
        n = len(s)
        word_set = set(wordDict)  # O(1) lookup instead of O(n)
        
        # dp[i] = Can we segment s[0:i] using words from wordDict?
        dp = [False] * (n + 1)
        dp[0] = True  # Empty string is always segmentable
        
        # For each position i, try all possible split points j:
        for i in range(1, n + 1):
            for j in range(i):
                left_part_valid = dp[j] 
                right_part_word = s[j:i]
                
                # If left part is segmentable AND right part is a valid word
                if left_part_valid and right_part_word in word_set:
                    dp[i] = True
                    break  # Found one valid segmentation, move to next i
        
        return dp[n]  # Can we segment the entire string?


sol = Solution()
sol.wordBreak("leetcode", ["leet","code"])
sol.wordBreak("applepenapple", ["apple","pen"])
sol.wordBreak("catsandog", ["cats","dog","sand","and","cat"])

# ============================================================================
#  EXAMPLE TRACE: s = "leetcode", wordDict = ["leet", "code"]
# ============================================================================

"""
Initial Setup:
--------------
s = "leetcode"
Position:  0   1   2   3   4   5   6   7   8
String:    |   l   e   e   t   c   o   d   e

dp = [T,  F,  F,  F,  F,  F,  F,  F,  F]
      0   1   2   3   4   5   6   7   8

dp[0] = True (base case: empty string)


==================== i = 1 (trying to segment "l") ====================
Check all split points j from 0 to 0:

  j=0: Split at position 0
       Left:  s[0:0] = ""        → dp[0] = True ✓
       Right: s[0:1] = "l"       → "l" in wordDict? NO ✗
       Result: Cannot segment "l"

dp = [T,  F,  F,  F,  F,  F,  F,  F,  F]
      0   1


==================== i = 2 (trying to segment "le") ====================
Check all split points j from 0 to 1:

  j=0: Split at position 0
       Left:  s[0:0] = ""        → dp[0] = True ✓
       Right: s[0:2] = "le"      → "le" in wordDict? NO ✗
       
  j=1: Split at position 1
       Left:  s[0:1] = "l"       → dp[1] = False ✗
       (Skip because left side isn't valid)
       
dp = [T,  F,  F,  F,  F,  F,  F,  F,  F]
      0   1   2


==================== i = 3 (trying to segment "lee") ====================
Check all split points j from 0 to 2:

  j=0: Split at position 0
       Left:  s[0:0] = ""        → dp[0] = True ✓
       Right: s[0:3] = "lee"     → "lee" in wordDict? NO ✗
       
  j=1: Split at position 1
       Left:  s[0:1] = "l"       → dp[1] = False ✗ (Skip)
       
  j=2: Split at position 2
       Left:  s[0:2] = "le"      → dp[2] = False ✗ (Skip)
       
dp = [T,  F,  F,  F,  F,  F,  F,  F,  F]
      0   1   2   3


==================== i = 4 (trying to segment "leet") ====================
Check all split points j from 0 to 3:

  j=0: Split at position 0
       Left:  s[0:0] = ""        → dp[0] = True ✓
       Right: s[0:4] = "leet"    → "leet" in wordDict? YES ✓✓
       Result: dp[4] = True, BREAK!

dp = [T,  F,  F,  F,  T,  F,  F,  F,  F]
      0   1   2   3   4
                      ↑
                Found "leet"!


==================== i = 5 (trying to segment "leetc") ====================
Check all split points j from 0 to 4:

  j=0: Split at position 0
       Left:  s[0:0] = ""        → dp[0] = True ✓
       Right: s[0:5] = "leetc"   → "leetc" in wordDict? NO ✗
       
  j=1: Split at position 1
       Left:  s[0:1] = "l"       → dp[1] = False ✗ (Skip)
       
  j=2: Split at position 2
       Left:  s[0:2] = "le"      → dp[2] = False ✗ (Skip)
       
  j=3: Split at position 3
       Left:  s[0:3] = "lee"     → dp[3] = False ✗ (Skip)
       
  j=4: Split at position 4
       Left:  s[0:4] = "leet"    → dp[4] = True ✓
       Right: s[4:5] = "c"       → "c" in wordDict? NO ✗
       
dp = [T,  F,  F,  F,  T,  F,  F,  F,  F]
      0   1   2   3   4   5


==================== i = 6 (trying to segment "leetco") ====================
Check all split points j from 0 to 5:

  j=0: s[0:6] = "leetco"   → NO ✗
  j=1: dp[1] = False (Skip)
  j=2: dp[2] = False (Skip)
  j=3: dp[3] = False (Skip)
  j=4: s[4:6] = "co"       → NO ✗
  j=5: dp[5] = False (Skip)
       
dp = [T,  F,  F,  F,  T,  F,  F,  F,  F]
      0   1   2   3   4   5   6


==================== i = 7 (trying to segment "leetcod") ====================
Check all split points j from 0 to 6:

  j=0: s[0:7] = "leetcod"  → NO ✗
  j=1: dp[1] = False (Skip)
  j=2: dp[2] = False (Skip)
  j=3: dp[3] = False (Skip)
  j=4: s[4:7] = "cod"      → NO ✗
  j=5: dp[5] = False (Skip)
  j=6: dp[6] = False (Skip)
       
dp = [T,  F,  F,  F,  T,  F,  F,  F,  F]
      0   1   2   3   4   5   6   7


==================== i = 8 (trying to segment "leetcode") ====================
Check all split points j from 0 to 7:

  j=0: Split at position 0
       Left:  s[0:0] = ""        → dp[0] = True ✓
       Right: s[0:8] = "leetcode" → "leetcode" in wordDict? NO ✗
       
  j=1: Split at position 1
       Left:  s[0:1] = "l"       → dp[1] = False ✗ (Skip)
       
  j=2: Split at position 2
       Left:  s[0:2] = "le"      → dp[2] = False ✗ (Skip)
       
  j=3: Split at position 3
       Left:  s[0:3] = "lee"     → dp[3] = False ✗ (Skip)
       
  j=4: Split at position 4
       Left:  s[0:4] = "leet"    → dp[4] = True ✓
       Right: s[4:8] = "code"    → "code" in wordDict? YES ✓✓
       Result: dp[8] = True, BREAK!

dp = [T,  F,  F,  F,  T,  F,  F,  F,  T]
      0   1   2   3   4   5   6   7   8
                      ↑              ↑
                  "leet"        "leetcode"
                               (split as "leet" + "code")


FINAL ANSWER: dp[8] = True ✓
Segmentation: "leet" + "code"
"""
