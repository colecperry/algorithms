# 503. Next Greater Element II

# Topics: Array, Stack, Monotonic

# Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

# The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

# Example 1:
# Input: nums = [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2; 
# The number 2 can't find next greater number. 
# The second 1's next greater number needs to search circularly, which is also 2.

# Example 2:
# Input: nums = [1,2,3,4,3]
# Output: [2,3,4,-1,4]

from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
        Monotonic Stack Pattern: Find next greater element in circular array
        Stack stores indices in decreasing order of their values
        
        TC: O(n)
            - Outer loop: 2n iterations
            - Each element pushed once and popped once = 2n operations total
            - Amortized O(1) per iteration
        
        SC: O(n)
            - Stack can hold at most n indices (worst case: decreasing array)
            - Output array: O(n)
        """
        mono_stack = []  # Stack holds indices (not values)
        n = len(nums)
        output = [-1] * len(nums)  # Default: no greater element found

        # Iterate twice to handle circular nature
        for i in range(2 * n): 
            current_index = i % n  # Wrap around after first pass

            # Pop all indices whose values are smaller than current
            while mono_stack and nums[current_index] > nums[mono_stack[-1]]:
                idx = mono_stack.pop()  # Index waiting for next greater element
                output[idx] = nums[current_index]  # Found it!
        
            # Only push during first pass (avoid duplicates)
            if i < n:
                mono_stack.append(current_index)  # Wait for next greater element
        
        return output
    
sol = Solution()
print(sol.nextGreaterElements([1,2,1])) #[2,-1,2]
print(sol.nextGreaterElements([1,2,3,4,3])) #[2,3,4,-1,4]