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

class Solution:
    """
    NOTE: Cannot use sliding window because numbers in the array can be negative
    (negative numbers mean window sum doesn't grow monotonically)
    """
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        - TC: O(n) - single pass through array
        - SC: O(n) - store at most n prefix sums
        """
        res = 0  # Count of subarrays that sum to k
        curSum = 0  # Running prefix sum
        prefixSums = {0: 1}  # Base case: handles subarrays starting from index 0
                            # (when curSum == k, diff will be 0)
        
        for num in nums:
            curSum += num  # Update running sum
            
            # Check if (curSum - k) exists in map
            # If yes: there's a previous prefix where removing it gives us sum k
            # Example: curSum=5, k=3 → diff=2 → if sum=2 seen before, the subarray from (right after that point to now) = 3
            diff = curSum - k
            
            # Add count of how many times diff appeared (found that many subarrays), + 0 if none
            res += prefixSums.get(diff, 0)
            
            # Store/update current prefix sum frequency
            prefixSums[curSum] = prefixSums.get(curSum, 0) + 1
        
        return res

# Example trace:
# nums = [1,1,1], k = 2
#
# prefixSums = {0: 1}
#
# i=0, num=1:
#   curSum = 1
#   diff = 1 - 2 = -1
#   -1 not in prefixSums, res = 0
#   prefixSums = {0: 1, 1: 1}
#
# i=1, num=1:
#   curSum = 2
#   diff = 2 - 2 = 0
#   0 in prefixSums! (appears 1 time), res = 0 + 1 = 1
#   (Found subarray [1,1] from index 0-1)
#   prefixSums = {0: 1, 1: 1, 2: 1}
#
# i=2, num=1:
#   curSum = 3
#   diff = 3 - 2 = 1
#   1 in prefixSums! (appears 1 time), res = 1 + 1 = 2
#   (Found subarray [1,1] from index 1-2)
#   prefixSums = {0: 1, 1: 1, 2: 1, 3: 1}
#
# Return res = 2

sol = Solution()
print(sol.subarraySum([1,1,1], 2))  # 2
print(sol.subarraySum([1,2,3], 3))  # 2
