# 977. Squares of a Sorted Array

# Topics: Array, Two Pointer, Sorting

# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# Example 2:
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

# Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?

# How to Solve (sorting): (N log N)
    # Use a list comprehension (loop through each element in the array, calculate the squared element, and store in a new arr -> not in place)
    # Use sorted function -> returns a new list, .sort() modifies in place

# How to Solve (two pointer): O(n)
    # Create an output array for the result (equal to the nums array)
    # Create two pointers L and R -> L starts at 0, R starts at len-1
        # Loop through the nums arr starting at the last index and moving -1 each it
        # Compare the absolute values of the L and R pointers (we know the largest squared values will be at the ends)
        # If nums[l] < nums[r], take the value, square it, and add to the output arr at index i, and move r pointer backwards
        # If nums[l] > nums[r], take the value, square it, add it to the output arr at index i, and move the left pointer forwards

class Solution(object):
    def sortedSquares(self, nums):
        return sorted(num * num for num in nums)
    
    def sortedSquares2(self, nums):
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1
            result[i] = square * square
        return result

my_solution = Solution()
print(my_solution.sortedSquares2([-4,-1,0,3,10]))
print(my_solution.sortedSquares([-7,-3,2,3,11]))