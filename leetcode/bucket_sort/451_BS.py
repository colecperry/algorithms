# 451. Sort Characters By Frequency

# Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

# Return the sorted string. If there are multiple answers, return any of them.

# Example 1:
# Input: s = "tree"
# Output: "eert"
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

# Example 2:
# Input: s = "cccaaa"
# Output: "aaaccc"
# Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
# Note that "cacaca" is incorrect, as the same characters must be together.

# Example 3:
# Input: s = "Aabb"
# Output: "bbAa"
# Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.

from collections import Counter

class Solution:
    """
    TC: O(n)
        - Create freq map for each char: O(n)
        - Place each unique char in bucket: O(m) where m = unique chars
        - Iterate buckets + build output: O(n) 
            - Outer loop: O(n) buckets
            - Inner loop: O(m) unique chars total across all iterations
            - String concat (char * i): O(n) total across all iterations
        - Total: O(n)  ✅ But needs clarification
    SC: O(n)
        - Buckets array: O(n)
        - Freq dict: O(m) where m = unique chars
        - Output string: O(n)
        - Total: O(n)  ✅
    """
    def frequencySort(self, s: str) -> str:
        # Create buckets where index = frequency, value = chars with that frequency
        buckets = [''] * (len(s) + 1) # Each i -> empty string
        freqs = {}
        
        # Count frequency of each character
        for char in s:
            freqs[char] = freqs.get(char, 0) + 1 # gets freq for char in the freq map, default freq 0, ++

        # Place each character in bucket based on its frequency
        for char, freq in freqs.items():
            buckets[freq] += char
        
        output = ''

        # Iterate buckets from highest to lowest frequency
        for i in range(len(buckets) - 1, -1, -1):
            for char in buckets[i]:  # Iterate over each char at this frequency (bucket)
                output += char * i  # Append char repeated i times
                
        return output

sol = Solution()
print(sol.frequencySort("tree"))
print(sol.frequencySort("cccaaa"))
print(sol.frequencySort("Aabb"))