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

    # Time Complexity: O(n)
    # - In the worst case, we traverse the string once and possibly make one additional traversal of a substring

class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        - TC: O(n) for outer two pointer loop, then O(n) + O(n) check if mismatch found from inner loop
        - SC: No extra space is used beyond a few pointers; checks are done in-place
        """
        def is_palindrome(left, right): # Bool -> check if passed in str is palindrome 
            while left < right: 
                if s[left] != s[right]: # Return False if chars !=
                    return False
                left += 1
                right -= 1
            return True

        left, right = 0, len(s) - 1 # Init "l" and "r" pointers 

        while left < right: 
            if s[left] != s[right]: # If char's are not == try deleting both chars
                return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)
            left += 1
            right -= 1

        return True # Return true if all chars are equal

sol = Solution()
print(sol.validPalindrome("aba"))
print(sol.validPalindrome("abca"))
print(sol.validPalindrome("abc"))