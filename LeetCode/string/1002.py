# 1002. Find Common Characters

# Topics: Array, Hash Table, String

# Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

# Example 1:
# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]

# Example 2:
# Input: words = ["cool","lock","cook"]
# Output: ["c","o"]

# How to Solve:
    # Start by counting the frequency of each character in the first word
    # Loop through the remaining words one by one
    #   - For each word, count the frequency of each character
    #   - For each character in the original count:
    #       - If the character is also in the current word, keep the minimum count between the two
    #       - If the character is missing in the current word, set its count to 0
    # After processing all words, build the result by repeating each character based on its final count
    # Return the list of common characters including duplicates

# Time Complexity: O(n * k), where n is the number of words and k is the average length of each word
# - Each word is processed to count characters, and character counts are compared across all words

# Space Complexity: O(1), since the alphabet size is fixed (at most 26 lowercase letters)
# - The Counter dictionaries store at most 26 entries, regardless of input size


from typing import List
from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # Initialize the count dictionary using the first word
        common_count = Counter(words[0])

        # Compare with the rest of the words
        for word in words[1:]:
            current_count = Counter(word)
            # Keep the minimum count of each character seen so far
            for char in list(common_count): # Start with first word
                if char in current_count: # Compare next word to that
                    common_count[char] = min(common_count[char], current_count[char])
                else:
                    # Remove the character if it doesn't exist in the current word
                    common_count[char] = 0

        # Build the result list using the final counts
        result = []
        for char, count in common_count.items():
            result.extend([char] * count)

        return result

# Example usage
sol = Solution()
print(sol.commonChars(["bella", "label", "roller"]))  # ['e', 'l', 'l']
print(sol.commonChars(["cool", "lock", "cook"]))      # ['c', 'o']





sol = Solution()
print(sol.commonChars(["bella","label","roller"]))
print(sol.commonChars(["cool","lock","cook"]))

