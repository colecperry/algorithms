# 1011. Capacity To Ship Packages Within D Days

# A conveyor belt has packages that must be shipped from one port to another within days days.

# The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

# Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

# Example 1:
# Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
# Output: 15
# Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
# 1st day: 1, 2, 3, 4, 5
# 2nd day: 6, 7
# 3rd day: 8
# 4th day: 9
# 5th day: 10

# Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.

# Example 2:
# Input: weights = [3,2,2,4,1,4], days = 3
# Output: 6
# Explanation: A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
# 1st day: 3, 2
# 2nd day: 2, 4
# 3rd day: 1, 4

# Example 3:
# Input: weights = [1,2,3,1,1], days = 4
# Output: 3
# Explanation:
# 1st day: 1
# 2nd day: 2
# 3rd day: 3
# 4th day: 1, 1

"""
Binary Search on Answer Space - Find minimum ship capacity

IDEA: Search through possible capacity values (not array elements)
- Min capacity = heaviest package
- Max capacity = all packages combined
- Test each capacity: can we ship everything in D days?

WHY 'while left < right':
- We want the exact minimum capacity
- Loop stops when left == right (our answer)
- Avoids confusion about which pointer has the final answer

TIME COMPLEXITY: O(n * log(sum(weights) - max(weights)))
- Binary search range: max(weights) to sum(weights)
- Number of iterations: log(sum - max)
- Each iteration calls feasibility function: O(n) to check all packages
- Total: O(n) per iteration × O(log(range)) iterations = O(n * log(range))

SPACE: O(1) - only using variables for pointers and counters

STEPS:
1. Binary search on capacity values
2. For each capacity, simulate day-by-day packing
3. If it works, try smaller capacity. If not, try larger.
"""

from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def can_fit(capacity): # Feasibility function
            days_used = 1
            current_weight = 0
            
            for weight in weights:
                if current_weight + weight <= capacity:
                    current_weight += weight
                else:
                    # Start new day
                    days_used += 1
                    current_weight = weight
                    
                    # Early exit if we exceed allowed days
                    if days_used > days:
                        return False
            
            return days_used <= days
        
        left = max(weights)   # Ship must carry the heaviest package
        right = sum(weights)  # Worst case: ship all packages in one day
        
        while left < right:
            mid = left + (right - left) // 2 # gives us capacity per day for d days
            if can_fit(mid):
                right = mid      # This capacity works, try smaller
            else:
                left = mid + 1   # This capacity fails, need larger
        
        return left # when l == r, l will be pointed at the min possible capacity 
        
sol = Solution()
print(sol.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5)) # 15
print(sol.shipWithinDays([3,2,2,4,1,4], 3)) # 6
print(sol.shipWithinDays([1,2,3,1,1], 4)) # 3