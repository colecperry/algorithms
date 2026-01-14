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

# How it works:
    # 1. Sort intervals by start time
    # 2. Compare each interval with last merged interval
    # 3. If current.start ≤ last.end, they overlap → merge
    # 4. If no overlap, add current as new interval
    # 5. Merging: extend last interval's end to max(last.end, current.end)


from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]: # for loop
        """
        - TC: O(n log n) - dominated by sorting
        - SC: O(n) - output array (or O(log n) for sorting if we don't count 
        output)
        """

        intervals.sort(key=lambda x: x[0]) # sort by start
        result = []
        prev_start, prev_end = intervals[0] # get initial start & end by destructuring

        for curr_start, curr_end in intervals[1:]: # iterate & unpack from i=1 
            if prev_end >= curr_start: # check for overlap with prev interval
                prev_end = max(prev_end, curr_end) # update end pointer
            else: # no overlap
                result.append([prev_start, prev_end]) # add merged interval to res
                prev_start, prev_end = curr_start, curr_end # move pointers
        
        result.append([prev_start, prev_end]) # Append after no more overlaps
        return result

sol = Solution()
print(sol.merge([[1,3],[2,6],[8,10],[15,18]])) # [[1,6],[8,10],[15,18]]
print(sol.merge([[1,4],[4,5]])) # [[1,5]]

#   0   1   2  3  4  5
#   a
# [-4, -1, -1, 0, 1, 2]
#       b            c





