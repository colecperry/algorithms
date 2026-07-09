# 628. Maximum Product of Three Numbers

# Topics: Array, Math, Sorting

# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

# Example 1:

# Input: nums = [1,2,3]
# Output: 6
# Example 2:

# Input: nums = [1,2,3,4]
# Output: 24
# Example 3:

# Input: nums = [-1,-2,-3]
# Output: -6

# How to solve: (Brute Force) -> O(n^3)
    # Iterate over all possibilities of the three numbers, calculate the product, and update the max product if necessary

# How to solve: (Sorting) -> O(n log n)
    # If we sort the numbers in ascending order, we know that there are two options:
        # If all numbers are positive, the maximum product will be the product of the last three nums in the array
        # If not all numbers are positive, the max product will bt the product of the first two nums and the last num in the array

# How to solve: (Single scan) -> O(n + m)
    # 

class Solution(object):
    def maximumProductBruteForce(self, nums):
        n = len(nums)
        max_product = float('-inf')
        
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    max_product = max(max_product, nums[i] * nums[j] * nums[k])
        
        return max_product

    def maximumProductSorting(self, nums):
        nums.sort()
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])
    
    def maximumProductLinear(self, nums):
        max1 = max2 = max3 = float('-inf') # Initialize var's for largest 3 nums
        min1 = min2 = float('inf') # Initialize var's for smallest 2 nums
        
        for num in nums: # Loop through nums
            # Update max nums
            if num > max1: # If we find num larger than largest number (max1)
                max3, max2, max1 = max2, max1, num # set max3 to max2, max2 to max1, and max1 to that new largest num
            elif num > max2: # If we find num only larger than max2 (not larger than max1)
                max3, max2 = max2, num # set max3 to max2, and max2 to num
            elif num > max3: # If we find num only larger than max3 (not larger than max2 or max1)
                max3 = num # set max3 to that num
            
            # Update min values
            if num < min1: # If we find num smaller than the lowest num (min1)
                min2, min1 = min1, num # set min2 to min1, and min1 to the new lowest num
            elif num < min2: # If we find num only smaller than min2 and not min1
                min2 = num # set min2 to num
        
        return max(max1 * max2 * max3, min1 * min2 * max1) # Return the max of the two options




my_solution = Solution()
nums1, nums2, nums3 = [1,2,3], [1,2,3,4], [-1,-2,-3]
nums4 = [-100, 4, -1, -98, 3, 4]
# print(my_solution.maximumProductSorting(nums1))
# print(my_solution.maximumProductSorting(nums2))
# print(my_solution.maximumProductSorting(nums3))
print(my_solution.maximumProductLinear(nums4))

