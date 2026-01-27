from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2 # calc mid index
            if nums[mid + 1] > nums[mid]: # Peak to the right of mid
                l = mid + 1
            else: # peak to the left
                r = mid # at peak now or peak to the left
        
        return l


    
sol = Solution()
print(sol.findPeakElement([1,2,3,1])) # 2
print(sol.findPeakElement([1,2,1,3,5,6,4])) # 5
