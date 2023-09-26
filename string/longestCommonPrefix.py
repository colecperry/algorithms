# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1: 
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2: 
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings. 

class Solution(object):
    def longestCommonPrefix(self, strs):
        # 1. Step 1: Start the result with an empty string
        res = ""

        # 2. Step 2: Iterate over every character in the first string
        for i in range(len(strs[0])):
            # 3. Step 3: Iterate over every other string in the list strs
            # print("-----")
            # print("At index:", i)
            for s in strs:
                # print("  --")
                # print("  s:", s)

                # 4. Step 4: Check to see i is out of bounds
                # Step 5: If the current index of the word you are iterating over ("s in strs") is not equal to the current index you are on in the string interation, return the result because there is no further common prefix
                # Step 6: If they are equal or you are not currently out of bounds, add the letter of the first string at index i to the result
                # Step 7: If the inner for loop runs and all the conditions are met, the for loop will move back to line 19 where it grabs the next letter in the first word of the list
                if i >= len(s) or s[i] != strs[0][i]:
                    return res
                # print("  s[i]:", s[i])
                # print("  strs[0][i]:",  strs[0][i])
            res = res + strs[0][i]
            # print("res:", res)

        return res
    
solution = Solution()
print(solution.longestCommonPrefix(["dog","racecar","car"]))
    
# Faster solution!!!

# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         s = min(strs, key=len)
#         for i in strs:
#             while len(s) > 0:
#                 if i.startswith(s):
#                     break
#                 else:
#                     s = s[:-1]
#         return s


