# 14 - Longest Common Prefix

# Topics: String, Trie

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# How to solve:
    # Create variable to store longest common prefix
    # Create an index based loop for comparing the letters(assume first word is the longest to start)
        # Create a for loop to loop through each word
        # Check if the index is equal to the length of the word we are currently on (we found a shorter word than the first) -> Elimintates index OOB issue
        # Compare the letter at index i of the first word to the letter at index i of the current word
            # If they are different stop the loop and return
        # If we loop through each word and they all match, add the letter to the result
    # Return the result at the end (this assumes that all words match completely)

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

class Solution(object):
    def longestCommonPrefix(self, strs):
        res = "" # Create variable to store longest common prefix

        for i in range(len(strs[0])): # Iterate over the index of the first word
            for s in strs: # Iterate over each word in array
                if i == len(s) or s[i] != strs[0][i]: # Stop loop if we find shorter word or curr letter != first  letter of words we're comparing
                    return res # And return the result
            res += strs[0][i] # Else add the letter to the res

        return res
    
    def longestCommonPrefix2(self, strs):
        if not strs:
            return ""
        prefix = strs[0] 
        for string in strs[1:]:
            print(string.find(prefix))
            while string.find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
    
my_solution = Solution()
print(my_solution.longestCommonPrefix2(["flower","flow","flight"]))
print(my_solution.longestCommonPrefix(["dog","racecar","car"]))