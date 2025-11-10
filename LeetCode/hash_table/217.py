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

class Solution(object):
    """
    TC:
        - O(n) due to iterating through the nums dict once
    SC:
        - O(n) due to storing worst case each num in nums in numdict
    """
    def containsDuplicate(self, nums):
        numdict = {} # dictionary to store nums we've seen
        for i, n in enumerate(nums):
            if n in numdict: # If num already in dict it's a duplicate
                return True
            numdict[n] = i # If not add it
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
