# 643 - Maximum Average SubArray I

# Topics - Array, Sliding Window

# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

# Example 1:

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# Example 2:

# Input: nums = [5], k = 1
# Output: 5.00000

# How to Solve:
    # Calculate the sum of the first window using the sum function, and calculate the avg as a float
    # Iterate through the array starting at k
        # Instead of recalculating the entire sum each iteration, use a rolling sum by taking the previous sum, subtracting the number leaving the window, adding the number entering the window, and finding the new average
        # Update the max average sum

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        - TC: O(n) - iterate through nums once
        - SC: O(1)
        """
        window_sum = sum(nums[:k]) # Calc starting window sum
        max_avg = window_sum / float(k) # Find avg -> float
        l = 0

        for r in range(k, len(nums)): # Loop through rest of window
            window_sum += nums[r] - nums[l] # Add val entering window, subtract val leaving 
            l += 1
            max_avg = max(max_avg, window_sum / float(k)) # Update max average sum

        return max_avg


my_solution = Solution()

nums1 = [1,12,-5,-6,50,3]
k1 = 4
print(my_solution.findMaxAverage(nums1, k1))

nums2 = [5]
k2 = 1
print(my_solution.findMaxAverage(nums2, k2))