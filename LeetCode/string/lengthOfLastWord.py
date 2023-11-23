import ipdb;

# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal 
# substring
#  consisting of non-space characters only.

# Example 1: Input: s = "Hello World"
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.

# Example 2: Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.

# Solution
# 1. Use a list comprehension to iterate over each character the array and split by spaces if 
# the character is not equal to a space
# 2. Return the length of the last item in the list (X)

# class Solution(object):
#     def lengthOfLastWord(self, s):
#         xs = [x for x in s.split(" ") if x.strip() != ""]
#         # ipdb.set_trace()
#         return len(xs[len(xs) - 1])

# Step 1: Split the list by spaces
# Step 2: Iterate backwards over the list
# Step 3: Since each space is an empty string, we know the first word from the end is the answer

def lengthOfLastWord(s):
    split_text = s.split()
    print(split_text)
    print(len(split_text[-1]))


lengthOfLastWord("   fly me   to   the moon  ")
    
# class Solution(object):
#     def lengthOfLastWord(self, s):
#         xs = s.split(" ")
#         print(xs)

#         for i in range(len(xs) - 1, 0, -1):
#             # print("Before strip:", xs[i])
#             if len(xs[i]) > 0:
#                 # print("xs[i]:", xs[i])
#                 return (xs[i])
        

# solution = Solution()
# print(solution.lengthOfLastWord("   fly me   to   the moon  "))
