# 53. Maximum Subarray

# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

# Example 2:
# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.

# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

nums1 = [-2,1,-3,4,-1,2,1,-5,4]
nums2 = [1]
nums3 = [5,4,-1,7,8]

class Solution(object):
    def maxSubArray(self, nums): # Uses Kadane's algo
        """
        - TC: O(n)
        - SC: O(1)
        """
        maxSub = nums[0] # Set max subarray to the first value
        curSum = 0 # Create variable to track current sum

        for n in nums: # Iterate through nums
            if curSum < 0: # If the current sum ever becomes negative
                curSum = 0 # Reset current sum to zero
            curSum += n # Update current sum
            maxSub = max(maxSub, curSum) # Update max sub to max of itself and current sum

        return maxSub


    # Brute Force
    def maxSubArray3(self, nums):
        largest = nums[0] # Assume first ele is the largest
        for i in range(len(nums)): # Loop through array
            sum = nums[i] # Each loop, reset the sum to the next next ele in nums
            largest = max(largest, sum) # Consider if the num itself is the largest subarr
            for j in range(i+1, len(nums)): # Create a loop starting at i + 1
                sum = sum + nums[j] # Calculate the running sum (prev + next num)
                largest = max(largest, sum) # Update largest if bigger sum found
        return largest
    
my_solution = Solution()
print(my_solution.maxSubArray(nums1))
print(my_solution.maxSubArray2(nums2))
print(my_solution.maxSubArray3(nums3))