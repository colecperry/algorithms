# 383 - Ransom Note

# Topics - Hash Table, String, Counting

# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true

from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        magazine_counter = Counter(magazine) # Create dict of char freq's

        for char in ransomNote:
            if magazine_counter[char] == 0 or magazine_counter[char] == None:
                return False
            else:
                magazine_counter[char] -= 1
        return True

# How to Solve (one hashmap):
    # Create a character frequency hashmap for magazine (the longer string)
    # Loop through each character of the ransomNote string (smaller string):
        # If that char does not exist or == 0 in the hashmap, return False
        # If it does exist, decrement the counter
    # If we loop through the whole string and every char in the smaller string ransomNote exists in the larger string magazine, return True

my_solution = Solution()

ransomNote1 = "a"
magazine1 = "b"
ransomNote2 = "aa"
magazine2 = "ab"
ransomNote3 = "aa"
magazine3 = "aab"
print(my_solution.canConstruct(ransomNote1, magazine1))
print(my_solution.canConstruct(ransomNote2, magazine2))
print(my_solution.canConstruct(ransomNote3, magazine3))



