# 266. Palindrome Permutation

# Topics: Hash Table, String, Bit Manipulation

# Given a string s, return true if a permutation of the string could form a palindrome and false otherwise.

# Example 1:

# Input: s = "code"
# Output: false
# Example 2:

# Input: s = "aab"
# Output: true
# Example 3:

# Input: s = "carerac"
# Output: true

# How to Solve:
    # Key Insight:
    # ------------------------------
    # - A string can be rearranged into a palindrome if at most **one character** has an odd count.
    # - This is because in a palindrome:
    #     - For **even-length** palindromes: all characters must have even counts (perfect mirror).
    #     - For **odd-length** palindromes: exactly one character can have an odd count (middle 
    #       character), all others must be even.
    # - So, regardless of string length, **at most one odd-count character is allowed**.

    # Steps to Solve:
    # ------------------------------
    # 1. Count the frequency of each character using collections.Counter.
    # 2. Iterate through the character counts:
    #     - Keep track of how many characters have odd frequencies.
    # 3. If more than one character has an odd frequency → return False.
    # 4. Otherwise → return True (it's possible to permute into a palindrome).

    # Time Complexity (TC): O(n)
    # ------------------------------
    # - We scan the string once to count character frequencies.
    # - Then, we iterate through the counts (limited by unique characters).
    # - n = length of the input string.

    # Space Complexity (SC): O(1)
    # ------------------------------
    # - We use a Counter (hash map), but since character sets are limited (e.g., 26 lowercase 
    #   letters), the extra space doesn't scale with n, so it's considered O(1) space.


from collections import Counter

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # Count the frequency of each character in the string
        letter_count = Counter(s)
        
        # A string can be permuted into a palindrome if:
        # - At most **one character** has an odd count.
        # - All others must have even counts.
        
        odd_count = 0  # Track how many characters have odd frequencies
        
        for count in letter_count.values():
            if count % 2 != 0:
                odd_count += 1 # Increase odd count
                # If more than one character has an odd count, it's not a palindrome permutation
                if odd_count > 1:
                    return False
        
        return True  # Valid palindrome permutation



sol = Solution()
print(sol.canPermutePalindrome("code"))
print(sol.canPermutePalindrome("aab"))
print(sol.canPermutePalindrome("carerac"))
print(sol.canPermutePalindrome("aaa"))
