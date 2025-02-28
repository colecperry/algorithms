# 704. Binary Search

# Topics: Array, Binary Search

# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.


# Example 1:
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

# Example 2:
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1

# Runtime Complexity: O(log n)
# - The algorithm uses binary search, which repeatedly divides the search space by half.
# - Since the number of elements is reduced exponentially, the time complexity is logarithmic.

# Space Complexity: O(1)
# - The algorithm operates in-place with only a few integer variables (l, r, mid).
# - No additional memory is used that scales with input size.



def search(nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1

print(search([-1,0,3,5,9,12], 9))
print(search([-1,0,3,5,9,12], 2))