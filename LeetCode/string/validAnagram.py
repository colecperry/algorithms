# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# Pseudo Code: (Cole) -> O(N)
# If the length of s and t are not equal, return false
# Create a dictionary of key value pairs (key: string, value: integer)
# Iterate through t, if key not in dict, add key with count 1
# If key in dict, add one to count for that key
# Iterate through s, if key not in dict, return false
# If key in dict, subtract one from count for that key's value
# If value for key gets to zero, remove key-value pair from dict
# Return true if dict is empty

# Constraints:
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        dict = {}
        for i, n in enumerate(t):
                if n not in dict:
                    dict[n] = 1
                else:
                    dict[n] += 1
        for char in s:
            if char in dict:
                dict[char] -= 1
                if dict [char] == 0:
                    del dict[char]
        return len(dict) == 0
    
    # Neetcode Solution 1 - Dictionary
    def isAnagram2(self, s, t):
        if len(s) != len(t): # If lengths are different they are not anagrams
            return False
        
        countS, countT = {}, {} # Create two dictionaries to store key value pairs for frequency of each char in s&t

        for i in range(len(s)): # Can iterate with len(s) since both strings are same length
            countS[s[i]] = 1 + countS.get(s[i], 0) # Increment the count of the key-value pairs. S is the string, s[i] is the character at the string of i index
            countT[t[i]] = 1 + countT.get(t[i], 0)# countT.get(t[i], 0) creates a key-value pair if none already exist
        for key in countS: # Iterate over each key in the dictionary S
            if countS[key] != countT.get(key, 0): # if that key's value in dict S != that key's value in dict T,
                return False 
        
        return True
    
    # Neetcode Solution 2 - Sorting - Python's built in sort uses Timsort which is a a hybrid sorting algorithm dervided from merge sort and insertion sort. Time complexity is O(n log n)
    def isAnagram2(self, s, t):
        return sorted(s) == sorted(t)



s1 = "anagram"
t1 = "nagaram"

my_solution = Solution()
print(my_solution.isAnagram(s1, t1))

s2 = "rat"
t2 = "car"

print(my_solution.isAnagram(s2, t2))


print("-----------------------------")
print(my_solution.isAnagram2(s1, t1))
print(my_solution.isAnagram2(s2, t2))