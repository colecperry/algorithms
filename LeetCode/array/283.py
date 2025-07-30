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

# High Level Solution (Overwrite then fill with zeros): 
    # Move all zeros in the list to the end while maintaining the relative order of non-zero elements
    # Use a two-pass approach: one pass to copy non-zeros forward, one pass to fill remaining with zeros

    # 1. Initialize a pointer `insert_pos` to track where the next non-zero element should go
    # 2. Loop through all elements in the array:
    #    - If the current element is non-zero, write it at `insert_pos` and increment `insert_pos`
    # 3. After processing all non-zeros, loop from `insert_pos` to the end of the array:
    #    - Fill each of those positions with 0

# Time complexity: O(n) - we iterate through the list twice, each in O(n)
# Space complexity: O(1) - in-place modification with no extra space used


from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None: # Overwrite then fill with zero's version
        """
        Do not return anything, modify nums in-place instead.
        """
        insert_pos = 0 # ptr to place next non zero ele

        for num in nums: # move all non-zero ele's fwrd
            if num != 0: # if num is not == 0
                nums[insert_pos] = num # insert it at next ins pos
                insert_pos += 1

        while insert_pos < len(nums): # fill rest w/ 0's -> ins pos to len(ums)
            nums[insert_pos] = 0
            insert_pos += 1
        
        return nums
    
    # High Level (one pass swap): 
        # Move all zeros to the end while maintaining the relative order of non-zero elements
        # Use two pointers: one to track where the next non-zero should go, one to scan the list

        # 1. Initialize `slow` pointer to 0 to track the next position for a non-zero
        # 2. Loop through the array using `fast` pointer:
        #    - If nums[fast] is non-zero, swap it with nums[slow] and increment `slow`
        #    - This ensures non-zeros are moved to the front, and zeros are pushed back
        # 3. Swapping also keeps the relative order of non-zero elements

    # Time complexity: O(n) - each element is visited once
    # Space complexity: O(1) - in-place swaps with no extra space used

    
    def moveZeroes2(self, nums: List[int]) -> None: # Swap version
        slow = 0 # first ptr tracks where non zero will go
        for fast in range(len(nums)): # second ptr
            if nums[fast] != 0: # when we find a non-zero element
                nums[slow], nums[fast] = nums[fast], nums[slow] # push it back to slow ptr's pos
                slow += 1 # move slow ptr's pos forward
        
        return nums
    
sol = Solution()
print(sol.moveZeroes2([0,1,0,3,12])) # [1,3,12,0,0]
print(sol.moveZeroes([0])) # [0]