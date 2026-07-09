# 56. Merge Intervals

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Example 1:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

# Example 2:
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]: # for loop
        intervals.sort(key=lambda x:x[0]) # sort intervals by start
        output = []
        curr_start, curr_end = intervals[0][0], intervals[0][1] # current interval
        
        for i in range(1, len(intervals)): # Iterate starting at first index
            if intervals[i][0] <= curr_end: # intervals overlap
                curr_end = max(curr_end, intervals[i][1]) # take max end of two intervals -> edge case where interval is fully contained
            else:
                output.append([curr_start, curr_end]) # intervals do not overlap
                curr_start, curr_end = intervals[i][0], intervals[i][1]
        
        output.append([curr_start, curr_end]) # append last interval
        
        return output
        

sol = Solution()
print(sol.merge([[1,3],[2,6],[8,10],[15,18]])) # [[1,6],[8,10],[15,18]]
print(sol.merge([[1,4],[4,5]])) # [[1,5]]
print(sol.merge([[1,4], [2,3]])) # [[1,4]] -> interval is fully contained edge case