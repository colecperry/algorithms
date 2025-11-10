# 1 - Two Sum

# Topics: Array, Hash Table

# Instructions
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

# Example 1: 
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3: 
# Input: nums = [3,3], target = 6
# Output: [0,1]

class Solution(object):
    """
    KEY INSIGHT: For each number, check if its complement (target - num) exists in the hashmap. Store numbers with their indices as you go—you need the index to return the answer—so when you find the complement, you have both indices ready.

    TC:
        - O(n) -> one pass through the array; worst case checks every element before finding complement
    SC:
        - O(n) -> worst case, we store every num & index in the hashmap
    """
    def twoSum(self, nums, target):
        valToIdx = {} # Create an empty dict to store values and corresponding indexes

        for i, n in enumerate(nums): # Iterate through the list nums
            diff = target - n   # Calc the difference: Target - num we are iterating on
            if diff in valToIdx: # Check if the matching number exists to add up to target
                return[valToIdx[diff], i] # If so, return the value (index) of the diff and the index you are iterating on. We know the index of diff in the dict will be the smaller b/c we don't find the solution until the second matching val
            valToIdx[n] = i # If not, add the number to the hahsmap
        return None
    
solution = Solution()
print(solution.twoSum([2, 4, 6, 8, 10], 16))
