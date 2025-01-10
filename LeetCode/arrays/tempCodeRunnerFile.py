class Solution(object):
    def maxSubArray(self, nums):
        largest = nums[0]
        for i in range(len(nums)):
            new_sum = nums[i]
            for j in range(i+1, len(nums)):
                new_sum = new_sum + nums[j] # need to reset the newsum after each iteration of i
                if new_sum > largest:
                    largest = new_sum
        return largest