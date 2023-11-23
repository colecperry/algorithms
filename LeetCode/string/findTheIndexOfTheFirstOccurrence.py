import ipdb;

# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1: Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.

# Example 2: 
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.

# Class Definition: class Solution(object):

# This line defines a class named Solution.
# Method Definition: def strStr(self, haystack, needle):

# This line defines a method named strStr within the Solution class.
# The method takes three parameters: self, haystack, and needle.
# The self parameter is used in object-oriented programming to refer to the instance of the class.
# The haystack parameter represents the string in which we want to search for the needle.
# The needle parameter represents the substring that we want to find in the haystack.
# Looping through the Haystack: for i in range(len(haystack) - len(needle) + 1):

# This line starts a for loop that iterates over the indices of the haystack string.
# The loop is set up to iterate up to len(haystack) - len(needle) + 1 to ensure that we don't go beyond the length of the haystack while checking for the needle.
# For example, if haystack is "hello" and needle is "ll", the loop will iterate over indices 0, 1, 2.
# Checking for Needle: if haystack[i:i + len(needle)] == needle:

# This if statement checks if the substring of haystack from index i to i + len(needle) matches the needle string.
# The expression haystack[i:i + len(needle)] retrieves a slice of the haystack string that has the same length as the needle string, starting from index i.
# If the slice is equal to the needle, it means we have found a match.
# Returning the Index: return i

# If a match is found, the method immediately returns the index i, which represents the starting position of the needle in the haystack.
# Returning -1: return -1

# If the loop completes without finding a match, the method returns -1 to indicate that the needle is not present in the haystack.

# Solution with Jen
# We only iterate through the length of the haystack minus the length of the needle plus one because if we iterated any longer we would go out of bounds - if we know that needle is 3 characters long and haystack is 9, we would stop at 7th index
# We are going to loop through haystack, and for each loop, we are going to use slice haystack to compare the index [i:(i+len(needle) to needle]


class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1): 
            if haystack[i:(i + len(needle))] == needle:
                return i
        return -1
    

solution = Solution()
print(solution.strStr("sadbutsad", "sad"))


# OTHER SOLUTION
# def strStr(haystack, needle):
#     return haystack.find(needle)








