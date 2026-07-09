# 347. Top K Frequent Elements

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

# Example 3:
# Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
# Output: [1,2]

# Key Insight: We use a min heap of size k, and if the len(heap) > k, we pop off the root (smallest ele) to maintain the k largest elements

from collections import Counter
import heapq

class TopK:
    '''
    Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

    Ex. 1
    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]

    TC: 
        - Counting: O(n)
        - Iterating through freq dict: O(m)
        - heappush() and heappop(): O(log k) for sink down/bubble up
        - Extracting result: O(k)
        - Total TC: O(n log k)
    SC: 
        - Storing freq dict: O(n)
        - Storing the heap: O(k)
        - Output list: O(k)
        - Total SC: O(n + k) -> O(n)
    '''

    def topKFrequent(self, nums, k):
        # Step 1: Count frequencies & create dict
        count = Counter(nums)
        
        # Step 2: Use min heap of size k (key = frequency)
        heap = []
        for num, freq in count.items(): # Create min heap
            heapq.heappush(heap, (freq, num)) # Python compares by first ele in tuple
            if len(heap) > k:
                heapq.heappop(heap)  # Remove element with smallest frequency (root)
        
        # Step 3: Extract all k elements from heap
        return [num for freq, num in heap] # Loop through tuples, unpack, and only take "num"

sol = TopK()
print(sol.topKFrequent([1,1,1,2,2,3], 2)) # [1,2]
print(sol.topKFrequent([1], 1)) # [1]
print(sol.topKFrequent([1,2,1,2,1,2,3,1,3,2], 2)) # [1,2]