# 239. Sliding Window Maximum

# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.

# Example 1:
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

# Brute Force - O(k * (n-k)) TC
# For a sliding window size k, loop through the array n-k times, and for each iteration, take the max of that sliding window & append 

from typing import List
from collections import deque
import heapq

class Solution:
    """
    Steps:
    1. Maintain a deque of indices in decreasing order of their values
    2. For each index i:
       a. Remove front if it is outside the current window (i - deq[0] >= k)
       b. Remove all indices from back whose values < nums[i] (they can never be max)
       c. Append i to deque
       d. Once window is full (i >= k-1), record nums[deq[0]] as the window max
    """
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:  # LC 239
        """
        TC: O(n) - each index pushed and popped at most once
        SC: O(k) - deque stores at most k indices
        """
        result = []
        deq = deque()  # Stores indices, values in decreasing order

        for i in range(len(nums)):
            window_start = i - k + 1

            # front index fell out of the window -> drop it
            if deq and deq[0] < window_start:
                deq.popleft()

            # anything smaller than nums[i] can never be a future max -> drop it
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()

            # nums[i] is now a candidate max -> add its index
            deq.append(i)

            # window has reached size k -> front of deque is this window's max
            if i >= k - 1:
                result.append(nums[deq[0]])

        return result

    # Trace: nums=[1,3,-1,-3,5,3,6,7], k=3
    # i=0 (1):  deq=[0]
    # i=1 (3):  3>1 pop 0 -> deq=[1]
    # i=2 (-1): deq=[1,2], window full -> result=[3]
    # i=3 (-3): deq=[1,2,3], result=[3,3]
    # i=4 (5):  5>-3 pop 3, 5>-1 pop 2, 5>3 pop 1 -> deq=[4], result=[3,3,5]
    # i=5 (3):  deq=[4,5], result=[3,3,5,5]
    # i=6 (6):  6>3 pop 5, 6>5 pop 4 -> deq=[6], result=[3,3,5,5,6]
    # i=7 (7):  7>6 pop 6 -> deq=[7], result=[3,3,5,5,6,7] ✓

    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]: # Heap Version - more simple
            """
            TC: O(n log n) - each of n pushes/pops does log n heap work
            SC: O(n) - stale entries can pile up in the heap before being popped
            """
            result = []
            heap = []  # stores (-value, index) so heapq acts as a max-heap, store value first so heapq can compare values left to right

            for i, num in enumerate(nums):
                heapq.heappush(heap, (-num, i))

                # while top of heap is outside the window start
                while heap[0][1] <= i - k: # compare index at top of heap to one before window start
                    heapq.heappop(heap)

                if i >= k - 1:
                    result.append(-heap[0][0])

            return result

sol = Solution()
print("Sliding Window Max:", sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))  # [3,3,5,5,6,7]
print("Sliding Window Max:", sol.maxSlidingWindow([1], 1))  # [1]

print("Sliding Window Max:", sol.maxSlidingWindow2([1,3,-1,-3,5,3,6,7], 3))  # [3,3,5,5,6,7]
print("Sliding Window Max:", sol.maxSlidingWindow2([1], 1))  # [1]