# 1636. Sort Array by Increasing Frequency

# Topics: Array, Hash Table, Sorting

# Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

# Return the sorted array.

# Example 1:

# Input: nums = [1,1,2,2,2,3]
# Output: [3,1,1,2,2,2]
# Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.

# Example 2:
# Input: nums = [2,3,1,3,2]
# Output: [1,3,3,2,2]
# Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.

# Example 3:
# Input: nums = [-1,1,-6,4,5,-6,1,4,1]
# Output: [5,-1,4,4,-6,-6,1,1,1]

# How to Solve: Solution 1:
    # Create a freq dict from the array by importing Counter
    # sort the frequency dictionary 
        # Use sorted() function on the dictionary items where each item is a tuple (key, freq)
        # We sort based on the lambda function which sorts based on:
        # item[1] -> the frequency in ascending order
        # -item[0] -> and the value second (descending if values are the same)
    # Loop through each key and value in the sorted_freq_dict.items()
        # Multiply the value times the frequency and store in list, and then use extend to add it to the output array

    # Time Complexity: O(N log N) (due to sorting the dictionary items).
    # Space Complexity: O(N) (stores frequency dictionary and output list).

# How to Solve: Solution 2:
    # Create a freq dict from the array by importing Counter
    # Create sorted array using the sorted() function on the array where each item is a tuple (key, freq)
        # We sort based on the lambda function where:
            # freq_dict[x] -> sorts by frequency (ascending)
            # -x -> If frequencies are the same, sorts by value (descending)

    # Time Complexity: O(N log N) (due to sorting the nums list).
    # Space Complexity: O(N) (stores frequency dictionary and sorted list).

# Notes on key parameter in sorted()
    # The "key" parameter in sorted(), min(), and max(), allows you to specify a custom sorting or comparison criteria
    # General synatx: sorted(iterable, key=lambda x: primary key, secondary key)
        # iterable is the list you iterate through
        # "x" is the element it takes from the iterable
        # primary key is what x is sorted by first, and secondary key is used if there is a tie from the primary key

from collections import Counter

class Solution(object):
    def frequencySort(self, nums):
        freq_dict = Counter(nums)  # Step 1: Count frequency

        # Step 2: Sort by frequency, then by value (descending)
        sorted_items = sorted(freq_dict.items(), key=lambda item: (item[1], -item[0]))

        output_arr = []  # Step 3: Build output array
        
        # Step 4: Construct the result
        for value, freq in sorted_items:  # Use sorted list instead of converting back to dict
            output_arr.extend([value] * freq)

        return output_arr
    
    def frequencySort2(self, nums):
        freq_dict = Counter(nums)  # Create counter dict

        # Sort by frequency (ascending), then by value (descending)
        sorted_nums = sorted(nums, key=lambda x: (freq_dict[x], -x))

        return sorted_nums



my_solution = Solution()
print(my_solution.frequencySort([1,1,2,2,2,3]))
print(my_solution.frequencySort2([2,3,1,3,2]))
print(my_solution.frequencySort([-1,1,-6,4,5,-6,1,4,1]))

# Example walk through -> Solution 1:
    # nums = [2,3,1,3,2]
    # freq_dict = {2: 2, 3: 2, 1: 1}
    # sort by lambda based on:
        # sort by frequency (item[1] in ascending order)
        # if freq's the same, sort by value -item[0] in descending order -> must put negative to sort in descending order since the default is ascending
            # tuple (key, freq) -> lambda output (freq, -key)
            #           (2,2)   ->   (2,-2)
            #           (3,2)   ->   (2,-3)
            #           (1,1)   ->   (1,-1)
        # 1 has lowest freq -> (1,-1)
        # Both 2 and 3 have same freq's (2,-2), (2,-3)
            # Sort by lower number -> -3, so 3 comes next, and 2 comes last
        
        # final result [(1, 1), (3, 2), (2, 2)]

# Example walk through -> Solution 2:
# nums = [2, 3, 1, 3, 2]
# freq_dict = {2: 2, 3: 2, 1: 1}
# sort nums list based on:
    # sort by frequency (freq_dict[x] in ascending order)
    # if freq's the same, sort by value -x in descending order
        # number x   -> lambda output (freq_dict[x], -x)
        #     2      ->   (2, -2)
        #     3      ->   (2, -3)
        #     1      ->   (1, -1)
        #     3      ->   (2, -3)
        #     2      ->   (2, -2)
        
    # 1 has the lowest frequency (1, -1), so it comes first.
    # Both 2 and 3 have the same frequency:
        # -3 < -2, so 3 comes before 2 in the sorted order.
    
    # sorted order of nums: [1, 3, 3, 2, 2]

