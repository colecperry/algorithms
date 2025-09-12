# 15 - 3Sum

# Topics - Array, Two Pointers, Sorting

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# How to Solve:
    # 1. Sort the input list to enable the two‐pointer approach.
    # 2. Loop over each element as the “first” value of the triplet, skipping duplicates to avoid repeats.
    # 3. For each fixed element, initialize two pointers (left, right) at the ends of the remaining subarray.
    #    - If the sum of the three values is less than zero, move left pointer right to increase the sum.
    #    - If the sum is greater than zero, move right pointer left to decrease the sum.
    #    - If the sum equals zero, record the triplet, then advance the left pointer past any duplicates.
    # 4. Continue moving pointers until they cross, then proceed to the next fixed element.
    # 5. Return the list of all unique triplets that sum to zero.

    # Time Complexity: O(n^2) – the outer loop runs O(n) times and the two‐pointer scan takes O(n) each
    # Space Complexity: O(1) extra space (ignoring the output list)


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
            if i > 0 and a == nums[i-1]: # Don't go OOB on first iteration
                continue # Check for consecutive dups when iterating i, skip if dup found

            l,r = i + 1, len(nums) - 1 # Set two pointers
            while l < r: # Loop until they meet
                sum = a + nums[l] + nums[r] # calc sum from three pointers
                if sum > 0: # if the sum is greater than zero,
                    r -= 1 # make total sum smaller (since arr is sorted)
                elif sum < 0: # if the sum is less than zero
                    l += 1 # make the total sum bigger
                else: # if sum == 0
                    ans.append([a, nums[l], nums[r]]) 
                    l += 1 
                    while nums[l] == nums[l - 1] and l < r: # Keep shifting while there are duplicates,
                        l += 1 # then recalculate sum
                
        return ans
    

my_solution = Solution()
print(my_solution.threeSum([-1,0,1,2,-1,-4]))
print(my_solution.threeSum([0,1,1]))
print(my_solution.threeSum([0,0,0]))
print(my_solution.threeSum([-2,-1,-1,0,1,3])) # inner while loop gets triggered

