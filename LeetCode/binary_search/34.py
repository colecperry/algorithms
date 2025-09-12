# 34. Find First and Last Position of Element in Sorted Array

# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]

# Key insight: Use binary search twice with different behaviors when target is found.
    # For leftmost: continue searching left half after finding target to find earlier occurrence
    # For rightmost: continue searching right half after finding target to find later occurrence.

# Time Complexity: O(log n) - two binary searches
# Space Complexity: O(1) - only using constant extra space

class Solution(object):
    def searchRange(self, nums, target):
        def binary_search(find_left):
            left, right = 0, len(nums) - 1
            result = -1 # result if no target found
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target: # if we find target
                    result = mid
                    if find_left: # looking for leftmost pos
                        right = mid - 1 # keep searching left
                    else: # looking for rightmost pos
                        left = mid + 1 # keep searching right
                elif nums[mid] < target: # num we are on is less than the target
                    left = mid + 1 # search right
                else: # num we are on is greater than the target
                    right = mid - 1 # search left
            return result
        
        return [binary_search(True), binary_search(False)]
    
sol = Solution()
print(sol.searchRange([5,7,7,8,8,10], 8)) # [3, 4]
print(sol.searchRange([5,7,7,8,8,10], 6)) # [-1, -1]
print(sol.searchRange([], 0)) # [-1, -1]
