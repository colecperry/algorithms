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
    def maxSubArray(self, nums):
        largest = nums[0] # Assume that the first element is the largest
        for i in range(len(nums)): # Create a loop using i that loops from index 0 to the end of the list
            sum = nums[i] # Each loop, reset the sum to the next index of i
            for j in range(i+1, len(nums)): # Create a loop using j that loops from index i+1 to the end of the list
                sum = sum + nums[j] # Calculate the sum (the sum is the previous sum plus the next num in the loop)
                if sum > largest: # If the sum is larger, set it to the largest variable
                    largest = sum
        return largest
    
my_solution = Solution()
print(my_solution.maxSubArray(nums1))
print(my_solution.maxSubArray(nums2))
print(my_solution.maxSubArray(nums3))