# 152 - Maximum Product Sub Array

# Given an integer array nums, find a subarray that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

# Example 1:
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

# Example 2:
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


class Solution:
    def maxProduct(self, nums):
        """
        LC 152 - Maximum Product Subarray
        
        Key insight: Track BOTH max and min products ending at each position
        Why? Negative numbers flip max ↔ min
        
        TC: O(n) - single pass through array
        SC: O(1) - only tracking a few variables
        """
        # Max and min products can only initially be the first number
        max_product = nums[0]  # Best product ending here
        min_product = nums[0]  # Worst product ending here
        result = nums[0]       # Overall best answer
        
        # Process each element starting from index 1
        for i in range(1, len(nums)):
            curr = nums[i] # get current number
            
            # Save old max before we update (needed for min calculation)
            temp_max = max_product
            
            # New max is the LARGEST of:
            # 1. Start fresh at current number
            # 2. Extend previous max (prev max * curr number)
            # 3. Extend previous min (prev min * curr number)
            max_product = max(curr, temp_max * curr, min_product * curr)
            
            # New min is the SMALLEST of:
            # 1. Start fresh at current number
            # 2. Extend previous max (prev max * curr number)
            # 3. Extend previous min (prev min * curr number)
            min_product = min(curr, temp_max * curr, min_product * curr)
            
            # Update global result
            result = max(result, max_product)
        
        return result


# ═══════════════════════════════════════════════════════════════════
# TRACE: maxProduct([2, 3, -2, -5])
# ═══════════════════════════════════════════════════════════════════
# 
# Initial: max_product=2, min_product=2, result=2
# 
# i=1 (curr=3):
#   temp_max = 2
#   max_product = max(3, 2*3=6, 2*3=6) = 6
#   min_product = min(3, 2*3=6, 2*3=6) = 3
#   result = max(2, 6) = 6
#   State: max=6, min=3
# 
# i=2 (curr=-2):
#   temp_max = 6
#   max_product = max(-2, 6*-2=-12, 3*-2=-6) = -2
#   min_product = min(-2, 6*-2=-12, 3*-2=-6) = -12  ← Keep this!
#   result = max(6, -2) = 6
#   State: max=-2, min=-12
# 
# i=3 (curr=-5):
#   temp_max = -2
#   max_product = max(-5, -2*-5=10, -12*-5=60) = 60  ← min*negative flipped!
#   min_product = min(-5, -2*-5=10, -12*-5=60) = -5
#   result = max(6, 60) = 60
#   State: max=60, min=-5
# 
# 🎯 FINAL ANSWER: 60 (subarray [2,3,-2,-5])
# ═══════════════════════════════════════════════════════════════════

sol = Solution()
print(sol.maxProduct([2,3,-2,4])) # 6
print(sol.maxProduct([-2,0,-1])) # 0