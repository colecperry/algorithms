# 347. Top K Frequent Elements

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

# Example 3:
# Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
# Output: [1,2]

from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = Counter(nums) # Dict -> Num: Count
        # Sort dict by count -> returns a sorted list of the keys
        sorted_dict = sorted(my_dict, key=lambda x: my_dict[x], reverse=True) 
        res = []
        for num in sorted_dict[:k]:
            res.append(num)
        
        return res

sol = Solution()
print(sol.topKFrequent([1,1,1,2,2,3], 2)) # [1,2]
print(sol.topKFrequent([1], 1)) # [1]
print(sol.topKFrequent([1,2,1,2,1,2,3,1,3,2], 2)) # [1,2]