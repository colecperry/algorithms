# 1984. Minimum Difference Between Highest and Lowest of K Scores

# Topics: Array, Sliding Window, Sorting

# You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student. You are also given an integer k.

# Pick the scores of any k students from the array so that the difference between the highest and the lowest of the k scores is minimized.

# Return the minimum possible difference.

# Example 1:

# Input: nums = [90], k = 1
# Output: 0
# Explanation: There is one way to pick score(s) of one student:
# - [90]. The difference between the highest and lowest score is 90 - 90 = 0.
# The minimum possible difference is 0.

# Example 2:
# Input: nums = [9,4,1,7], k = 2
# Output: 2
# Explanation: There are six ways to pick score(s) of two students:
# [9,4,1,7]. The difference between the highest and lowest score is 9 - 4 = 5.
# [9,4,1,7]. The difference between the highest and lowest score is 9 - 1 = 8.
# [9,4,1,7]. The difference between the highest and lowest score is 9 - 7 = 2.
# [9,4,1,7]. The difference between the highest and lowest score is 4 - 1 = 3.
# [9,4,1,7]. The difference between the highest and lowest score is 7 - 4 = 3.
# [9,4,1,7]. The difference between the highest and lowest score is 7 - 1 = 6.
# The minimum possible difference is 2.

# How to Solve (Fixed Sliding Window)
    # Key Insight - by sorting, we can guarentee that the minimum difference will always be a contiguous segment of length k because every other combination's difference will be greater than or equal to the contiguous segment
        # ex. [1,4,7,9]
            # contiguous segments of length 2:
                # 4 - 1 = 3 -> any other combination is greater
                # 7 - 4 = 3 -> any other combination is greater
                # 9 - 7 = 2 -> any other combination is greater
    # Without sorting we would need to check every combination -> O(n)^2

    # TC: sorting is log n, iterating is O(n), total is O(n)log(n)

    # SC: O(1) -> constant time because sorting is in place and it does not take additional memory

from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort() # Sorting returns nothing
        l = 0 # Start left pointer at index 0
        min_score = float('inf') # Track min score difference
        for r in range(k - 1, len(nums)): # Start r pointer at right window max
            score = nums[r] - nums[l] # Calc score for each fixed len window
            min_score = min(min_score, score) # Update min
            l += 1 # Move left window edge
        return min_score
    
sol = Solution()
print(sol.minimumDifference([90], 1)) # 0
print(sol.minimumDifference([9,4,1,7], 2)) # 2