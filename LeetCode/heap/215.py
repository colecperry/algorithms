# 215. Kth Largest Element in an Array

# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?

# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5

# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4

import heapq

def findKthLargest(nums, k):
    """
    TC: 
        - Heapify is O(n)
        - Heappop() is log(n), worst case num of operations = n - k, when k = 1 that == n
        - Total TC is (O(n) log(n))
    SC:
        - O(1) -> we use original nums array as the heap
    """
    heapq.heapify(nums) # turn nums into a min heap

    # pop smallest ele off until length of min heap == k
    while len(nums) > k:
        heapq.heappop(nums)
    
    return nums[0] # root guarenteed to be kth largest



print(findKthLargest([3,2,1,5,6,4], 2))
print(findKthLargest([3,2,3,1,2,4,5,5,6], 4))
