from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0
        while l < r:
            curr_width = r - l
            curr_height = min(height[l], height[r])
            curr_area = curr_width * curr_height
            max_area = max(curr_area, max_area)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        
        return max_area
    
sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))