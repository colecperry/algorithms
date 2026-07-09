# 131. Palindrome Partitioning

# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

# Example 1:
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]

# Example 2:
# Input: s = "a"
# Output: [["a"]]

from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        
        def is_palindrome(string):
            return string == string[::-1]
        
        def backtrack(i, path): # i = current index in string, # path = palindromes collected so far
            
            # Base case: reached end of string, found valid partition
            if i == len(s):
                result.append(path[:])
                return
            
            # Try all possible substrings starting at index i
            # j represents where we cut: s[i:j]
            for j in range(i + 1, len(s) + 1):
                substring = s[i:j]
                
                # Only proceed if it's a palindrome
                if is_palindrome(substring):
                    path.append(substring)   # Choose
                    backtrack(j, path)       # Explore from j (where we just cut)
                    path.pop()               # Undo
        
        backtrack(0, []) # start at index 0, empty path
        return result

sol = Solution()
print(sol.partition("aab")) # [["a","a","b"],["aa","b"]]
print(sol.partition("a")) # [["a"]]

# ============================ DECISION TREE FOR "aab" ============================
#
#                                    backtrack(i=0, [])
#                                       s = "a a b"
#                                            ↑
#                                            i=0
#                                             |
#                 ---------------------------------------------------------
#                 |                           |                           |
#            j=1: s[0:1]                 j=2: s[0:2]                 j=3: s[0:3]
#              "a" ✓                       "aa" ✓                      "aab" ✗
#                 |                           |                        PRUNED
#                 |                           |
#         backtrack(i=1, ["a"])       backtrack(i=2, ["aa"])
#            s = "a a b"                 s = "a a b"
#                 ↑                               ↑
#                 i=1                             i=2
#                 |                               |
#        -------------------                 j=3: s[2:3]
#        |                 |                   "b" ✓
#   j=2: s[1:2]       j=3: s[1:3]                 |
#     "a" ✓             "ab" ✗                    |
#        |              PRUNED           backtrack(i=3, ["aa","b"])
#        |                                        |
# backtrack(i=2, ["a","a"])                 i == len(s)
#    s = "a a b"                          ✅ FOUND: ["aa","b"]
#             ↑
#            i=2
#             |
#        j=3: s[2:3]
#          "b" ✓
#             |
#  backtrack(i=3, ["a","a","b"])
#             |
#        i == len(s)
#   ✅ FOUND: ["a","a","b"]
#