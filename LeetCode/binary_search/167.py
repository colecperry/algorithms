# 167. Two Sum II - Input Array Is Sorted

# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space. This means your algorithm must not use extra space that grows with the size of the input array. -> O(n^2) is not allowed. 


# Example 1:

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
# Example 2:

# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
# Example 3:

# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

nums1 = [2, 7, 11, 15]
target1 = 9
nums2 = [2, 3, 4]
target2 = 6
nums3 = [-1, 0]
target3 = -1
nums4 = [1, 3, 4, 5, 7, 11]
target4 = 9

class Solution(object):
    def twoSum2(self, numbers, target):
        left = 0 # Variable left initialized to 0
        right = len(numbers) - 1 # Variable right initialized to last index

        while left < right: # Create binary search while loop
            sum = numbers[left] + numbers[right] # Take the sum
            if sum < target: # If the target is greater than sum
                left = left + 1 # Move left pointer over
            elif sum > target: # If sum is greater than target
                right = right - 1 # Move right pointer over
            else: # If they are equal
                return [left + 1, right + 1] # Return index + 1


my_solution = Solution()
print(my_solution.twoSum2(nums1, target1))
print(my_solution.twoSum2(nums2, target2))
print(my_solution.twoSum2(nums3, target3))
print(my_solution.twoSum2(nums4, target4))