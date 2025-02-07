# 15 - 3Sum

# Topics - Array, Two Pointers, Sorting

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# How to Solve:
# Brute Force: Triple loop
# Optimal:
    # Sort the input array
    # When we are searching for combinations on our first loop, and we get to the same number we skip it (this eliminates us from having duplicates)
    # Create left and right pointers l = i+1, r = len(nums)
    # Check for duplicates among left and right pointers by comparing l and r to nums[i], if found move the pointer
    # Add up the sum of i, l, and r
    # If it == 0 add to ans, if sum > 0 move right pointer over (decreases our sum), if sum < 0 move left pointer over (increases our sum)

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
    def threeSum(self, nums):
        nums.sort() # Sort the nums for 2 pointer
        ans = [] # Store answer
        for i, a in enumerate(nums): # Loop through idx and val
            if i > 0 and a == nums[i-1]: # Check for dups 
                continue # If dup found skip

            l,r = i + 1, len(nums) - 1 # Set two pointers
            while l < r: # Loop until they meet
                sum = a + nums[l] + nums[r] # Calc sum
                if sum == 0: # If sum is equal to zero
                    ans.append([a, nums[l], nums[r]]) # Append ans and move both ptrs
                    l += 1
                    r -=1
                    while l < r and (nums[l] == nums[l-1]): # Check for dups on l
                        l += 1
                    while l < r and nums[r] == nums[r+1]: # Check and skip dups for r
                        r -= 1
                elif sum > 0: # If sum is too big
                    r -= 1 # Make sum smaller (sorted arr)
                else: # If sum too small
                    l += 1 # Make sum bigger (sorted arr)
                
        return ans





my_solution = Solution()
print(my_solution.threeSum([-1,0,1,2,-1,-4]))
print(my_solution.threeSum([0,1,1]))
print(my_solution.threeSum([0,0,0]))
