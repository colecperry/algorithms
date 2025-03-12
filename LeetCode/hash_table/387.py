# 387. First Unique Character in a String

# Hash Table, String, Queue, Counting

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

# Example 1:
# Input: s = "leetcode"
# Output: 0
# Explanation:

# The character 'l' at index 0 is the first character that does not occur at any other index.

# Example 2:
# Input: s = "loveleetcode"
# Output: 2

# Example 3:
# Input: s = "aabb"
# Output: -1

# How to Solve:
    # Iterate over the string and add frequencies for each character (can use default dict or counter)
    # Iterate over the string again, and check if char at index i occurs once in the hashmap, if it does, return that index, if none occur once, return -1 

from collections import Counter, defaultdict

class Solution(object):
    def firstUniqChar(self, s):
        freq_dict = Counter(s) # Creates a freq dict

        for i in range(len(s)): # Loop over the string
            if freq_dict[s[i]] == 1: # Check if char at index i is 1 in dict
                return i 
            
        return -1
    
    def firstUniqChar2(self, s):
        freq_dict = defaultdict(int) # Creates a default dict with all zero's as values

        for c in s:
            freq_dict[c] += 1 # Populate dict

        for i, c in enumerate(s):
            if freq_dict[c] == 1:
                return i
            
        return -1


my_solution = Solution()
print(my_solution.firstUniqChar("leetcode"))
print(my_solution.firstUniqChar("loveleetcode"))
print(my_solution.firstUniqChar("aabb"))

