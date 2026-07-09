# 33. Search in Rotated Sorted Array

# Topics: Array, Binary Search

# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

# Example 3:
# Input: nums = [1], target = 0
# Output: -1

class Solution(object):
    def search(self, nums, target):
        """
        - TC: O(log n) -> search space is halved each iteration
        - SC: O(1)
        """
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target: # Found it
                return mid
            
            # Step 1: Find which side is sorted
            # Step 2: See if target falls in sorted half
            if nums[l] <= nums[mid]: # Left half is sorted (<=, not < — when 2 elements remain l and mid are equal)
                if nums[l] <= target < nums[mid]: # Target in left half? (<= on l, < on mid)
                    r = mid - 1
                else:
                    l = mid + 1
            
            else: # Right half is sorted
                if nums[mid] < target <= nums[r]: # Target in right half? (< on mid, <= on r)
                    l = mid + 1
                else:
                    r = mid - 1
        
        return -1

"""
- In rotated arrays, you can't just compare target to mid (rotation breaks ordering).
- Example: [4,5,6,7,0,1,2], target=0, mid=7 → 0<7 suggests "go left" but target is right!
- SOLUTION: One half is always sorted. by finding which side is sorted (not sorting the array, just identifying the sorted half), we can:
    - Reliably check if target falls within that sorted range
    - Make a confident decision about which direction to search
    - Update our pointers correctly
"""

# TWO ELEMENT EDGE CASE: use <= on sorted half check (nums[l] <= nums[mid])
# when 2 elements remain, l and mid point to the same index so nums[l] == nums[mid]
# using < would make the condition False and misroute to the else branch

# BOUNDARY RULE: < on mid, <= on everything else
# mid gets < because target == mid is already handled above
# l and r get <= because target could equal either boundary



my_solution = Solution()
print(my_solution.search([4,5,6,7,0,1,2], 0)) # 4
print(my_solution.search([4,5,6,7,0,1,2], 3)) # -1
print(my_solution.search([1], 0)) # -1
print(my_solution.search([4,5,6,0,1,2,3], 5)) # 1
print(my_solution.search([8,1,2,3], 3)) # 3