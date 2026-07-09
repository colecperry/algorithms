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

class Solution(object):
    def sortedSquares(self, nums):
        """
        - TC: 
        - SC:
        """
        output = [0] * len(nums) 
        write = len(nums) - 1 # track write position starting from end
        l, r = 0, len(nums) - 1 # two pointer

        while l <= r:
            if abs(nums[l]) > abs(nums[r]): # left is bigger
                output[write] = nums[l] ** 2 
                l += 1
            else: # right is bigger
                output[write] = nums[r] ** 2
                r -= 1
            write -= 1 # move write pos
                
        return output

my_solution = Solution()
print(my_solution.sortedSquares2([-4,-1,0,3,10]))
print(my_solution.sortedSquares([-7,-3,2,3,11]))