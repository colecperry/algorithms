from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0
        for num in num_set:
            curr_len = 0
            if (num - 1) not in num_set:
                while num in num_set:
                    curr_len += 1
                    num += 1
            
            max_len = max(max_len, curr_len)
        
        return max_len
    
sol = Solution()
print(sol.longestConsecutive([100,4,200,1,3,2])) # 4