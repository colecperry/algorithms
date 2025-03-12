# 933. Number of Recent Calls

# Topics: Design, Queue, Data Stream

# You have a RecentCounter class which counts the number of recent requests within a certain time frame.

# Implement the RecentCounter class:

# RecentCounter() Initializes the counter with zero recent requests.
# int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
# It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.


# Example 1:

# Input
# ["RecentCounter", "ping", "ping", "ping", "ping"]
# [[], [1], [100], [3001], [3002]]
# Output
# [null, 1, 2, 3, 3]

# Explanation
# RecentCounter recentCounter = new RecentCounter();
# recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
# recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
# recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
# recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3

# How to solve:
    # Initialize a deque that represents the ele's that act as a sliding window for any ele's in the range of 3000 milliseconds
    # Ping() appends the next value to the deque, and uses a while loop to check if the the first ele is out of range, if so, it pops off the first ele and checks again since the next ele will now be at the 0th idx
    # Return the len of the sliding window since each ele represents 1 second

    # Time Complexity: O(1)
    # - Appending and returning the length is O(1).
    # - Removing outdated pings is amortized O(1) since each ping is only removed once in total, but worst-case O(N) since we could keep remove many pings if we have a back log

    # Space Complexity: O(1)
    # - The deque stores at most N (3000) timestamps, leading to O(N) space.
    # - However, in practice, it holds only pings within 3000ms, so it does not grow proportional to N -> O(1).

from collections import deque

class RecentCounter(object):

    def __init__(self):
        self.slide_window = deque()

    def ping(self, t):
        # step 1). append the current call to the deque
        self.slide_window.append(t)

        # step 2). invalidate the outdated pings
        while self.slide_window[0] < t - 3000:
            self.slide_window.popleft() # Pop the oldest ele

        return len(self.slide_window) # Each ele = 1 second


# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
print(obj.ping(1))
print(obj.ping(100))
print(obj.ping(3001))
print(obj.ping(3002))


