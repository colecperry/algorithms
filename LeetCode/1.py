# 1 - Two Sum

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

# Options to Solve

# 1. Brute Force
# Take the first number of the array, and check every combination of that number with the remaining numbers of the array
# For example 1, check 2 against 7, 11, and 15. Repeat the process for number 7, check it against 11 and 15

# 2. One Pass
# Take the target number and subtract the number in the array at index i, and check if the number that equals target - number at index i exists. 
# For example 1, given the target = 9 and number 2 at index[0], does the 7 exist?
# The problem lies that if you added the values/indexes to your hashmap before checking, it could re-use the value
# Like in example 2, after checking i[0], it would look to see if 3 exists, and then find it again/duplicate
# The solution is to only add the value and indexes after you check if the value exists, as opposed to adding them all in the beginning

# Code Explination
# Step 1: Create a method twoSum that takes in three paramaters: self, nums(list of numbers), and target
# Step 2: Create an empty dictionary, valToIdx. This dictionary will be used to store previous encountered numbers as keys and their corresponding indicies as values.
# Step 3: Create a for loop that iterates over the nums list. The enumerate() function returns both the index(i) and corresponding value (n) of each element in the list
# For example, if nums is [1, 2, 3, 4, 5], in the first iteration, i would be 0 and n would be 1.
# Step 4: Calculate the difference between the target value and the current element n in the list
# For example, if the target is 8 and n is 3, the difference would be 5.
# Step 5: Check to see if "diff" is already present as a key in valToIdx dictionary. The difference represents that value that needs to be found in order to reach the target
# For example, if diff is 5 and valToIdx already has 5 as a key, it means there is a pair of numbers that sum up to the target.
# Step 6: If the difference is found in the dictionary, the function immediately returns a list containing the indicies of the two numbers, [valToIdx[diff], i]. valToIdx[diff] retrieves the index value associated with the difference with the dictionary, while i represents the current index
# For example, if the valToIdx dictionary has 5 as a key with a value of 1 and the current index i is 2, the function would return [1, 2].
# Step 7: valToIdx[n] = i. This line adds the current number n as a key to the valToIdx dictionary with its corresponding index i as the value. This is done to keep track of the previously encountered numbers and their indices, allowing for efficient lookups in the future.
# Step 8: return. If no pair of numbers is found that adds up to the target during the loop, the function returns None or nothing.


class Solution(object):
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
