# # Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums. Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things: Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums. Return k.

# # Custom Judge: 
# // # Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# // # Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# // # Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# // # Return k.

# // # Custom Judge:
# // # int[] nums = [...]; // Input array
# // # int val = ...; // Value to remove
# // # int[] expectedNums = [...]; // The expected answer with correct length.
# // #                             // It is sorted with no values equaling val.

# // # int k = removeElement(nums, val); // Calls your implementation

# // # assert k == expectedNums.length;
# // # sort(nums, 0, k); // Sort the first k elements of nums
# // # for (int i = 0; i < actualLength; i++) {
# // #     assert nums[i] == expectedNums[i];
# // # }

# // # Example 1: 
# // # Input: nums = [3,2,2,3], val = 3
# // # Output: 2, nums = [2,2,_,_]
# // # Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# // # It does not matter what you leave beyond the returned k (hence they are underscores).

# // # Example 2: 
# // # Input: nums = [0,1,2,2,3,0,4,2], val = 2
# // # Output: 5, nums = [0,1,4,0,3,_,_,_]
# // # Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
# // # Note that the five elements can be returned in any order.
# // # It does not matter what you leave beyond the returned k (hence they are underscores).


def removeElement(nums, val):
    i = 0
    while i < len(nums):
        print("i:", i)
        print("len(nums):", len(nums))
        print("nums:", nums)
        if nums[i] == val:
            del nums[i]
        else:
            i+=1


print(removeElement([0,1,2,2,2,3,0,4,2], 2))