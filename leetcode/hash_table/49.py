# 49. Group Anagrams

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:
# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]

# How to solve:
# Use default dict which allows you to create a dict with default values, i.e., if you pass in list each value will initially be a list, or if you pass in "int" each value will be 0
# Loop through the word list, and create a list "count" of 26 integers that represent the counts of each word
# Loop through each letter and update the "count" list using ord(), which converts each character into it's corresponding Unicode code point. For example, ord("a") = 97, ord("b") = 98, so we need to subtract each letter from ord("a") to get the correct value
# Turn the key into a tuple (keys in a dict must be immutable)
# Add the word to the default dict for the specific key




from collections import defaultdict

class Solution(object):
        def groupAnagrams(self, strs):
            res = defaultdict(list) # map charCount to list of anagrams, defaultdict creates a dictionary initialized with an empty list as the value for each key
            for s in strs: # Loop through list
                count = [0] * 26 # count characters a-z (init to 0's)
                for c in s: # Loop through each list element (string)
                    count[ord(c) - ord("a")] += 1 # Get the ASCII index of the letter
                key = tuple(count) # Create "key" that's the count list as a tuple
                res[key].append(s) # Access the res default dict by key and append the word to the list
            return res.values() # Return the values of the dict (somehow it's a list of lists)

        def groupAnagrams2(self, strs):
            outer_dict ={}
            for i in range(len(strs)):
                inner_dict = {}
                for j in range(len(strs[i])):
                    if strs[i][j] not in inner_dict:
                        inner_dict[strs[i][j]] = 1
                    else:
                        inner_dict[strs[i][j]] += 1
                outer_dict[strs[i]] = inner_dict
            
            outer_list = set()

            for i in range(len(strs)):
                inner_list = set()
                for el in outer_dict:
                    if (not el and not strs[i]) or outer_dict[el] == outer_dict[strs[i]]:
                        inner_list.add(el)
                outer_list.add(frozenset(inner_list))
    
            return [list(inner) for inner in outer_list]

my_solution = Solution()
print(my_solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(my_solution.groupAnagrams([""]))
print(my_solution.groupAnagrams(["a"]))