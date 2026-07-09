# 15 - 3Sum

# Topics - Array, Two Pointers, Sorting

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

# Example 2:
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.

class Solution(object):
    """
    - TC: O(n)^2 - one loop for fixed index i and another while loop w two pointers iterates through rest
    - SC: O(1) - no extra data structures
    """
    def threeSum(self, nums):
        nums.sort() # Sort so two pointer logic works (moving l/r changes sum predictably)
        res = []

        for i in range(len(nums)): # Fix i as the first number in the triplet
            if i != 0 and nums[i] == nums[i - 1]: # Skip duplicate values of i to avoid duplicate triplets
                continue

            l, r = i + 1, len(nums) - 1 # Two pointers search the rest of the array

            while l < r:
                sum = nums[i] + nums[l] + nums[r]

                if sum == 0: # Valid triplet found
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1 # Move left pointer to look for more triplets
                    while l < r and nums[l] == nums[l - 1]: # Skip duplicate values of l
                        l += 1
                elif sum > 0: # Sum too big — move r left to decrease sum
                    r -= 1
                else: # Sum too small — move l right to increase sum
                    l += 1

        return res

my_solution = Solution()
print(my_solution.threeSum([-1,0,1,2,-1,-4]))
print(my_solution.threeSum([0,1,1]))
print(my_solution.threeSum([0,0,0]))
print(my_solution.threeSum([-2,-1,-1,0,1,3])) # inner while loop gets triggered

