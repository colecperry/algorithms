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

# Tips to solve search2:
    # Base case: if middle == target return middle

    # Check if the middle is in the left sorted portion (middle >= left)
        # If target is >= L and <= Middle -> Search Left
        # Else search Right
        # Update pointers
    # Else (middle is in right sorted portion)
        # If target >= Middle and <= R -> Search Right
        # Else search left
        # Update pointers


nums1 = [4,5,6,7,0,1,2]
target1 = 0

nums2 = [4,5,6,7,0,1,2]
target2 = 3

nums3 = [1]
target3 = 0

nums4 = [5,1,3]
target4 = 5

nums5 = [3,4,5,6,7,0,1,2]
target5 = 1

class Solution(object):
    def search(self, nums, target):
        l = 0
        r = len(nums) - 1

        while l <= r: # Create while loop
            mid = (l + r) // 2 # Find the middle point of l and r pointers
            if nums[mid] == target: 
                return mid
            
            # Check if the left half is sorted
            if nums[l] <= nums[mid]: 
                if nums[l] <= target < nums[mid]: # Check if the target is in the left side half
                    r = mid - 1 # If the target is in the left side half, move r one left of the middle
                else:
                    l = mid + 1 # If the target is not in the left side half, move l one right of the middle
            else: # The right half is sorted
                if nums[mid] < target <= nums[r]: # If the target is in the right side
                    l = mid + 1 # Move the left pointer one right of the middle
                else: # If the target is not in the right side
                    r = mid - 1 # Move the right pointer one left of the middle
        return -1 # If you don't find the target, return -1




my_solution = Solution()
print(my_solution.search(nums1, target1))
print(my_solution.search(nums2, target2))
print(my_solution.search(nums3, target3))
print(my_solution.search(nums4, target4))
print(my_solution.search(nums5, target5))