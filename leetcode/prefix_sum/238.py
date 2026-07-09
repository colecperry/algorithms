# 238. Product of Array Except Self

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

# nums = [1,2,3,4]

# How to solve:
    # BIG IDEA: Create prefix and postfix array. The prefix element at any given index represents the product of that element and all of those before it, and the postfix element represents the product of that element and any of those that come after it. Create a final output array by multiplying these values together for each index.
    # Prefix array loop: Initialize the prefix variable to 1 (only on first loop). Store the prefix variable in the prefix output array. Update the prefix variable by multiplying the it with the current element in nums before moving to the next index.
    # Postfix array loop (going backwards): Initialize the postfix array variable to 1 (only on first loop). Store the postfix variable in postfix output array. Update the postfix variable by mutiplying it with the current element in nums before moving to the next index.
    # For each index in prefix and postfix output array, mutiply the values together and store in a final output array.

    # Another way to solve without using the prefix and postfix array (reccomended)
    # BIG IDEA: Create an output array, loop through forwards and store the prefix value (all the elements before it multiplied together) in your output array. Then loop through backwards, and mutiply the postfix value (all the elements after multiplied) to each value in the output array (holding the prefix value) to give you the final answer.

    # Loop 1:
    # Initialize a prefix variable to 1 (Since the prefix of 1 is 1)
    # Store a 1 as the first element in the output array.
    # Multiply the first element in the nums array by the prefix to update the prefix number.
    # Move to the second element in the nums array and store the current prefix in the second index of the output array. Multiply the current prefix by the current element in num to update the prefix variable.
    # Move to the third element in the nums arrary and store the current prefix in the third index of the output array. Multiply the current prefix by the current element in num to update the prefix variable.
    # Continue the loop until you run out of spots in the output array

    # Loop 2:
    # Initialize the postfix variable to 1
    # Multiply the postfix variable by the current element in the output array and replace the value
    # Update the postfix variable by multiplying the postfix variable by the current element in the nums array 
    # Move to the second to last variable
    # Take the postfix variable, mutiply it by the current element in the output array and replace the element in the output array with the new value
    # Update the postfix variable by mutiplying the postfix variable by the current element in the nums array
    # Continue until there are no more values to update

nums = [1,2,3,4]
nums2 = [-1,1,0,-3,3]


class Solution(object):
    def productExceptSelf(self, nums):
        res = [1] * (len(nums))

        # Prefix product
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix = prefix * nums[i]

        # Postfix product
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):  # Fix range to go backwards
            res[i] = res[i] * postfix
            postfix = postfix * nums[i]

        return res


my_solution = Solution()
print(my_solution.productExceptSelf(nums))
print(my_solution.productExceptSelf(nums2))


