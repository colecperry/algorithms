# 3. Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest substring without duplicate characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution:
    """
    - TC: O(n) -> right pointer visits each character once, left pointer never exceeds right
    - SC: O(n) -> set stores at most n characters in the worst case
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = set()  # Characters currently in the window
        longest = 0

        for right in range(len(s)):
            while s[right] in seen:  # Duplicate found — shrink window from left until it's gone
                seen.remove(s[left])
                left += 1
            
            seen.add(s[right])  # Window is valid — add new character
            longest = max(longest, right - left + 1)  # Is this window the longest we've seen?

        return longest

sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))
print(sol.lengthOfLongestSubstring("bbbbb"))
print(sol.lengthOfLongestSubstring("pwwkew"))