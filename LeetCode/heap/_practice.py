from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for _ in range(k):
            num = heapq.heappop(nums)

        return num

sol = Solution()
print(sol.findKthLargest([3,2,1,5,6,4], 2))
