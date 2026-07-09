# 409. Longest Palindrome

# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome.

# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome.

# Example 1:
# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

# Example 2:
# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.

# Topics: Hash Table, String, Greedy

# How to Solve (High Level):
    # Step 1: Count how many times each character appears in the string
    # Step 2: Initialize a counter to track the length of the palindrome
    # Step 3: Use a flag to track if a middle character (with an odd count) has been used
    # Step 4: For each character count:
    #   - Add the largest even number of characters (i.e., full pairs) to the total length
    #   - If there's an unused odd-count character, add 1 for the center and mark it as used
    # Step 5: Return the total length of the longest possible palindrome

# Time Complexity: O(n), where n is the length of the string
# Space Complexity: O(1), since the number of unique characters (A–Z, a–z) is bounded



from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        letter_counts = Counter(s)
        total_length = 0
        used_middle_letter = False

        for char, count in letter_counts.items():
            # Find how many full pairs we can make from this character
            pairs = count // 2
            # Each pair adds 2 characters to the palindrome
            total_length += pairs * 2

            # If there's an unused middle and we have an odd count, use one in the center
            if count % 2 == 1 and not used_middle_letter:
                total_length += 1
                used_middle_letter = True

        return total_length


sol = Solution()
print(sol.longestPalindrome("abccccdd"))
print(sol.longestPalindrome("a"))
print(sol.longestPalindrome("ccca"))