# 268. Missing Number

# Topics: Array, Hash Table, Math, Binary Search, Bit Manipulation, Sorting

# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# Example 1:
# Input: nums = [3,0,1]
# Output: 2
# Explanation:
# n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

# Example 2:
# Input: nums = [0,1]
# Output: 2
# Explanation:
# n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

# Example 3:
# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8
# Explanation:
# n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

# High-Level Idea (set solution)
    # Use a set to track all numbers from 0 to n, then remove the ones that are present in the input array.
    # The one remaining element in the set is the missing number.

    # Step 1: Create an empty set nums_range
    # Step 2: Add every number from 0 to n (inclusive) to the set
    # Step 3: Iterate through each number in the input array `nums`
    #   - If the number exists in the set, remove it
    # Step 4: The remaining element in the set is the missing number
    # Step 5: Return the remaining number using set.pop()

# Time Complexity:
    # O(n) to build the set and iterate through the nums array

# Space Complexity:
    # O(n) to store the set of numbers from 0 to n


from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int: # Using a set
        nums_range = set()
        for i in range(len(nums) + 1): # add all the nums in the range to a set
            nums_range.add(i) 
        for n in nums: # iterate through nums array
            if n in nums_range: # if that num is in the range set
                nums_range.remove(n) # remove it
            else:
                continue
        return nums_range.pop() # last ele in the set will be the missing number
    
    # High-Level Idea: (Using counts + list)
        # Use a counting array to track how many times each number from 0 to n appears.
        # The number with a count of 0 is the missing number.

        # Step 1: Create a list `counts` of zeros with length n + 1 (to cover numbers 0 to n)
        # Step 2: Iterate through the input list `nums`
        #   - For each number, increment the count at the corresponding index in `counts`
        # Step 3: Iterate through the `counts` array
        #   - Return the index that has a count of 0 (this is the missing number)

    # Time Complexity:
        # O(n) - one pass through the input array and one pass through the counts array

    # Space Complexity:
        # O(n) - extra array of size n+1 for counting


    def missingNumber2(self, nums: List[int]) -> int:
        counts = [0] * (len(nums) + 1) # Create an arr of zero's the length of the range
        for num in nums:
            counts[num] += 1 # Increase the count for each index
        for i in range(len(counts)): # missing num will be the number with count == 0
            if counts[i] == 0:
                return i
            
    # High-Level Idea: O(1) space using sum of first n natural numbers
        # Use the formula for the sum of the first n natural numbers to find the expected total,
        # then subtract the actual sum of the input list to find the missing number.

        # Step 1: Calculate `n` as the length of the input list
        # Step 2: Compute the expected sum of numbers from 0 to n using the formula n(n+1)/2
        # Step 3: Compute the actual sum of the numbers in the input list
        # Step 4: Subtract the actual sum from the expected sum to find the missing number

    # Time Complexity:
        # O(n) - summing the input list takes linear time

    # Space Complexity:
        # O(1) - only a few variables are used

    def missingNumber3(self, nums: List[int]) -> int:
        n = len(nums)
        expected = n * (n + 1) // 2 # get the expected output of the list with no missing number
        actual = sum(nums) # get the actual output of the list
        return expected - actual # the difference is the missing number

sol = Solution()
print(sol.missingNumber3([3,0,1])) # 2
print(sol.missingNumber([0,1])) # 2
print(sol.missingNumber([9,6,4,2,3,5,7,0,1])) # 8



