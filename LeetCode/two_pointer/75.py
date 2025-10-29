# 75. Sort Colors

# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

# Example 1:
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# Example 2:
# Input: nums = [2,0,1]
# Output: [0,1,2]

from typing import List

class Solution:
    """
    TC
        - O(n): Iterate through the nums arr twice - one for moving 0's to front and once to move 1's to middle
    SC
        - O(1): Just use a left pointer and swap in place
    """
    def sortColors(self, nums: List[int]) -> None:
        # Pass 1: Move all 0s to the left
        left = 0 # Insertion pointer
        for i in range(len(nums)):
            if nums[i] == 0: # If we find a zero
                # Swap 0's to insertion point at front
                nums[left], nums[i] = nums[i], nums[left] # swap
                left += 1 # Increment insertion ptr
        
        # Pass 2: Move all 1s to the middle (starting after 0s)
        for i in range(left, len(nums)): # Start ptr where left ended
            if nums[i] == 1: # If we find a one
                # Swap 1's to insertion point in middle
                nums[left], nums[i] = nums[i], nums[left] 
                left += 1 # Increment insertion pointer
        
        # 2s automatically end up at the right!
        
sol = Solution()

nums1 = [2,0,2,1,1,0]
sol.sortColors(nums1)
print(nums1)  # [0,0,1,1,2,2]

nums2 = [2,0,1]
sol.sortColors(nums2)
print(nums2)  # [0,1,2]