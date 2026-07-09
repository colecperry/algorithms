# 1768. Merge Strings Alternately

# Topics: Two Pointers, Strings

# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

# Example 1:
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r

# Example 2:
# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b 
# word2:    p   q   r   s
# merged: a p b q   r   s

# Example 3:
# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q 
# merged: a p b q c   d

# High-Level Idea:
        # Merge two strings by alternating characters from each.
        # Start from the beginning of both strings and append one character from each at a time.
        # If one string is longer, append the remaining characters at the end.

        # Time Complexity (TC): O(n + m)
        # - We traverse each character in word1 and word2 exactly once,
        #   where n = len(word1) and m = len(word2)

        # Space Complexity (SC): O(n + m)
        # - We use a list to store the result with one character per position
        #   and convert it to a string at the end.

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ptr_1, ptr_2 = 0, 0
        output = []
        while ptr_1 < len(word1) and ptr_2 < len(word2): # While both have chars
            output.append(word1[ptr_1]) # Append first char in word_1
            output.append(word2[ptr_2]) # Append second char in word_2
            ptr_1 += 1
            ptr_2 += 1
        while ptr_1 < len(word1): # If only word_1 has chars left
            output.append(word1[ptr_1])
            ptr_1 += 1
        while ptr_2 < len(word2):
            output.append(word2[ptr_2]) # If only word_2 has chars left
            ptr_2 += 1
        return ('').join(output)


sol = Solution()
print(sol.mergeAlternately("abc", "pqr")) # "apbqcr"
print(sol.mergeAlternately("ab", "pqrs")) # "apbqrs"
print(sol.mergeAlternately("abcd", "pq")) # "apbqcd"