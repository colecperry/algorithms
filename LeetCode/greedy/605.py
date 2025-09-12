# 605. Can Place Flowers

# Topics: Array, Greedy

# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

# Example 1:

# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
# Example 2:

# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false

from typing import List

"""
Problem: Can Place Flowers (LeetCode 605)

High-level approach:
1. Iterate through flowerbed and greedily plant flowers
2. Can plant at position i if: flowerbed[i] == 0 AND both neighbors are empty
3. Use boundary conditions for first/last positions (treat as empty)
4. Early termination when n flowers planted

Why greedy works:
- Planting early never hurts future opportunities
- If greedy fails, no strategy will work

Time Complexity: O(n) - single pass through array
Space Complexity: O(1) - only constant extra variables
"""

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0: # Edge case for placing zero flowers
            return True
        if not flowerbed:
            return False
            
        for i in range(len(flowerbed)): # loop through every spot
            if flowerbed[i] == 0:
                # Check if left neighbor is empty (if at left boundary -> True)
                left_empty = (i == 0) or (flowerbed[i-1] == 0)
                # Check if right neighbor is empty (if at right boundary -> True) 
                right_empty = (i == len(flowerbed)-1) or (flowerbed[i+1] == 0)
                
                if left_empty and right_empty: # if 
                    flowerbed[i] = 1
                    n -= 1
                    if n == 0: # early stopping condition
                        return True
        
        return n == 0

sol = Solution()
print(sol.canPlaceFlowers([1,0,0,0,1], 1)) # True
print(sol.canPlaceFlowers([1,0,0,0,1], 2)) # False