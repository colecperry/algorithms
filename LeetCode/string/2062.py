# 2062. Count Vowel Substrings of a String

# Topics: Hash Table, String

# A substring is a contiguous (non-empty) sequence of characters within a string.

# A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u') and has all five vowels present in it.

# Given a string word, return the number of vowel substrings in word.

# Example 1:
# Input: word = "aeiouu"
# Output: 2
# Explanation: The vowel substrings of word are as follows (underlined):
# - "aeiouu"
# - "aeiouu"

# Example 2:
# Input: word = "unicornarihan"
# Output: 0
# Explanation: Not all 5 vowels are present, so there are no vowel substrings.

# Example 3:
# Input: word = "cuaieuouac"
# Output: 7
# Explanation: The vowel substrings of word are as follows (underlined):
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        pass

sol = Solution()
print(sol.countVowelSubstrings("aeiouu")) # 2
print(sol.countVowelSubstrings("unicornarihan")) # 0
print(sol.countVowelSubstrings("cuaieuouac")) # 7