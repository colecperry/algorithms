# 35. Search Insert Position

# Topics: Array, Binary Search

# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order. You must write an algorithm with O(log n) runtime complexity.

# Example 1: Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2: Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3: Input: nums = [1,3,5,6], target = 7
# Output: 4

#  Binary Search
class Solution(object):
    """
    KEY INSIGHT: binary search ensures that the start ptr always ends up at the smallest index where the target could be inserted
    
    TC:
        - O(log n) -> binary search halves the search space each iteration
    SC:
        - O(1) - just pointers
    """
    def searchInsert(self, nums, target):
        start, end = 0, len(nums) - 1 # binary search ptrs
        while start <= end:
            middle = start + (end - start) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                start = middle + 1
            else:
                end = middle - 1
        return start
    
solution = Solution()
print(solution.searchInsert([1,2,3,4,5,6,7,8,9,10], 10))
