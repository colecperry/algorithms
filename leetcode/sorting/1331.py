# 1331 - Rank Transform of an Array

# Topics : Array, Hash Table, Sorting

# Given an array of integers arr, replace each element with its rank.

# The rank represents how large the element is. The rank has the following rules:

# Rank is an integer starting from 1.
# The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
# Rank should be as small as possible.

# Example 1:
# Input: arr = [40,10,20,30]
# Output: [4,1,2,3]
# Explanation: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.

# Example 2:
# Input: arr = [100,100,100]
# Output: [1,1,1]
# Explanation: Same elements share the same rank.

# Example 3:
# Input: arr = [37,12,28,9,100,56,80,5,12]
# Output: [5,3,4,2,8,6,7,1,3]

# How to Solve (Sorting plus hashmap):
    # Create a rankings hashmap -> sort the original array into another sorted array
    # Loop through the sorted array and assign rankings to each value starting at 1
    # Now loop back over the original array and store the ranking in the current index


class Solution(object):
    def arrayRankTransform(self, arr):
        sorted_arr = sorted(arr) # Sort the array
        ranking_map = {} # Create a rankings map
        rank = 1 # Variable to assign ranks

        for i in range(len(sorted_arr)): # Loop through sorted array
            if sorted_arr[i] not in ranking_map: # If the num isn't in the rankings map
                ranking_map[sorted_arr[i]] = rank # Add it to the rankings map
                rank += 1 # Increment the rank for the next num

        for i, num in enumerate(arr): # Loop through original array
            arr[i] = ranking_map[num] # Set the current index to the ranking in the map

        return arr
            



my_solution = Solution()
print(my_solution.arrayRankTransform([40, 10, 20, 30]))
print(my_solution.arrayRankTransform([100, 100, 100]))
print(my_solution.arrayRankTransform([37,12,28,9,100,56,80,5,12]))