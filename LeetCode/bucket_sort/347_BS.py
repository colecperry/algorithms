# 347 - Top K Frequent Elements

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]

# How to solve -> Use BUCKET SORT
    # For the index, we store the count numbers, and for the values, we store a list of numbers from input array nums with that count
    # For nums [1,1,1,2,2,100] indecies stop at 6 because that is the max possible count for any number (proportinate to the size of the input array)
    # We then start at the end of the array and add to our result a max of k times

from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        - TC: O(n) -> iterate through nums to count freq's, create freq array, add items to freq array, and iterate backwards to create result list
        - SC: O(n) -> hold "n" nums in count map, and "n" nums in freq list
        """
        count_map = Counter(nums) # Hashmap to count the occurences of each num
        freq = [[] for i in range(len(nums) + 1)] # List of buckets where i = freq and each index holds a list of nums with that freq
        
        for num, count in count_map.items(): # Loop thru freq dict
            freq[count].append(num) # Add nums to freq bucket
        
        res = []
        for i in range(len(freq) - 1, 0 , -1): # Iterate in reverse order
            for num in freq[i]: # Iterate through sublist
                res.append(num) # Append the val
                if len(res) == k: # Only append top K freq
                    return res 

my_solution = Solution()
print(my_solution.topKFrequent([1,1,1,2,2,3], 2)) # [1,2]
print(my_solution.topKFrequent([1], 1)) # [1]
