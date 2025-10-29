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

import heapq
from collections import Counter

class Solution:
    """
    TC
        - O(n) to create freq dict
        - O(m log m) to create max heap of m unique chars (iterate + heappush)
        - O(m log m) to extract chars (iterate + heappop)
        - O(n) to build result string (string concat copies existing string each time)
        - Total: O(n + m log m)
    SC
        - O(m) to store m unique char freqs in dict
        - O(m) to store max heap of m chars
        - O(n) to store n chars in result string
        - Total: O(n)
    """
    def frequencySort(self, s: str) -> str:
        # Count frequency of each character
        freq_dict = Counter(s)
        
        # Build max heap from freq dict with (negative_freq, char)
        max_heap = []
        for char, freq in freq_dict.items():
            heapq.heappush(max_heap, (-freq, char)) # freq first
        
        # Extract characters in frequency order (highest first)
        sol = ""
        while max_heap:
            freq, char = heapq.heappop(max_heap)
            sol += (char * -freq)  # Concat char * freq
        return sol

sol = Solution()
print(sol.frequencySort("tree"))
print(sol.frequencySort("cccaaa"))
print(sol.frequencySort("Aabb"))