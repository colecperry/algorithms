# 55. Jump Game

# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

# How it works:
# 1. Track maximum position we can reach at each step
# 2. If current position is beyond max reach, it's unreachable
# 3. Update max reach based on jump length at current position
# 4. Greedy works: always maximize reach, no benefit to stopping short

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool: # LC 55
        """
        - TC: O(n) - single pass through array
        - SC: O(1) - only track max reachable position
        """
        farthest = 0 # Track the farthest index we can reach
        
        # Check each position we can actually reach
        for i in range(len(nums)):
            # If current position is beyond our farthest reach, we're stuck
            if i > farthest:
                return False
            
            # Update the farthest position we can reach from here
            farthest = max(farthest, i + nums[i])
            
            # Early exit: if we can already reach the end
            if farthest >= len(nums) - 1:
                return True
        
        return True
    
    def canJump2(self, nums: List[int]) -> bool:
        # Our goal: can we reach the last index?
        goal = len(nums) - 1
        
        # Work backwards - if we can reach the goal from position i,
        # then position i becomes our new goal
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        # If our goal moved all the way back to index 0, we can make it
        return goal == 0

sol = Solution()
print("Can jump to end:", sol.canJump([2,3,1,1,4]))  # True
print("Can jump to end:", sol.canJump2([2,3,1,1,4]))  # True
print("Can jump to end:", sol.canJump([3,2,1,0,4]))  # False
print("Can jump to end:", sol.canJump2([3,2,1,0,4]))  # False