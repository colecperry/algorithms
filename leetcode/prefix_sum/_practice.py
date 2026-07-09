# 560. Subarray Sum Equals K

# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

# Example 1:
# Input: nums = [1,1,1], k = 2
# Output: 2

# Example 2:
# Input: nums = [1,2,3], k = 3
# Output: 2

from typing import List
from collections import defaultdict

class Solution:
    """
    NOTE: Cannot use sliding window because numbers in the array can be negative
    (negative numbers mean window sum doesn't grow monotonically)
    """
    def subarraySum(self, nums: List[int], k: int) -> int: # O(n)^2
        n = len(nums)
        prefix_sum = [0] * (n+1)
        count = 0

        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]

        for i in range(len(prefix_sum) - 1, -1, -1):
            for j in range(i-1, -1, -1):
                diff = prefix_sum[i] - prefix_sum[j]
                if diff == k:
                    count += 1
        
        return count
    
    def subarraySum2(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        sum_freq = defaultdict(int)  # prefix sum : frequency
        sum_freq[0] = 1  # empty subarray base case
        count = 0

        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]
            count += sum_freq[prefix_sum[i+1] - k]  # how many valid subarr end here
            sum_freq[prefix_sum[i+1]] += 1  # add curr sum count to dict

        return count



sol = Solution()
print(sol.subarraySum2([1,1,1], 2))  # 2
print(sol.subarraySum2([1,2,3], 3))  # 2