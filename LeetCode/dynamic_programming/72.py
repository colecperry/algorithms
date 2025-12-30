# 72. Edit Distance

# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

# You have the following three operations permitted on a word:

# Insert a character
# Delete a character
# Replace a character

# Example 1:
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')

# Example 2:
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        TC: O(m*n) -> each loop iterates m and n times, O(1) work done per iteration
        SC: O(m*n) -> DP array of m * n
        """
        n = len(word1)
        m = len(word2)

        # dp[i][j] = min number of operations to convert first "i" chars of word1 into first "j" chars of word2
        dp = [[0] * (m + 1) for _ in range(n + 1)] # n rows, m cols

        # Base Cases
        for i in range(n + 1): # Converting first "i" chars of word1 into an empty str
            dp[i][0] = i       # Need "i" deletions
        
        for j in range(m + 1): # Converting an empty string into first "j" chars of word2
            dp[0][j] = j       # Need "j" insertions

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i-1] == word2[j-1]: # Chars match -> no operation needed
                    dp[i][j] = dp[i-1][j-1] # Cost from converting shorter strings
                else: # Chars don't match -> consider 3 operations
                    # Replace: solved dp[i-1][j-1], now replace word1[i-1] with word2[j-1]
                    cost1 = dp[i-1][j-1] + 1
                    
                    # Delete: Delete word1[i-1], solved dp[i-1][j]
                    cost2 = dp[i-1][j] + 1
                    
                    # Insert: solved dp[i][j-1], now insert word2[j-1]
                    cost3 = dp[i][j-1] + 1
                    
                    dp[i][j] = min(cost1, cost2, cost3) # take min of 3 operations

        return dp[n][m] # Return min cost of converting whole words

# Example: word1 = "horse", word2 = "ros", i = 1, j = 1

# REPLACE: Look up cost to convert shorter word1 to shorter word2, then replace the last char
    # - dp[0][0]: converting word1="" to word2="" costs 0
    # - Replace 'h' in word1 with 'r' from word2 (cost = +1)
    # - Total: dp[i-1][j-1] + 1 = dp[0][0] + 1 = 0 + 1 = 1

# DELETE: Delete char from word1, then look up cost to convert remaining word1 to word2
    # - Delete 'h' from word1: word1 "h" → "" (cost = +1)
    # - dp[0][1]: converting word1="" to word2="r" costs 1
    # - Total: dp[i-1][j] + 1 = dp[0][1] + 1 = 1 + 1 = 2

# INSERT: Look up cost to convert word1 to shorter word2, then insert the missing char
    # - dp[1][0]: converting word1="h" to word2="" costs 1 (delete 'h')
    # - Insert 'r' to extend our target from "" to "r" (cost = +1)
    # - Total: dp[i][j-1] + 1 = dp[1][0] + 1 = 1 + 1 = 2

sol = Solution()
print(sol.minDistance("horse", "ros"))
print(sol.minDistance("intention", "execution"))