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


# Time complexity: O(n)
# Space complexity: O(n)

from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        count_map = {} # Hashmap to count the occurances of each value
        freq = [[] for i in range(len(nums) + 1)] # Array where the index is the count of an element and value is the list of the elements that occur that many times

        for n in nums: # Loop through input array nums
            count_map[n] = 1 + count_map.get(n, 0) # Count number of occurances and add to prev count or add zero if not in dict
        
        for num, count in count_map.items(): # Loop thru number&count in each key-val pair in dict
            freq[count].append(num) # At index "count" we append the key "n" which is the number
        
        res = []
        for i in range(len(freq) -1, 0 , -1): # Iterate in descending order
            for num in freq[i]: # For every value in the sublist of freq at idx i
                res.append(num) # Append the value n
                if len(res) == k: # When the length of the result is equal to k
                    return res # Return the result
    
# How to Solve: Hashmap with sorting
    # Create a frequency arr using counter
    # Sort the dict by freq using a lambda -> Creates a list of tuples
    # iterate through the list of tuples, and append k key's to the output array
    # Time complexity: Sorting is O(n log n), iterating again is O(n), total is O(n log n)
    # Space complexity: Creating counter dict is O(n), storing a list of tuples is O(n), and storing the output array is O(k), simplify to O(n)


    def topKFrequent2(self, nums, k):
        count = Counter(nums) # Create a frequency dict
        output = [] # Create an output array
        
        sorted_counts = sorted(count.items(), key=lambda item: item[1], reverse=True) # Sort the dict by freq
        # Iterate trhough the list of tuples
        for i, (key, value) in enumerate(sorted_counts):
            if i >= k: # Check if we already have k ele's
                break
            output.append(key) # If not append the key (ele)

        return output

my_solution = Solution()
print(my_solution.topKFrequent2([1,1,1,2,2,3], 2))
print(my_solution.topKFrequent([1], 1))
