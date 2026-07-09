# 1876. Substrings of Size Three with Distinct Characters

# Topics: Hash Table, String, Sliding Window, Counting

# A string is good if there are no repeated characters.

# Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.

# Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

# A substring is a contiguous sequence of characters in a string.

# Example 1:
# Input: s = "xyzzaz"
# Output: 1
# Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
# The only good substring of length 3 is "xyz".

# Example 2:
# Input: s = "aababcabc"
# Output: 4
# Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
# The good substrings are "abc", "bca", "cab", and "abc".

# Key Insight: recognize that this is a fixed length sliding window question with a size of three

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        l = 0 # Start left pointer at idx 0
        good_string_count = 0 # count for good substrings
        for r in range(2, len(s)): # start right pointer at idx 2
            my_set = set(s[l:r + 1]) # Count unqiue chars from l to r
            if len(my_set) == 3: # If len == 3, each char is unique
                good_string_count += 1 # Increment count & 
            l += 1 # increment pointer
            
        return good_string_count

sol = Solution()
print(sol.countGoodSubstrings("xyzzaz")) # 1
print(sol.countGoodSubstrings("aababcabc")) # 4