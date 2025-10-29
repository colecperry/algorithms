
# LC 16 - 3Sum Closest (CLEANER for learning the pattern)

class Pattern5(object):
    """
    Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

    Return the sum of the three integers.

    You may assume that each input would have exactly one solution.

    Example 1:
    Input: nums = [-1,2,1,-4], target = 1
    Output: 2
    Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
    """
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        Pattern: Fixed + Two Converging (CLEANER VERSION)
        - Fix first element
        - Use two pointers for remaining two
        - NO duplicate handling needed!
        - Just track closest sum
        
        Time: O(n²), Space: O(1)
        """
        nums.sort() # Sort array (required for two pointer logic)
        closest_sum = float('inf')
        
        for i in range(len(nums) - 2): # Fix the first element
            left, right = i + 1, len(nums) - 1 # 2 ptrs for remaining
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # Update closest if this sum is closer to target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move ptrs based on whether sum too small or large
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum  # Exact match
        
        return closest_sum
    
sol = Pattern5()
print(sol.threeSumClosest([-1,2,1,-4], 1))