# 520. Detect Capital

# Topics: String

# We define the usage of capitals in a word to be right when one of the following cases holds:

# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Given a string word, return true if the usage of capitals in it is right.

# We define the usage of capitals in a word to be right when one of the following cases holds:

# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Given a string word, return true if the usage of capitals in it is right.

# Example 1:

# Input: word = "USA"
# Output: true
# Example 2:

# Input: word = "FlaG"
# Output: false

# Time Complexity: O(n), where n is the length of the word
# - word.isupper(), word.islower(), and word[1:].islower() each scan the string once.

# Space Complexity: O(1)
# - Constant extra space is used; string methods do not require additional space proportional to input 
#   size.


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return (word[0].isupper() and word[1:].islower()) or word.isupper() or word.islower()
    
sol = Solution()
print(sol.detectCapitalUse("USA"))
print(sol.detectCapitalUse("FlaG"))
