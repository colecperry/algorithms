# 189. Rotate Array

# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

# Example 1:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# Example 2:
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        TC: O(n): We touch each element twice
        SC: O(1): No extra data stuctures, fn calls do not create recursion depth
        
        NOTE: Rotating right by k is the same as:
        1. Reverse the entire array
        2. Reverse the first k elements
        3. Reverse the remaining elements
        """
        n = len(nums)
        k = k % n  # Handle k > n
        
        def reverse(start: int, end: int) -> None:
            """Reverse nums[start:end+1] in place"""
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        # Step 1: Reverse entire array
        reverse(0, n - 1)
        
        # Step 2: Reverse first k elements
        reverse(0, k - 1)
        
        # Step 3: Reverse remaining n-k elements
        reverse(k, n - 1)

sol = Solution()
print(sol.rotate([1,2,3,4,5,6,7], 3)) # [5,6,7,1,2,3,4]
print(sol.rotate([-1,-100,3,99], 2)) # [3,99,-1,-100]