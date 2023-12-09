# Given two strings needle and haystack, return the index of the first occurrence of 
# needle in haystack, or -1 if needle is not part of haystack.

# Example 1:
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.

# Example 2:
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.

# How to Solve:
    # Need to use a nested for loop:
    # Iterate X times for haystack (how many is optimal?), and create a nested for
    # that iterates X times (to go through each character in the needle)
    # If the first character of needle does not equal the current character iteration
    # of haystack, break, and move on to the next iteration of haystack
    # If it does, continue the nested for loop and check if the current iteration of 
    # "j" equals the length of the last index of needle
    # Return the index or -1

class Solution(object):
    def strStr(self, haystack, needle):
        if needle == "": #If our needle is an empty string, they want us to 
            return 0 # return zero (Only sais this in neetcode video not leetcode problem)
        
        for i in range(len(haystack) + 1 - len(needle)): # We only need to iterate
            # to the last possible index the needle could start in the haystack,
            # in example 1, we would only iterate to the second "s" since needle
            # is three characters long and couldn't start at the second to last index
            for j in range(len(needle)): # Iterate through each character in needle
                if haystack [i + j] != needle[j]: # "i" is the index we start at in
                # the haystack, and "j" is the incrementer (0, 1, 2).
                    break # If the index we are at on the haystack is not equal to the
                    # first character of needle, break out of the for loop and return
                    # to the top to look at the next i position in our haystack. 
                if j == len(needle) - 1: # If they are equal, we want to continue to
                    # the next iteration of our j loop until we have seen every
                    # character and confirmed they're equal. We will know this when
                    # "j" (# of loops) is equal to the length of last index of needle
                        return i # Return i because we know that we didn't break out
                        # of the loop and we reached the last character and were all ==
            return -1 # Return -1 if not
            

# Other way to write it

    def strStr2(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1): # We only need to iterate
            # to the last possible index the needle could start in the haystack,
            # in example 1, we would only iterate to the second "s" since needle
            # is three characters long and couldn't start at the second to last index
            if haystack[i:(i + len(needle))] == needle: # Compare the characters
                # beginning on the index of each iteration of haystack through 
                # the index of the iteration plus the length of needle to the "needle"
                # string
                return i # If they are equal, return the index you are currently on.
                # If not, move to the next iteration of haystack
        return -1 # If you iterate through haystack and find no matches, return -1


solution = Solution()
print("example 1")
print(solution.strStr("sadbutsad", "sad"))
print("example 2")
print(solution.strStr("leetcode", "leeto"))








