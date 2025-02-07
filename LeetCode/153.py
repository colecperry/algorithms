# 153. Find Minimum in Rotated Sorted Array

# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

# Example 1:
# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.

# Example 2:
# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

# Example 3:
# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 

nums1 = [3,4,5,1,2]
nums2 = [4,5,6,7,0,1,2]
nums3 = [11,13,15,17]

# Tips to solve:
# Use binary search
# You have two sorted portions of the list, the left sorted portion and the right sorted portion due to the rotation
# If the middle value is in the left sorted portion, we want to recursively search the right side (the values in the left sorted portion always be greater than the values in the right sorted portion), and if the middle value is in the right sorted portion, we want to recursively search the left side 
# We can check if the middle value is in the left sorted portion by comparing it to the first value in the list
    # If the middle value is greater than the first value, it is in the left sorted portion
    # If the middle value is less than the first value, it is in the right sorted portion
# 


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0] # Create an arbitrary placeholder for the smallest element
        l = 0 # Create a left and right pointers, starting at the beginning and end of the list
        r = len(nums) - 1

        
        while l <= r: # Create a while loop
            if nums[l] < nums[r]: # Code only executes once our list is sorted (very left pointer less than very right)
                res = min(res, nums[l]) # Set the result to the min of the result and the left value
                break
        
        # If the list is not sorted
            m = (l + r) // 2 # Calculate the middle point
            res = min(res, nums[m]) # Update the result to be the minimum of the result and the middle
            if nums[m] >= nums[l]: # Check if the middle is part of the left sorted portion
                l = m + 1 # Move the left pointer over one to the left of the middle if the middle value is in the left sorted portion
            else:
                r = m - 1
    
        return res
    

class Solution(object):
    def findMin2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums)-1
        while l<r: 
            mid = l + (r - l)//2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]

nums1 = [3,4,5,1,2]
nums3 = [11,13,15,17]




my_solution = Solution()
print(my_solution.findMin(nums1))
print(my_solution.findMin(nums2))
print(my_solution.findMin(nums3))
