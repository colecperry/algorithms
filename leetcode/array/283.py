# 283. Move Zeroes

# Topics: Array, Two Pointers

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# Output: [0]


from typing import List

class Solution:
    """
    - Time complexity: O(n) - we iterate through the list twice, each in O(n)
    - Space complexity: O(1) - in-place modification with no extra space used
    """
    def moveZeroes(self, nums: List[int]) -> None: # Overwrite then fill with zero's version
        """
        Do not return anything, modify nums in-place instead.
        """
        write_pos = 0 # track a write pos to move non zero ele's forward

        for i in range(len(nums)): # move non zero ele's forward
            if nums[i] != 0:
                nums[write_pos] = nums[i]
                write_pos += 1

        for i in range(write_pos, len(nums)): # fill the rest of the arr with zero's
            nums[i] = 0

    
sol = Solution()
print(sol.moveZeroes2([0,1,0,3,12])) # [1,3,12,0,0]
print(sol.moveZeroes([0])) # [0]