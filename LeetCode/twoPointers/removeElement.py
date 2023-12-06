# Given an integer array nums and an integer val, remove all occurrences of val in nums
# in-place. The order of the elements may be changed. Then return the number of elements
# in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get
# accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements
# which are not equal to val. The remaining elements of nums are not important as well
# as the size of nums.
# Return k.

# Custom Judge:
# The judge will test your solution with the following code:
# int[] nums = [...]; // Input array
# int val = ...; // Value to remove
# int[] expectedNums = [...]; // The expected answer with correct length.
#                             // It is sorted with no values equaling val.

# int k = removeElement(nums, val); // Calls your implementation

# assert k == expectedNums.length;
# sort(nums, 0, k); // Sort the first k elements of nums
# for (int i = 0; i < actualLength; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.



# Example 1:
    # Input: nums = [3,2,2,3], val = 3
    # Output: 2, nums = [2,2,_,_]
    # Explanation: Your function should return k = 2, with the first two elements of
    # nums being 2.
    # It does not matter what you leave beyond the returned k (hence they are
    # underscores).

# Example 2:
    # Input: nums = [0,1,2,2,3,0,4,2], val = 2
    # Output: 5, nums = [0,1,4,0,3,_,_,_]
    # Explanation: Your function should return k = 5, with the first five elements of
    # nums containing 0, 0, 1, 3, and 4.
    # Note that the five elements can be returned in any order.
    # It does not matter what you leave beyond the returned k (hence they are
    # underscores).

# How to Solve:
    # We need to get rid of occurances in the nums list that equal val, and return
    # the number of elements in the nums list not equal to val.
    # Using a two pointer approach, initialize a left pointer at the zero'th index
    # and the right pointer which will interate through the nums list
    # If the value at the current index is not equal to val, replace it at the 
    # next available position. If it does equal, ignore it, essentially replacing
    # the value at all the indexes that equal val. The left pointer iterates the
    # number of times that the value at the current index does not equal val


class Solution(object):
    def removeElement(self, nums, val):
        l = 0 # Initalize a left pointer at the zero'th index
        for i in range(len(nums)): # Iterate through the list, ending before (but not
            # including) the length of the nums list
            if nums[i] != val: # If the value at the current index is not equal to 
                # the value passed in,
                nums[l] = nums[i] # Replace the value at the next available position
                # we can insert at with the value at the current index. If the value
                # at the current index is equal to the value passed in, continue
                l += 1 # Iterate the left pointer by one
        nums = nums[:l] # Trim the list to remove the elements equal to val
        return nums, l # Return the number of elements not equal to val
        
answer = Solution()
print(answer.removeElement([3,2,2,3], 3))
print(answer.removeElement([0,1,2,2,3,0,4,2], 2))