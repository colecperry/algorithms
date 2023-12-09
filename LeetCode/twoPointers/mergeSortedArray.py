# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
# and two integers m and n, representing the number of elements in nums1 and nums2
# respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored
# inside the array nums1. To accommodate this, nums1 has a length of m + n, where the
# first m elements denote the elements that should be merged, and the last n elements
# are set to 0 and should be ignored. nums2 has a length of n.


# Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from
# nums1.

# Example 2:
# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].

# Example 3:
# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to
# ensure the merge result can fit in nums1.

# How to Solve:
    # Since we are guarenteed to have enough space for nums2 to fit in nums1, and 
    # the zeroes are at the end of the list, we want to start merging from the 
    # end of nums1.
    # Create a variable "last" where we are going to insert elements
    # Since both lists are in increasing order, compare the last non-zero element in
    # list 1 with the last element in nums2, which ever is bigger will fill "last"
    # Decrement counters "m, n, and last"
    # Solve for last edge case (need to review and use a better example)

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1 = nums1 + [0] * n # Wrote this to ensure there are enough spaces
        # to fill in list1, was getting a strange error
        last = m + n - 1 # Get the last index of nums1

        while m > 0 and n > 0: # Create a while loop that runs as long as there are
            # still elements left in both arrays
            if nums1[m - 1] > nums2[n - 1]: # Find the greater value between the last
                # non-zero element in nums1 and the last element in nums2. If the
                # nums1 element is greater than the nums2 element, 
                nums1[last] = nums1[m - 1] # replace the element at the last index of
                # nums1 with the last non-zero element of nums1 and
                m -= 1 # Decrement m, which represents the number of elements in nums1
            else: # If the last non-zero element in nums1 and the last element in
                # nums2 are equal or last element in nums2 is greater,
                nums1[last] = nums2[n - 1] # replace the element at the last index of
                # nums1 with the last element of nums2 and
                n -= 1 # Decrement n, which represents the number of elements in nums2
            last -= 1 # After each loop, we replace an element so we must move the 
            # last index to the left once
        
        while n > 0: # Once m decrements to zero, we may have a case where the last
            # element in nums1 is bigger than the last element in nums2, so we create
            # a loop that runs until there are no more elements left in nums2
            nums1[last] = nums2[n - 1] # Fill the last spot in nums1 with the 
            # last elements in nums2, since they are smaller
            n = n - 1 # Decrement n
            last = last - 1 # Decrement last
        
        return nums1


answer = Solution()
print("Example 1:")
print(answer.merge([1,2,3], 3, [2,5,6], 3))

print("Example 2:")
print(answer.merge([1], 1, [], 0))

print("Example 3:")
print(answer.merge([0], 0, [1], 1))