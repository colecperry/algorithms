# 1408. String Matching in an Array

# Topics: Array, String, String Matching

# Given an array of string words, return all strings in words that are a substring of another word. You can return the answer in any order.

# Example 1:
# Input: words = ["mass","as","hero","superhero"]
# Output: ["as","hero"]
# Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
# ["hero","as"] is also a valid answer.

# Example 2:
# Input: words = ["leetcode","et","code"]
# Output: ["et","code"]
# Explanation: "et", "code" are substring of "leetcode".

# Example 3:
# Input: words = ["blue","green","bu"]
# Output: []
# Explanation: No string of words is substring of another string.

# High-Level Idea:
    # For each word, check if it is a substring of any other word in the list.
    # If it is, add it to the result.
    # Make sure to skip the iterations where i == j
    # Use a set to avoid duplicate entries in case the same substring appears in multiple words.

    # Time Complexity (TC): O(n^2 * k)
    # - We compare each word with every other word => O(n^2)
    # - Each substring check (`in`) takes up to O(k), where k is the max word length.

    # Space Complexity (SC): O(m)
    # - We store up to m matching words in the output set (m ≤ n).


from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        output = set() # Use a set to skip duplicates (substring in multiple words)
        for i in range(len(words)): # Iterate through each word
            for j in range(len(words)): # And compare to every other word
                if words[i] in words[j] and i != j: # Check if word is in the other
                    output.add(words[i]) 

        return list(output) 

sol = Solution()
print(sol.stringMatching(["mass","as","hero","superhero"]))
print(sol.stringMatching(["leetcode","et","code"]))
print(sol.stringMatching(["blue","green","bu"]))