# 162. Find Peak Element

# A peak element is an element that is strictly greater than its neighbors.

# Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

# You must write an algorithm that runs in O(log n) time.

# Note to self: nums[-1] in lc means index before the first ele, not the last ele like in python

# Example 1:
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.

# Example 2:
# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

def find_peak_element(nums):  # LC 162
    """    
    Key insight: Compare mid with neighbor to decide direction:
        - If nums[mid] < nums[mid + 1]: slope is increasing, peak guarenteed if we keep searching right because either one element goes down (peak found) or we hit OOB (ele at OOB is less than last ele)
        - If nums[mid] > nums[mid + 1]: slope is decreasing, peak guarenteed at mid or if we keep searching left because either one element goes up (peak found) or we hit OOB (ele at OOB is less than first ele)

    TC: O(log n) - eliminates half the search space each iteration
    SC: O(1) - only using pointer variables
    """
    left, right = 0, len(nums) - 1
    
    while left < right:  # Note: use < not <= for convergence to single answer
        mid = left + (right - left) // 2
        
        if nums[mid] < nums[mid + 1]:
            # We're on upward slope, peak must be to the right
            left = mid + 1
        else:
            # We're on downward slope, peak could be at mid or to the left  
            right = mid
    
    return left  # left == right, pointing to a peak

print(find_peak_element([1,2,3,1]))        # peak at index 2
print(find_peak_element([1,2,1,3,5,6,4]))  # peak at index 5

# Downward slope examples

print(find_peak_element([5,3,1]))          # peak at index 0
print(find_peak_element([1, 6, 4, 2]))     # peak at index 1
