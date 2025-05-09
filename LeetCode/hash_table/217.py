# 217 - Contains Duplicate

# Topics - Array, Hashtable, Sorting

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1: 
# Input: nums = [1,2,3,1]
# Output: true

# Example 2: 
# Input: nums = [1,2,3,4]
# Output: false

# Example 3: 
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

# How to solve
# Create a dictionary
# Iterate through the dictionary
    # If the value is not in the dict, add it to the dict
    # If the value is in the dict, return true
# If we iterate all the way through, we have all different numbers, return false

class Solution(object):
    def containsDuplicate(self, nums):
        numdict = {}
        for i, n in enumerate(nums):
            if n in numdict:
                return True
            numdict[n] = i
            print(numdict[n])
        return False
    
# Also viable solution
# class Solution(object): 
#     def containsDuplicate(self, nums):
#         numlist =[]
#         for n in nums:
#             if n in numlist:
#                 return True
#             numlist.append(n)
#         return False


solution = Solution()
print(solution.containsDuplicate([1,2,3,1]))
