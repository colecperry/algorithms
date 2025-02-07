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

# Solution 1 uses an array to organize elements into the freq array without using a sort, which is the most expensive operation in Solution 2 and increases the time complexity to O(n log n)

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
    
    # The second solution needed extra handling for this edge case because sorting by frequency alone does not inherently preserve the order of elements as they appear in the input array (nums). In contrast, the first solution indirectly preserves the order due to the way it constructs the freq array and processes it in reverse.

    def topKFrequent2(self, nums, k):
        my_dict = dict()

        # Count the frequency of each number
        for i in range(len(nums)):
            if nums[i] not in my_dict:
                my_dict[nums[i]] = 1
            else:
                my_dict[nums[i]] += 1
        
        # Sort the dictionary by frequency (descending) and tie-break by the order in `nums`
        sorted_items = sorted(my_dict.items(), key=lambda item: (-item[1], nums.index(item[0])))

        # Extract the top k keys
        res = [item[0] for item in sorted_items[:k]]
        
        return res

my_solution = Solution()
print(my_solution.topKFrequent([1,1,1,2,2,3], 2))
print(my_solution.topKFrequent([1], 1))
