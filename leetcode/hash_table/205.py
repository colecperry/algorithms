# 205. Isomorphic Strings

# Topics - Hash Table, String

# Given two strings s and t, determine if they are isomorphic. Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

# Example 1:
# Input: s = "egg", t = "add"
# Output: true

# Explanation:
# The strings s and t can be made identical by:
# Mapping 'e' to 'a'.
# Mapping 'g' to 'd'.

# Example 2:
# Input: s = "foo", t = "bar"
# Output: false

# Explanation:
# The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

# Example 3:
# Input: s = "paper", t = "title"
# Output: true

# How to Solve:
    # Create two hashmaps: one maps characters from string S to string T, and one maps characters from string T to string S
    # Loop through either string (both are the same length)
        # Assign variables for each string at current index
        # If first character is in first map and if value of first character in first map is not equal to character 2 (char in string 2 at index i)
        # OR
        # If second character is in the second map and if the value of the second character in the second map is not equal to character 1 (char in string 1 at index i)
            # Return False
        # Map the character in first string to second string, and map character in second string to character in first string
    # Return True if we exit the loop

# Time Complexity: O(n)
# The function iterates through both strings once, performing constant-time operations (dictionary lookups and assignments) for each character.
# Since there are n characters in each string, the overall time complexity is O(n).

# Space Complexity: O(1)
# The function uses two hash maps (dictionaries) to store mappings between characters from 's' and 't'.
# In the worst case, each dictionary stores every unique character from 's' and 't'.
# Since the input consists of ASCII characters (limited to 128 unique characters), the space usage is bounded by O(1).


class Solution(object):
    def isIsomorphic(self, s, t):
        mapST, mapTS = {}, {} # Create dictonary mappings from S->T and T->S
        # Iterate through two strings simultaneously
        for c1, c2 in zip(s, t): 
            # Checks if key pair is already in mapST or TS with different value than c1 or c2
            if ((c1 in mapST and mapST[c1] != c2) or (c2 in mapTS and mapTS[c2] != c1)):
                return False
            
            mapST[c1] = c2 # Map c1 to c2 in mapST
            mapTS[c2] = c1 # Map c2 to c1 in mapTS
        
        return True
    
    def isIsomorphic2(self, s: str, t: str) -> bool:

        mapping_s_t = {}  #  Create dictonary mappings from S->T and T->S
        mapping_t_s = {}

        for c1, c2 in zip(s, t): # Iterate through two strings, char by char (c1 for s and c2 for t)

            # Case 1: No mapping exists in either of the dictionaries
            if (c1 not in mapping_s_t) and (c2 not in mapping_t_s):
                mapping_s_t[c1] = c2 # Map c1 to c2 in st dict
                mapping_t_s[c2] = c1 # Map c2 to c1 in ts dict

            # If mapping exists, check if value for c1 is not equal to c2 or vise versa -> return False, if mapping exits but values equal, skip adding to dicts
            elif mapping_s_t.get(c1) != c2 or mapping_t_s.get(c2) != c1:
                return False

        return True

my_solution = Solution()
print(my_solution.isIsomorphic2("egg", "add"))
print(my_solution.isIsomorphic2("foo", "bar"))
print(my_solution.isIsomorphic("bar", "foo"))
print(my_solution.isIsomorphic("paper", "title"))