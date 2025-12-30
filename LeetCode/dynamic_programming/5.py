# 5. Longest Palindromic Substring

# Given a string s, return the longest palindromic substring in s.

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        - TC: O(n^2) -> outer loop iterates from 2 to n, inner loop iteraes through valid start positons (O(n) worst case), each loop does O(1) work
        - SC: O(n^2) -> dp table is n x n
        """
        n = len(s)
        dp = [[False] * n for _ in range(n)] # dp[i][j] = True/False (is a palindrome)

        for i in range(n): # Base case -> Any single letter is a palindrome
            dp[i][i] = True
        
        max_length = 1 # max length of the longest palindrome (track for output)
        start_pos = 0 # starting pos of the longest palindrome (track for output)

        for length in range(2, n + 1):  # lengths from 2 to n (valid palindrome lengths)
            for i in range(n - length + 1): # all valid start positions
                j = i + length - 1 # string ending pos

                # check: characters match AND (inner string is palindrome OR length is 2)
                if s[i] == s[j] and (length == 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True # if we find palindrome
                    if length > max_length: # check if it's longer
                        max_length = length # update result
                        start_pos = i
                
        return s[start_pos : start_pos + max_length] # return longest palindrome
    
sol = Solution()
print(sol.longestPalindrome("babad"))
print(sol.longestPalindrome("cbbd"))
