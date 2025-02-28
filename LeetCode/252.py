# 252. Meeting Rooms

# Topics: Array, Sorting

# Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

# Example 1:
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: false

# Example 2:
# Input: intervals = [[7,10],[2,4]]
# Output: true

# How to Solve:
    # Sort the list of lists which sorts them by first index
    # Starting from the first index, check if the start time of the current index is less than the end time of the prev index -> return False
    # If we loop through every list of lists, and the above condition is not met, we return True because the person will be able to attend all meetings

class Solution(object):
    def canAttendMeetings(self, intervals):
        intervals.sort()
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False
        return True

my_solution = Solution()
arr, arr2 = [[0,30],[5,10],[15,20]], [[7,10],[2,4]]


print(my_solution.canAttendMeetings(arr))
print(my_solution.canAttendMeetings(arr2))