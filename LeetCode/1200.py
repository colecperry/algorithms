# 1200. Minimum Absolute Difference

# Topics: Array, Sorting

# Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.

# Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows
    # a, b are from arr
    # a < b
    # b - a equals to the minimum absolute difference of any two elements in arr

# Example 1:
# Input: arr = [4,2,1,3]
# Output: [[1,2],[2,3],[3,4]]
# Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.

# Example 2:
# Input: arr = [1,3,6,10,15]
# Output: [[1,3]]

# Example 3:
# Input: arr = [3,8,-10,23,19,-4,-14,27]
# Output: [[-14,-10],[19,23],[23,27]]

# How to solve:
    # Sort the array so we can return the list of pairs in ascending order where a < b
    # Create a variable to store the minimum abs value (float('inf')) and an output arr to store the answer
    # Loop through the array starting at the first index
        # Take the abs value by subtracting the value at i - 1 from i
        # If the min abs value equals the abs value you just calculated, append pair [a,b] to array
        # If the abs value you just calculated is less than the min abs value, reassign min abs value, clear the output array, and append the new pair with the min abs value [b,a] to the array

class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()
        min_abs_val = float('inf')# Create var to hold min abs value
        output_arr = [] # Create an empty arr to store output
        for i in range(1, len(arr)): 
            abs_val = abs(arr[i] - arr[i-1])# Take abs value
            if abs_val == min_abs_val: 
                output_arr.append([arr[i-1], arr[i]]) # Append to arr
            if abs_val < min_abs_val:
                min_abs_val = abs_val # Reassign min
                output_arr = [] # Clear out arr
                output_arr.append([arr[i-1], arr[i]])# Append to arr
        return output_arr

arr1, arr2, arr3 = [4,2,1,3], [1,3,6,10,15], [3,8,-10,23,19,-4,-14,27]

my_solution = Solution()
print(my_solution.minimumAbsDifference(arr1))
print(my_solution.minimumAbsDifference(arr2))
print(my_solution.minimumAbsDifference(arr3))
