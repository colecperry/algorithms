# 26. Remove Duplicates from Sorted Array

# Given an integer array nums sorted in non-decreasing order, remove the duplicates
# in-place such that each unique element appears only once. The relative order of the
# elements should be kept the same. Then return the number of unique elements in nums.
# Consider the number of unique elements of nums to be k, to get accepted, you need
# to do the following things: Change the array nums such that the first k elements of
# nums contain the unique elements in the order they were present in nums initially.
# The remaining elements of nums are not important as well as the size of nums. Return
# k.


# Example 1: 
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums
# being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Example 2: 
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of
# nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# How to Solve:
    # Big Idea: Use a two pointer approach: one pointer scans through the array and one holds the next open position for the unique number
    # Code:
        # Initialize pointer for next open spot
        # Scan thru the array starting at second index (first index is guarenteed unique)
            # If the numbers at index i and i - 1 are not equal, we have encountered a new unique number: move the number at index i to the number at the index of the pointer which holds the next position for a unique number
            # Increment the pointer
            # If the numbers at index i and i - 1 are equal, we have not encountered a new unique number, so i continue to the next iteration
        # Return pointer value (will hold the number of unique numbers)



class Solution(object):
    def removeDuplicates(self, nums):
        l = 1 # Set our left pointer to index 1
        for i in range(1, len(nums)): # Start a loop starting at index 1 
            if nums[i] != nums[i-1]: # If values at i & i - 1 are not equal
                nums[l] = nums[i] # replace num with left pointer
            l += 1 # Increment the left pointer one to the left (the next available)
                # position we can insert a new, unique value at
        return l # Return l, which represents the number of unique values in the list
        # On the last loop, when 4 is placed in nums[l]'s spot, we increment l one more
        # time, so it ends at l = 5
    
answer = Solution()
print(answer.removeDuplicates([1,1,2]))
print(answer.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))