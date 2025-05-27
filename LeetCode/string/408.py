# 408. Valid Word Abbreviation

# Topics: Two Pointer, String

# A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.

# For example, a string such as "substitution" could be abbreviated as (but not limited to):

# "s10n" ("s ubstitutio n")
# "sub4u4" ("sub stit u tion")
# "12" ("substitution")
# "su3i1u2on" ("su bst i t u ti on")
# "substitution" (no substrings replaced)

# The following are not valid abbreviations:

# "s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
# "s010n" (has leading zeros)
# "s0ubstitution" (replaces an empty substring)
# Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

# A substring is a contiguous non-empty sequence of characters within a string.

# Example 1:
# Input: word = "internationalization", abbr = "i12iz4n"
# Output: true
# Explanation: The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n").

# Example 2:
# Input: word = "apple", abbr = "a2e"
# Output: false
# Explanation: The word "apple" cannot be abbreviated as "a2e".

# Problem: Validate whether a given abbreviation matches a full word.
#
# Strategy:
# - Iterate through each character in the abbreviation (abbr)
# - Track the current position in the original word using a counter
# - Accumulate any digits into a number to determine how many characters to skip in the word
# - If a letter is encountered:
#     - Apply the accumulated number (skip characters in word)
#     - Check if the current letter in abbr matches the word at the current position
#     - If not, return False
# - After the loop, apply any remaining accumulated number
# - Finally, check if the counter has exactly reached the end of the word
#
# Edge cases handled:
# - Leading zeros in numbers (e.g., "01") are invalid
# - Skipping past the end of the word is invalid
#
# Time Complexity: O(n + m), where
#     - n is the length of abbr
#     - m is the length of word (in worst case, we scan most of it)
#
# Space Complexity: O(1)
#     - We use only a few integer variables; no extra space that grows with input size

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word_index = 0  # Tracks the current position in the original word
        curr_digit = 0  # Accumulates digit characters into a number

        for i in range(len(abbr)): # loop through the abbreviation
            # Case 1: character in abbreviation is a digit
            if abbr[i].isdigit(): # Leading zero is not allowed (e.g., "01")
                if curr_digit == 0 and abbr[i] == '0': # Check if "0" is the first number in digit sequence
                    return False
                # Build the full number from consecutive digits
                curr_digit = curr_digit * 10 + int(abbr[i])
            else: # Case 2: character in abbreviation is not a digit (char)
                word_index += curr_digit # Increment counter by num accumulated so far (if any)
                curr_digit = 0  # Reset digit accumulator

                # If counter is out of bounds or characters do not match
                if word_index >= len(word) or abbr[i] != word[word_index]:
                    return False # Invalid match returns False
                word_index += 1  # Move to the next character in word

        # Apply any remaining number after the loop ends
        word_index += curr_digit

        # Final check: abbreviation must consume the entire word
        return word_index == len(word)


sol = Solution()
print(sol.validWordAbbreviation("internationalization", "i12iz4n"))
print(sol.validWordAbbreviation("apple", "a2e"))