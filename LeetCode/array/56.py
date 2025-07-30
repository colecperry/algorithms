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

# How to Solve (while loop):
# - First, sort the intervals by their starting point so overlapping intervals are adjacent.
# - Use a while loop to iterate through the intervals.
# - Track the start and end of the current merged interval.
# - As long as the next interval starts before or at the current interval's end,
#   extend the current interval's end to include it.
# - Once no more overlapping intervals are found, append the merged interval to the output.
# - Repeat until all intervals are processed.

# Time Complexity (TC):
# - Sorting the intervals takes O(n log n)
# - The while loop goes through each interval once → O(n)
# - So overall time complexity is O(n log n)

# Space Complexity (SC):
# - O(n) in the worst case, if no intervals overlap and each interval is added to the output
# - No extra space beyond the output list (ignoring sorting overhead, which is O(1) if done in-place)


from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]: # while
        # sort intervals by start of interval
        intervals.sort(key=lambda x: x[0])
        i = 0 # Manual i pointer for while loop
        output = []
        while i < len(intervals): # Loop until end of interval array
            start = intervals[i][0] # Start of current interval range 
            end = intervals[i][1] # End of current interval range
            while i + 1 < len(intervals) and intervals[i + 1][0] <= end: # if overlap exists (next start less than current end), keep iterating
                end = max(end, intervals[i + 1][1]) # update the end
                i += 1
            output.append([start, end]) # append interval once overlap ends
            i += 1
        return output
                
    # High-level approach (For loop):
    # - Sort the intervals by their starting point so overlapping intervals are adjacent.
    # - Initialize the first interval as the starting range.
    # - Iterate through each interval using a for loop:
    #   - If the current interval overlaps with the previous one (i.e., current start <= previous end), update the end of the current merged range to the maximum of both ends.
    #   - If there is no overlap, append the previous merged interval to the result,
    #     and start a new range with the current interval.
    # - After the loop, append the final merged interval to the result list.

    # Time Complexity (TC):
    # - Sorting takes O(n log n)
    # - The for loop processes each interval once → O(n)
    # - Total time complexity is O(n log n)

    # Space Complexity (SC):
    # - O(n) in the worst case, if no intervals overlap and each interval is added to the result
    # - Additional space is minimal beyond the output list


    def merge2(self, intervals: List[List[int]]) -> List[List[int]]: # for loop
        intervals.sort(key=lambda x:x[0]) # sort intervals by start of interval
        result = []

        start, end = intervals[0] # get initial start and end interval numbers
        for interval in intervals:
            currStart, currEnd = interval # get the current start and end

            if(currStart <= end): # see if there is an overlap
                end = max(end, currEnd) # update end of merged interval
            else: # if no overlap
                result.append([start, end]) # append the prev interval
                start, end = currStart, currEnd # update new start and end
        
        result.append([start, end]) # Append the last interval
        return result

sol = Solution()
print(sol.merge2([[1,3],[2,6],[8,10],[15,18]])) # [[1,6],[8,10],[15,18]]
print(sol.merge2([[1,4],[4,5]])) # [[1,5]]

#   0   1   2  3  4  5
#   a
# [-4, -1, -1, 0, 1, 2]
#       b            c





