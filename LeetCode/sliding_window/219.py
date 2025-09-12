# 219 - Contains Duplicate II

# Topics = Array, Hash Table, Sliding Window

# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

# Example 1:
# Input: nums = [1,2,3,1], k = 3
# Output: true

# Example 2:
# Input: nums = [1,0,1,1], k = 1
# Output: true

# Example 3:
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false

# How to Solve: (Brute Force): O(n^2)
    # Iterate through nums from 0 to len(nums) - 1
        # Iterate through nums starting at l + 1 to l + k ensuring it does not go OOB (smaller input)
        # If the nums in the window are equal return True
    # If we iterate all the way through and don't find any duplicates, return False

# How to Solve: (Sliding Window): O(n)
    # Create a window using a set (to easily check for duplicates in O(1) time)
    # Initialize left pointer for beginning of window
    # Loop through array (iterator will be our right pointer)
        # Check if the window is greater than k -> if so, remove element at left pointer from the set, increment the left pointer (we need to do this first to ensure the window never exceeds k elements)
        # If the number is already in the set, that means we are in the window and we found a duplicate -> return True (now we know the window is properly sized from the first "if" statement)
        # Add the number at the right pointer to the window (insert only after we know there are no duplicates present)


class Solution(object):
    # Brute Force
    def containsNearbyDuplicate(nums, k):
        n = len(nums)

        for l in range(n):  # Left pointer (start of window)
            for r in range(l + 1, min(l + k + 1, n)):  # Right pointer (within k distance)
                if nums[l] == nums[r]:  # Check for duplicate
                    return True  # Found valid pair
            
        return False  # No duplicate found within range

    # Sliding Window
    def containsNearbyDuplicate2(self, nums, k):
        window = set() # Keep track of all values in our window
        L = 0 # Beginning of window

        for R in range(len(nums)): # End of window
            if R - L > k: # Check if our window is too large
                window.remove(nums[L]) # Remove element at left side of window
                L += 1 # Increment beginning of window

            if nums[R] in window: # If the num at R is in the window already
                return True # We found a duplicate
            
            window.add(nums[R]) # If the num is not already in the window, add it
            
        return False

my_solution = Solution()

nums1 = [1,2,3,1]
k1 = 3
print(my_solution.containsNearbyDuplicate2(nums1, k1))

nums2 = [1,0,1,1]
k2 = 1
print(my_solution.containsNearbyDuplicate2(nums2, k2))

nums3 = [1,2,3,1,2,3]
k3 = 2
print(my_solution.containsNearbyDuplicate2(nums3, k3))