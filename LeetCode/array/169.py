# 169. Majority Element

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

class Solution(object):
    """
    - TC: O(n) -> loop through nums array once
    - SC: O(1)
    - NOTE: This is the boyer-moore voting algorithm
    """
    def majorityElement(self, nums):
        # Phase 1: Find a candidate
        candidate = None
        count = 0
        
        for num in nums:
            if count == 0:  # Update candidate when count is 0
                candidate = num
            count += (1 if num == candidate else -1)
        
        # Whatever candidate is left is the majority
        return candidate



solution = Solution()
print(solution.majorityElement([3,2,3]))
print(solution.majorityElement([2,2,1,1,1,2,2]))
