# 303. Range Sum Query - Immutable

# Given an integer array nums, handle multiple queries of the following type:

# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:

# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

# Example 1:

# Input
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
# Output
# [null, 1, -1, -3]

# Explanation
# NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
# numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
# numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
# numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3

from typing import List

class RangeSumQuery:
    """
    Problem: Given an int array, handle multiple sumRange(left, right) queries.

    Example:
        nums = [1, 2, 3, 4, 5]
        sumRange(0, 2) → 6    # [1,2,3]
        sumRange(1, 4) → 14   # [2,3,4,5]

    Steps:
    1. Build prefix where prefix[i] = sum(nums[0..i-1]), prefix[0] = 0
    2. sumRange(left, right) = prefix[right+1] - prefix[left]
         prefix[right+1] covers nums[0..right]
         prefix[left]    covers nums[0..left-1]
         Difference      = nums[left..right]
    """
    def __init__(self, nums: List[int]):  # LC 303 - Range Sum Query Immutable
        self.prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix[i + 1] = self.prefix[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        """
        Total TC: O(n) build + O(1) per query
        SC: O(1)
        """
        return self.prefix[right + 1] - self.prefix[left]

rsq = RangeSumQuery([-2, 0, 3, -5, 2, -1]) 
print(rsq.sumRange(0, 2))  
print(rsq.sumRange(2, 5))  
print(rsq.sumRange(0, 5))




