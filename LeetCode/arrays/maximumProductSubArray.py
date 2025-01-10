# Given an integer array nums, find a subarray that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

nums1 = [2,3,-2,4]
nums2 = [-2,0,-1]

class Solution(object):
    def maxProduct(self, nums):
        largest = nums[0]
        for i in range(len(nums)):
            product = nums[i]
            for j in range(i+1, len(nums)):
                product = product * nums[j]
                if product > largest:
                    largest = product
        return largest

my_solution = Solution()
print(my_solution.maxProduct(nums1))
print(my_solution.maxProduct(nums2))