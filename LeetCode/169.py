# 169. Majority Element

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

class Solution(object):
    def majorityElement(self, nums):
        # Create a dictionary that holds the number and the count
        my_dict = {}
        # Loop through the array
        for n in nums:
            # If the number does not exist, add it to the dict
            if n not in my_dict:
                my_dict[n] = 1
            # If it does, increment the count
            else:
                my_dict[n] += 1       
        # Loop through the dict, 
        for key in my_dict:
            # If the value is bigger than n/2
            if my_dict[key] > len(nums)//2:
            # Return the max num element
                return key
    
    # O(1) space complexity
    def majorityElement2(self, nums):
        # Phase 1: Find a candidate
        candidate = None
        count = 0
        
        for num in nums:
            if count == 0:  # Update candidate when count is 0
                candidate = num
            count += (1 if num == candidate else -1)
        
        # Phase 2: Verify the candidate (optional if input guarantees a majority element)
        # The problem guarantees that there is always a majority element, so this step is not strictly necessary.
        return candidate



solution = Solution()
print(solution.majorityElement2([3,2,3]))
print(solution.majorityElement2([2,2,1,1,1,2,2]))
