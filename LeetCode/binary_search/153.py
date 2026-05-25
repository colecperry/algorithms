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



class Solution(object):
    def findMin(self, nums):
        """
        - TC: O(log n) -> search space is halved each iteration
        - SC: O(1)
        """
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2

            # Compare mid against r, not l: r is a stable anchor that never crosses the inflection point, while l can shift into the sorted right portion
            if nums[mid] < nums[r]: # mid is in the right (sorted) portion
                r = mid             # min is at or left of mid, keep mid as candidate
            else:                   # mid is in the left (sorted) portion
                l = mid + 1         # mid is above the inflection point, min must be to right

        # l and r have converged on the inflection point — the minimum
        return nums[l]


my_solution = Solution()
print(my_solution.findMin([3,4,5,1,2]))
print(my_solution.findMin([4,5,6,7,0,1,2]))
print(my_solution.findMin([11,13,15,17]))
