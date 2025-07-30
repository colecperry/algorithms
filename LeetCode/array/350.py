# 350. Intersection of Two Arrays II

# Topics - Array, Hash Table, Two Pointers, Binary Search, Sorting

# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.

# How to Solve: (Two Hashmaps)
    # Step 1: Create frequency maps (counters) for both input arrays
    # Step 2: Iterate over each unique element in nums1's counter
    # Step 3: If the element exists in nums2's counter, take the minimum frequency of the element from each hashmap
    # Step 4: Add that element to the output list the minimum number of times
    # Step 5: Return the output list containing the intersection of nums1 and nums2

    # Time Complexity: O(n + m)
    # - O(n) to build the Counter for nums1
    # - O(m) to build the Counter for nums2
    # - O(k) to iterate through keys in nums1's counter, where k <= n
    # So total time = O(n + m)

    # Space Complexity: O(n + m)
    # - O(n) for nums1_counter
    # - O(m) for nums2_counter
    # - O(min(n, m)) for the output list in the worst case (all elements overlap)

from collections import Counter
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]: # Two Dictionary Solution
        output = [] 
        nums1_counter = Counter(nums1)       
        nums2_counter = Counter(nums2)
        for key, val in nums1_counter.items():
            if key in nums2_counter:
                min_val = min(nums1_counter[key], nums2_counter[key])
                output.extend([key] * min_val)
        return output
    
    # How to Solve: (One Hashmap)

        # - Ensure the counter is built on the smaller array to minimize space usage:
        #     - If nums1 is larger than nums2, swap them so nums1 is always the smaller array.

        # - Build a frequency counter (hash map) of nums1 elements.

        # - Initialize an empty result list to store the intersection elements.

        # - Loop through each number in nums2:
        #     - If the number exists in the counter with count > 0:
        #         - Add the number to the result list.
        #         - Decrement its count in the counter to correctly account for duplicates.

        # - Return the result list containing the intersection of nums1 and nums2.

    # Time Complexity: O(N + M), where N and M are the lengths of nums1 and nums2.
    # Space Complexity: O(min(N, M)), for the hash map storing counts of the smaller array.

    
    def intersect2(self, nums1, nums2): # One Dictionary Solution
        # Always build counter on the smaller array for efficiency
        if len(nums1) > len(nums2): # If len of nums1 is greater
            nums1, nums2 = nums2, nums1 # Swap with nums2 to get smaller array

        count = Counter(nums1)  # count elements in nums1
        result = []

        for num in nums2: # Loop through larger arr
            if count[num] > 0:  # if num is in nums1 and still has count left
                result.append(num) # append to the res
                count[num] -= 1 # decrease the count

        return result
    
    # High-Level Idea:
        # Use two pointers to traverse both sorted arrays and collect common elements.
        # Sorting both arrays ensures we can scan them linearly to find intersections.
    
        # Step 1: Sort both arrays to allow for linear scanning with two pointers
        # Step 2: Initialize two pointers (i and j) for nums1 and nums2
        # Step 3: Traverse both arrays:
        #   - If elements match, append to output and advance both pointers
        #   - If num at pointer i is less, move that ptr forward 
        #   - Else, advance pointer j
        # Step 4: Continue until one pointer reaches the end of its array
        # Step 5: Return the list of intersecting elements

    # Time Complexity:
        # O(n log n + m log m) due to sorting both arrays (n = len(nums1), m = len(nums2))
        # O(n + m) for the while loop (each pointer moves at most once per element)

    # Space Complexity:
        # O(1) extra space if we ignore the output list (in-place pointer operations on input arrays)
        # O(k) for the output list where k is the number of intersecting elements
    
    def intersect3(self, nums1: List[int], nums2: List[int]) -> List[int]: # Sorting solution
        nums1.sort()  # O(n log n)
        nums2.sort()  # O(m log m)
        i = j = 0 # ptr 1 and ptr 2
        output = []
        
        while i < len(nums1) and j < len(nums2): # while both ptrs didn't hit the end
            if nums1[i] == nums2[j]: # if nums are ==
                output.append(nums1[i]) # append the num and move both ptrs
                i += 1
                j += 1
            elif nums1[i] < nums2[j]: # if the first ptr's num is less
                i += 1 # move that ptr forward
            else:
                j += 1 # move other ptr forward
        
        return output

sol = Solution()
print(sol.intersect2([1,2,2,1], [2,2])) # [2,2]
print(sol.intersect2([4,9,5], [9,4,9,8,4])) # [4,9]

