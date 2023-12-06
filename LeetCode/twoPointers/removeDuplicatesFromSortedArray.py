# Given an integer array nums sorted in non-decreasing order, remove the duplicates
# in-place such that each unique element appears only once. The relative order of the
# elements should be kept the same. Then return the number of unique elements in nums.
# Consider the number of unique elements of nums to be k, to get accepted, you need
# to do the following things: Change the array nums such that the first k elements of
# nums contain the unique elements in the order they were present in nums initially.
#The remaining elements of nums are not important as well as the size of nums. Return
# k.

# Custom Judge: 
# The judge will test your solution with the following code:
# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length

# int k = removeDuplicates(nums); // Calls your implementation

# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }

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
    # We need to remove duplicates in place - AKA with the original list.
    # Given a list, we need to use the two pointer approach using the indexes at the 
    # next available poisition we can insert at (left pointer) and the index we are
    # iterating on.
    # We compare the value at the index we are iterating on to the index before,
    # and if we encounter a new value in the list, we replace it at the left pointer's
    # index.
    # Since the know the first value is unique no matter what, we start our loop on
    # the first index (instead of zero).


class Solution(object):
    def removeDuplicates(self, nums):
        l = 1 # Set our left pointer to index 1
        for i in range(1, len(nums)): # Start a loop starting at index 1 and ending
            # before (but not including) the length of the nums list
            if nums[i] != nums[i-1]: # Compare the value at the current index to the
                # value at the previous index. If the numbers are not the same, 
                nums[l] = nums[i] # replace the number at the left pointer's index
                # with the value at the current index we are iterating on
                l += 1 # Increment the left pointer one to the left (the next available)
                # position we can insert a new, unique value at
        return l # Return l, which represents the number of unique values in the list
        # On the last loop, when 4 is placed in nums[l]'s spot, we increment l one more
        # time, so it ends at l = 5
    
answer = Solution()
print(answer.removeDuplicates([1,1,2]))
print(answer.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))