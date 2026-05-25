# 125. Valid Palindrome

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1: Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2: Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3: Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

class Solution(object):
    """
    - TC: O(n)
    - SC: O(1)
    """
    def isPalindrome(self, s): # 0(1) space
        l, r = 0, len(s) - 1 # Create left and right pointers
        while l < r:
            # Skip non-alphanumeric characters
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            # Compare characters (case-insensitive)
            elif s[l].lower() != s[r].lower():
                return False
            else: # If they are equal move pointers
                l += 1
                r -= 1
        return True # if l meets r all chars were equal


solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))