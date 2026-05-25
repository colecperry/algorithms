# 268. Missing Number

# Topics: Array, Hash Table, Math, Binary Search, Bit Manipulation, Sorting

# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# Example 1:
# Input: nums = [3,0,1]
# Output: 2
# Explanation:
# n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

# Example 2:
# Input: nums = [0,1]
# Output: 2
# Explanation:
# n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

# Example 3:
# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8
# Explanation:
# n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.


from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int: # Using a set - O(n) space
        """
        - TC: O(n) - two passes through n
        - SC: O(n) - store each ele in a set
        """
        nums_range = set(range(len(nums) + 1)) # add all nums in range (0 to n) to a set 
        
        for n in nums: # iterate through nums array & remove those ele's from the set
            nums_range.remove(n) 
        return nums_range.pop() # last ele in the set will be the missing number

    def missingNumber2(self, nums: List[int]) -> int: # Guass Formula - O(1) space
        """
        - TC: O(n) - sum iterates over the whole array
        - SC: O(1) - only variables
        """
        n = len(nums)
        expected = n * (n + 1) // 2 # get the expected output of the list with no missing number
        actual = sum(nums) # get the actual output of the list
        return expected - actual # the difference is the missing number

sol = Solution()
print(sol.missingNumber3([3,0,1])) # 2
print(sol.missingNumber([0,1])) # 2
print(sol.missingNumber([9,6,4,2,3,5,7,0,1])) # 8



