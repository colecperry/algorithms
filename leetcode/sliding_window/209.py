# 209. Minimum Size Subarray Sum

# Topics: Array, Sliding Window, Binary Search, Sliding Window

# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

# Example 1:
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

# Example 2:
# Input: target = 4, nums = [1,4,4]
# Output: 1

# Example 3:
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0

# Key Insight: 
    # This is a variable length sliding window problem -> the left and right pointers can continue to increase and shrink until they hit the end of the array
    # We want to keep increasing the window size with the R pointer until the sum is greater than the target, and then shrink from the left as much as possible while the sum is greater than or equal to the target to find the smallest window possible
    # In this case, we want to use a while loop inside a for loop because if we use a if/elif/else inside a for loop we can only shrink the window from l once per iteration

from typing import List

class Solution:
    """
    - TC: O(n): Each element is added to the sliding window once when r reaches it, and removed at most once when l passes it, O(2n) -> O(n)
    - SC: O(1) - No extra data structures needed
    """
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0 # Left sliding window pointer
        min_len = float('inf') # Keep track of the minimum subarr len
        curr_sum = 0 # Track the current sum of nums between R and L ptrs
        for r in range(len(nums)):
            curr_sum += nums[r] # Keep adding until window sum >= target
            while curr_sum >= target: # Keep shrinking window
                min_len = min(r - l + 1, min_len) # (r - l + 1) is count b/t 2 ele's
                curr_sum -= nums[l] # Decrease the sum by left element
                l += 1 

        return 0 if min_len == float('inf') else min_len # If the window never gets bigger than the sum, min_sub_arr will end up as inf, so return 0
        
sol = Solution()
print(sol.minSubArrayLen(7, [2,3,1,2,4,3])) # 2
print(sol.minSubArrayLen(4, [1,4,4])) # 4
print(sol.minSubArrayLen(11, [1,1,1,1,1,1,1,1])) # 0