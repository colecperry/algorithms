# 875. Koko Eating Bananas

# Topics: Array, Binary Search

# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.

# Example 1:
# Input: piles = [3,6,7,11], h = 8
# Output: 4

# Example 2:
# Input: piles = [30,11,23,4,20], h = 5
# Output: 30

# Example 3:
# Input: piles = [30,11,23,4,20], h = 6
# Output: 23

# KEY INSIGHT: Instead of searching in a given array, search the range of possible answers and use a helper function to test if each candidate works. Find the minimum value that satisfies the constraint.

# Pattern:
#     1. Define answer range [min_possible, max_possible]
#     2. Write helper function to test if candidate answer works
#     3. Binary search: if works, try smaller; if doesn't work, try larger

# 1. SEARCH SPACE SETUP:
#   - Min speed = 1 (can't eat 0 bananas/hour)  
#   - Max speed = max(piles) (eating faster won't help - still 1 hour per pile minimum)

# 2. FEASIBILITY FUNCTION:
#   - For each pile: time = ceil(pile_size / speed) 
#   - Total time = sum of all pile times
#   - Speed works if total_time <= h

# 3. BINARY SEARCH LOGIC:
#   - If current speed works: save it, try slower (right = mid - 1)
#   - If current speed fails: try faster (left = mid + 1)
#   - We want the MINIMUM speed that works

# Time Complexity: O(n * log(max(piles)))
    # - Binary search on answer space [1, max(piles)] takes O(log(max(piles))) iterations since
    #   we are not searching through an array, we are searching through possible speed values
    # - Binary search complexity = O(log(search_space_size))
    # - Each iteration calls helper function that loops through all n piles
    # - Total: O(n * log(max(piles)))

# Space Complexity: O(1)
    # - Only using constant extra variables, no additional data structures


import math

def min_eating_speed(piles, h):  # LC 875

    def can_finish(speed):
        total_hours = 0
        for pile in piles:
            total_hours += math.ceil(pile / speed)
        return total_hours <= h

    left, right = 1, max(piles)  # Starting answer space: 
    result = right # min speed starts at the largest possible pile so she can finish each pile in one hour

    while left <= right:
        mid = left + (right - left) // 2
        if can_finish(mid):  # Check if this speed works
            result = mid     # Save this answer
            right = mid - 1  # Try to find smaller speed
        else:                # This speed too slow
            left = mid + 1   # Need faster speed
            
    return result

# Test cases
print(min_eating_speed([3,6,7,11], 8))  # 4
print(min_eating_speed([30,11,23,4,20], 5))  # 30
print(min_eating_speed([30,11,23,4,20], 5)) # 6