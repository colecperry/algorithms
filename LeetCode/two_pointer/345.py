# 345. Reverse Vowels of a String

# Topics: Two Pointers, String

# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# Example 1:
# Input: s = "IceCreAm"
# Output: "AceCreIm"
# Explanation:
# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"

# How to Solve
    # Key Insight:
    # ---------------------------------
    # - Use a **two-pointer approach**:
    #     - One pointer starts from the beginning (`l`), the other from the end (`r`).
    #     - Move both pointers inward, swapping vowels when both pointers are at vowel characters.
    #     - Skip over non-vowel characters.
    # - Since strings are **immutable** in Python, convert the string to a **list** for in-place
    #   modifications, then join it back into a string at the end.

    # Steps to Solve:
    # ---------------------------------
    # 1. Define a set or string containing all vowels (including uppercase for case insensitivity).
    # 2. Initialize two pointers: `l` at the start and `r` at the end of the string.
    # 3. Convert the input string into a list for in-place swapping.
    # 4. While `l < r`, do:
    #     - If both `s[l]` and `s[r]` are vowels, swap them and move both pointers inward.
    #     - If `s[l]` is not a vowel, move `l` forward.
    #     - If `s[r]` is not a vowel, move `r` backward.
    # 5. After processing, join the list back into a string and return it.

    # Time Complexity (TC): O(n)
    # ---------------------------------
    # - Each character in the string is checked at most once.
    # - n = length of the string.

    # Space Complexity (SC): O(n)
    # ---------------------------------
    # - A list copy of the string is created to allow in-place modification.
    # - The extra space used is proportional to the input string length.


class Solution:
    def reverseVowels(self, s: str) -> str:
        l, r = 0, len(s) - 1
        s_list = list(s)  # Strings are immutable, convert to list for in-place swaps
        vowels = 'aeiouAEIOU'  # Include uppercase vowels for completeness

        while l < r:
            if s_list[l] in vowels and s_list[r] in vowels:
                # Swap vowels at positions l and r
                s_list[l], s_list[r] = s_list[r], s_list[l]
                l += 1
                r -= 1
            elif s_list[l] not in vowels:
                l += 1  # Move left pointer if not a vowel
            elif s_list[r] not in vowels:
                r -= 1  # Move right pointer if not a vowel

        return ''.join(s_list)  # Convert list back to string



sol = Solution()
print(sol.reverseVowels("IceCreAm"))
print(sol.reverseVowels("leetcode"))