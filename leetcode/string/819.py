# 819. Most Common Word

# Topics: Array, Hash Table, String Counting

# Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

# The words in paragraph are case-insensitive and the answer should be returned in lowercase.

# Note that words can not contain punctuation symbols.

# Example 1:
# Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
# Output: "ball"
# Explanation: 
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"), 
# and that "hit" isn't the answer even though it occurs more because it is banned.

# Example 2:
# Input: paragraph = "a.", banned = []
# Output: "a"

# Clean the paragraph by removing punctuation and converting all letters to lowercase
# Split the cleaned paragraph into individual words
# Count the frequency of each word using a Counter from the collections module
# Iterate through the words in descending order of frequency using Counter.most_common()
#   - For each word, check if it is not in the list of banned words
#   - Return the first word that is not banned (this will be the most common allowed word)

# Time Complexity: O(n), where n is the number of characters in the paragraph
# - Cleaning, splitting, and counting all take linear time
# - most_common() is O(k log k), where k is the number of unique words (usually small)

# Space Complexity: O(k), where k is the number of unique words
# - Additional space is used for the word list, Counter, and set of banned words


from collections import Counter
from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # Clean punctuation and lowercase everything
        for ch in "!?',;.":
            paragraph = paragraph.replace(ch, " ")
        words = paragraph.lower().split()

        # Count frequencies
        counts = Counter(words)

        # Return the most common non-banned word
        for word, freq in counts.most_common():
            if word not in set(banned):
                return word
            
sol = Solution()
print(sol.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
print(sol.mostCommonWord("a.", []))