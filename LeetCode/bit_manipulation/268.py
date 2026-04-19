# 268. Missing Number

# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# Example 1:
# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

# Example 2:
# Input: nums = [0,1]
# Output: 2
# Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

# Example 3:
# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8
# Explanation:n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

#                       XOR EXPLANATION
# --------------------------------------------------------------
# You apply XOR to integers and Python handles the bitwise operation across all their bits under the hood
# XOR outputs 1 when bits are different, 0 when they're the same
# 0 XOR 0 = 0  (same)
# 1 XOR 1 = 0  (same)
# 0 XOR 1 = 1  (different)
# 1 XOR 0 = 1  (different)

# Key tricks:
#   n ^ n = 0  (same number cancels out)
#   n ^ 0 = n  (zero has no effect)

# Ex: 
# 3 ^ 5
# 011 XOR 101 = 110 = 6

class Solution(object):
    def missingNumber(self, nums):
        """
        Approach: XOR
        - XOR every number from 0 to n into res
        - XOR every number in nums into res
        - Pairs cancel out (n ^ n = 0), leaving only the missing number
        - TC: O(n)
        - SC: O(1)

        Example: nums = [3, 0, 1], missing = 2
          XOR expected (0 to n): res = 0 ^ 1 ^ 2 ^ 3 = 0
          XOR actual (nums):     res = 0 ^ 3 ^ 0 ^ 1 = 2  <- missing number

          0 ^ 0 = 0  (cancels)
          1 ^ 1 = 0  (cancels)
          3 ^ 3 = 0  (cancels)
          2          (survivor = missing number)
        """
        res = 0

        for i in range(len(nums) + 1):  # XOR every expected number 0 to n
            res ^= i

        for num in nums:                # XOR every actual number in nums
            res ^= num

        return res # number left (survivor) is missing number

sol = Solution()
print(sol.missingNumber([3,0,1])) # 2
print(sol.missingNumber([0,1])) # 2
print(sol.missingNumber([9,6,4,2,3,5,7,0,1])) # 8





