# 1143 - Longest Common Subsequence

# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

# Example 1:
# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.

# Example 2:
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.

# Example 3:
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.

class LongestCommonSubsequence:
    """  
    TC:
        - O(m*n) -> we use nested loops to fill out the DP table which run once for every (i,j) pair. There are "m" possible "i" values and "n" possible "j" values.
    SC: O(m*n)
        - The dp table has (m + 1) x (n + 1) entries.
    """
    def longestCommonSubsequence(self, text1, text2):
        m, n = len(text1), len(text2)
        
        # Matrix DP table stores LCS from only the first "i" chars of text1 and first "j" chars of text2
        # dp[i][j] = LCS length for text1[0:i] and text2[0:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Base cases already initialized for empty str -> dp[0][j] = 0 for all j, dp[i][0] = 0 for all i
        
        # Fill DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    # Characters match, add 1 to whatever LCS we had without both these chars
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    # Characters don't match, take best from excluding either char
                    dp[i][j] = max(
                        dp[i-1][j],   # Exclude char from text1
                        dp[i][j-1]    # Exclude char from text2
                    )
        
        return dp[m][n]

sol = LongestCommonSubsequence()
print(sol.longestCommonSubsequence("abcde", "ace"))  # 3
print(sol.longestCommonSubsequence("abc", "abc"))    # 3
print(sol.longestCommonSubsequence("abc", "def"))    # 0