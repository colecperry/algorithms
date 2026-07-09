# 2099. Find Subsequence of Length K With the Largest Sum

# You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the largest sum.

# Return any such subsequence as an integer array of length k.

# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

# Example 1:
# Input: nums = [2,1,3,3], k = 2
# Output: [3,3]
# Explanation:
# The subsequence has the largest sum of 3 + 3 = 6.

# Example 2:
# Input: nums = [-1,-2,3,4], k = 3
# Output: [-1,3,4]
# Explanation: 
# The subsequence has the largest sum of -1 + 3 + 4 = 6.

# Example 3:
# Input: nums = [3,4,3,3], k = 2
# Output: [3,4]
# Explanation:
# The subsequence has the largest sum of 3 + 4 = 7. 
# Another possible subsequence is [4, 3].

from typing import List
import heapq

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]: # Max Heap Solution
        """
        TC:
            - Build heap: Iterate through nums O(n) & heappush O(log n): O(n log n)
            - Extract k elements: O(k) iterations x O(log n) per heappop = O(k log n)
            - Sort k indicies: O(k log k)
            - Since k ≤ n, total TC dominated by O(n log n)
            - Note -> heapop and heappush depend on n since the heap has n ele's, and not k in all cases

        SC:
            - Store nums in max heap -> O(n)
            - Store k ele indicies -> O(k)
            - Sort k ele indicies (timsort) -> O(k)
            - Total: O(n)
        """
        # Build max heap with (negative_value, index)
        max_heap = []
        for i in range(len(nums)):
            heapq.heappush(max_heap, (-nums[i], i))
        
        # Extract k largest ele & collect their indices
        indices = []
        for _ in range(k):
            val, idx = heapq.heappop(max_heap)
            indices.append(idx)
        
        # Sort indices to preserve original order
        indices.sort()
        
        # Build result array in original order
        return [nums[i] for i in indices]
    
    def maxSubsequence2(self, nums: List[int], k: int) -> List[int]: # Min Heap Solution
        """
        TC
            - Build min heap
                - Iterate through nums -> (O(n))
                - heappush, heappop on heap of size k -> O(log k))
                - total TC: O(n log k)
            - Sort the heap of size k: O(k log k)
            - Build output array: O(k)
            - Total: O(n log n) dominates
        SC
            - Store k ele in min heap: O(k)
            - Store k ele in output arr: O(k)
            - Total: O(k)
        """
        # Keep only k largest elements using min heap
        min_heap = []
        for i, num in enumerate(nums):
            if len(min_heap) < k: # Fill heap until we have k elements
                heapq.heappush(min_heap, (num, i))
            elif num > min_heap[0][0]: # Replace smallest if curr is larger
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, (num, i))

        # Sort by original index to preserve order
        min_heap.sort(key=lambda x: x[1])

        # Extract values in original order
        output = []
        for num, index in min_heap:
            output.append(num)
        return output
    
sol = Solution()
print(sol.maxSubsequence2([2,1,3,3], 2))
print(sol.maxSubsequence([-1,-2,3,4], 3))