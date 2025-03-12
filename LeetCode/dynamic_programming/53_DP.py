# 53. Maximum Subarray

# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# How to solve (Brute Force)
    # Track the largest sum (assume first it is just the first element)
    # Loop through array
        # Update largest if the new number itself is larger
        # Use nested for loop with j from i + 1 to length of the array
            # Update the running sum (prev sum + new number)
            # If the new sum is larger than the old sum, update largest
        # Return largest

# How to Solve (Dynamic Programming):
    # Track the max sum (initialize as the largest single number in the array) -> 
    # Track the current max (used as we loop through the array)
    # Loop through the array
        # Update the current max to the max of the number we are on, or the number we are on plus the current max (either we start a new subarray with n, or we extend the previous subarray by adding n)
        # Update result if larger

    # Time complexity: O(n): we iterate through all numbers once
    # Space complexity: O(1): we only use two variables curMax and res

# How to Solve (sliding window):
    # Create variable to track max sum and current sum
    # Iterate through array
        # If the current sum is negative, reset it to zero (this is based on Kadane's algorithm, basically any negative current sum can only hurt our potential maximum sub array, so it will always be better to reset the current sum to zero and start fresh)
        # Update the current sum and the max sum




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
    # DP Solution
    def maxSubArray(self, nums):
        res = max(nums)
        curMax = 0

        for n in nums:
            curMax = max(n, curMax + n)
            res = max(res, curMax)

        return res
    
    # Sliding Window Solution
    def maxSubArray(self, nums):
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
print(my_solution.maxSubArray(nums2))
print(my_solution.maxSubArray(nums3))