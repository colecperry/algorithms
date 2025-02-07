# 392. Is Subsequence

# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false

class Solution(object):
    def isSubsequence(self, s, t):
        # Create pointer at the beginning of s, and the beginning of t
        s_ptr, t_ptr = 0, 0
        # Create a while loop that continues until either pointer <= len
        while s_ptr < len(s) and t_ptr < len(t):
            # Check if characters match
            if s[s_ptr] == t[t_ptr]:
            # Increment both pointers if they match
                s_ptr += 1
                t_ptr += 1
            else: # If they do not match increment only the pointer for string t
                t_ptr += 1
        return s_ptr == len(s) # Returns true if pointer a is equal to the length of s (all chars were matched)
    
    def isSubsequence2(self, s, t):
        a = 0 # Create a pointer for the t string
        for char in t: # Loop through the t string
            if a < len(s) and char == s[a]: # If ptr's len < len(s) (a has zero based index) & match
                a += 1 # Increment pointer
        return a == len(s) # Return true if ptr == len(s) -> a increments once more before exiting loop, return false if not equal (a does not increment to find all chars)

my_solution = Solution()
print(my_solution.isSubsequence2("abc", "ahbgdc"))
print(my_solution.isSubsequence("axc", "ahbgdc"))