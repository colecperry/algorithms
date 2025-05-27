# 680. Valid Palindrome II

# Topics: Two Pointers, String, Greedy

# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

# Example 1:
# Input: s = "aba"
# Output: true

# Example 2:
# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.

# Example 3:
# Input: s = "abc"
# Output: false

# How to Solve: 
    # Start by initializing two pointers at the beginning and end of the string
    # Use a loop to compare characters at both ends, moving inward
    # If all characters match, the string is already a palindrome, return True
    # If a mismatch is found:
        # Try skipping the character at the left pointer and check if the rest is a palindrome
        # If not, try skipping the character at the right pointer and check again
        # If either case results in a valid palindrome, return True
        # If no mismatches are found through the loop, return True by default

    # Time Complexity: O(n)
    # - In the worst case, we traverse the string once and possibly make one additional traversal of a substring

    # Space Complexity: O(1)
    # - No extra space is used beyond a few pointers; checks are done in-place


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(left, right): # Checking palindrome after skipping
            while left < right: 
                if s[left] != s[right]: # Return False if chars !=
                    return False
                left += 1
                right -= 1
            return True

        left, right = 0, len(s) - 1 # Init "l" and "r" pointers 

        while left < right: 
            if s[left] != s[right]: # If char's are not ==
                # Try skipping either the left or the right character
                return is_palindrome(left + 1, right) or is_palindrome(left, right - 1) # Return true if either are a palindrome after skipping from each side
            left += 1
            right -= 1

        return True # Return true if all chars are equal


sol = Solution()
print(sol.validPalindrome("aba"))
print(sol.validPalindrome("abca"))
print(sol.validPalindrome("abc"))