# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.

# Custom Judge:
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

# Example 1: 
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Example 2: 
# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
# Note that the five elements can be returned in any order.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Notes:
# Step 1: Iterate over the nums array
# Step 2: If the number on the current iteration is not equal to the value
#       - replace the value of the the index that you are currently on &
#       - increment i
# Step 3: If the num is equal to the value, do not increment i
# Note: The way this works for example 2 is that once it hits the number 3 in the array it will
# replace the first 2 with it
# Step 4: Return i, which is the number of the unique iterations not equal to the value

class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        for num in nums:
            if num != val:
                nums[i] = val 
                i += 1
            else:
                i += 0
        return i
                

solution = Solution()
print(solution.removeElement([3, 2, 2, 3], 3))

# OR:
# def removeElement(nums, val):
#     i = 0
#     while i < len(nums):
#         print("i:", i)
#         print("len(nums):", len(nums))
#         print("nums:", nums)
#         if nums[i] == val:
#             del nums[i]
#         else:
#             i+=1


# print(removeElement([0,1,2,2,2,3,0,4,2], 2))