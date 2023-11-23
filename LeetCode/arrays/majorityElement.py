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
        hashmap = {}

        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]] += 1
                
            else:
                hashmap[nums[i]] = 1
            print(hashmap)
        
        maxCount = 0
        maxNum = -1
        for k in hashmap.keys():
            if hashmap[k] > maxCount:
                maxCount = hashmap[k]
                maxNum = k
        if maxCount > len(nums)/2:
            return maxNum

        return -1




solution = Solution()
print(solution.majorityElement([3,2,3]))