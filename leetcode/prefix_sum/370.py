# 370. Range Addition

# Assume you have an array of length n initialized with all 0's and are given k update operations.

# Each operation is represented as a triplet: [startIndex, endIndex, inc] which increments each element of the
# subarray A[startIndex ... endIndex] (startIndex and endIndex inclusive) by inc.

# Return the modified array after all k operations were executed.

# Example 1:
# Input: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
# Output: [-2,0,3,5,3]

# Brute Force O(n*k) - For each update, loop from startIndex to endIndex and add inc to every element. k updates * up to n elements each.

# O(n+k) - Big Idea: don't touch every element in the range. Instead, mark only the two boundaries of each update in a diff array: diff[startIndex] += inc (start applying inc from here on) and diff[endIndex+1] -= inc (stop applying inc after here). 
# Once every update is recorded, take a single running-sum pass over diff — the result at each index is the final array value, since the running sum naturally re-applies every inc that started before it and cancels every inc that already ended.

from typing import List

class Solution:
    """
    NOTE: diff[endIndex+1] -= inc needs a sentinel slot, so the diff array is length n+1 (endIndex can be n-1).
    """
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        """
        - TC: O(n + k) - k updates (O(1) each) + one O(n) pass to reconstruct
        - SC: O(n) - diff array
        """
        diff = [0] * (length + 1)  # Extra slot so endIndex+1 never goes out of bounds

        for startIndex, endIndex, inc in updates:
            diff[startIndex] += inc      # Start applying inc from here on
            diff[endIndex + 1] -= inc    # Stop applying inc right after endIndex

        result = [] # result array
        curSum = 0  # Running total = value re-applied by every update that's "active" at this index

        for i in range(length):
            curSum += diff[i]
            result.append(curSum)

        return result

# Example trace:
# length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
#
# diff starts as [0,0,0,0,0,0] (length 6)
#
# NOTE: 
# diff[start] += val — marks "starting from index start, add val from here onward"
# diff[end+1] -= val — marks "cancel that val addition from here onward"
#
# update [1,3,2]:  diff[1] += 2 -> diff[4] -= 2
#   diff = [0, 2, 0, 0, -2, 0]
#
# update [2,4,3]:  diff[2] += 3 -> diff[5] -= 3
#   diff = [0, 2, 3, 0, -2, -3]
#
# update [0,2,-2]: diff[0] += -2 -> diff[3] -= -2 (i.e. += 2)
#   diff = [-2, 2, 3, 2, -2, -3]
#
# Running sum over indices 0..4:
#   i=0: curSum = -2         -> result = [-2]
#   i=1: curSum = -2+2 = 0   -> result = [-2, 0]
#   i=2: curSum = 0+3 = 3    -> result = [-2, 0, 3]
#   i=3: curSum = 3+2 = 5    -> result = [-2, 0, 3, 5]
#   i=4: curSum = 5-2 = 3    -> result = [-2, 0, 3, 5, 3]
#
# Return result = [-2, 0, 3, 5, 3]

sol = Solution()
print(sol.getModifiedArray(5, [[1,3,2],[2,4,3],[0,2,-2]]))  # [-2, 0, 3, 5, 3]
print(sol.getModifiedArray(3, [[0,1,1],[1,2,-1]]))          # [1, 0, -1]
