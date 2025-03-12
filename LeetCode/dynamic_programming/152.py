# 152 - Maximum Product Sub Array

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

# How to Solve: Brute Force O(n^2) -> gets time limit exceeded
# Initialize a largest variable, which holds the largest sum, which we initally assume is the first number in the array (a sub array can be 1 element)
# Iterate over the array
    # Update the product -> If the next number (a single element) is larger than the current largest sub array, update largest
    # Iterate over each element starting at i+1
    # Calculate the product by multiplying the current product with the new number
    # If the new product is greater than the largest product, update largest

# How to solve (optimal):
# Big Idea : On each iteration, we are going to have the max and min sub array values for all of the elements that came before it and update the values with the next element, updating our result if we find something bigger

# Start by taking the maximum and minimum products of the subarray of the first two elements and store in variables (create variables currMax and currMin and initialize them to 1, and multiply by the first element)
# As we move to the next number, multiply the next element by the minimum and maximum products of the subarray so far and store the maximum and minimum products for that specific element which includes the possibility of the number itself (we don't know which combination is going to produce the biggest result, since we are dealing with negatives)
# Edge case: If we have a zero in our array, it's going to make the min and max products, zero, and even if we continue on to positive or negative numbers after, anything * 0 = 0
    # We need to reset our max and min to 1

# Example: 
# arr = [-1, -2, -3, 4]
# arr [-1, -2] -> max = 2, min = -2
# arr[-1, -2, -3] -> max = 2 * -3 = 6, min =  -2 * 3 = -6
# arr[-1, -2, -3, 4] -> max = 6 * 4 = 24, min = -6 * 4 = -24
# ans = 24 


class Solution(object):
    def maxProduct(self, nums):
        res = max(nums) # Set res initially to max num in arr
        curMin, curMax = 1, 1 # Store currentMin and currentMax
        for n in nums: # Iterate through input arr
            if n == 0: # If we hit 0
                curMin, curMax = 1,1 # Reset our min and max
                continue
            temp = curMax * n # Calculate curr max
            curMax = max(n * curMax, n * curMin, n) # The max will be either the num * curMin, curMax, or n itself
            curMin = min(temp, n * curMin, n) # Need to use temp since we reassigned curMax in code before
            res = max(res, curMax, curMin) # Take the max of the old res, or the new values we just calc'd
        return res


    def maxProduct2(self, nums):
        largest = nums[0]
        for i in range(len(nums)):
            product = nums[i]
            if product > largest:
                largest = product
            for j in range(i+1, len(nums)):
                product = product * nums[j]
                if product > largest:
                    largest = product
        return largest

my_solution = Solution()

nums1 = [2,3,-2,4]
nums2 = [-2,0,-1]

print(my_solution.maxProduct(nums1))
print(my_solution.maxProduct(nums2))