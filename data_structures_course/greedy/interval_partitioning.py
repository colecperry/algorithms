"""
Greedy Algorithm for Interval Partitioning: Interval partitioning is about grouping overlapping intervals into the fewest possible groups so that no two intervals in the same group overlap. Key idea:
    - If two intervals overlap, they must be in different groups
    - Our goal is to use the minimum number of groups (also called "resources" or "rooms)
    - The maximum number of overlapping intervals at any time tells us the minimum number of groups needed.

ex. Say we have 5 activites represented by (start time, finish time):
(1, 4), (2, 5), (3, 6), (7, 8), (8, 9)

Drawn on a timeline, we see:
Time:  1---2---3---4---5---6---7---8---9
Activity 1: [------]  
Activity 2:    [------]  
Activity 3:       [------]  
Activity 4:                [---]  
Activity 5:                    [---]  

- At time 3 we have 3 overlapping intervals -> these must be in different groups. At time 7-8, only one interval is active.

Approach (Earliest Start Time First):
1. Sort the intervals by their start time (greedy choice)
2. Use a min-heap to track the end times of currently used resources.
3. Allocate a new resource if no existing resource is available at the interval’s start time.
4. Return the maximum number of resources used at any time.

# Big picture: Sort the list of intervals by start time which ensures we're not missing opportuities to re-use rooms or resources at each step. Use a min heap to store end times of each interval, and track the number of rooms in use at each interval. Loop through the interval, and add the first finish time to the heap. Continue to the second interval -> If the value at index 0 in the min heap (the soonest available finish time of a resource) is less than the start time of the next interval, we can "re-use" that room, so we can pop off the interval in the min heap and add the new one (only add finish time). If the end time of the soonest avaiable resource is greater than the interval we are processing's start time, we can't re-use that room, so we need to create another. Return the max number of rooms used at any point during the process.

Time Complexity: O(log n) to sort by start time, loop through the intervals = O(n), total time complexity = O(n log n)
"""

import heapq

def interval_partitioning(intervals):
    '''This algorithm finds the minimum number of resources required to schedule intervals without overlapping.
    '''
    # Sort intervals by start time ensures we're not missing opportunities to re-use rooms
    intervals.sort(key=lambda x: x[0])
    
    resources = [] # Min heap to track end times -> ensures we remove earliest available resource first
    allocation = []  # Tracks how many active resources are used at each processing step
    
    for start, end in intervals:
        if resources and resources[0] <= start: # Check if earliest resource (smallest finish time) is free
            heapq.heappop(resources) # Reuse the earliest available resource
        
        heapq.heappush(resources, end) # Push new interval's finish time into the heap
        allocation.append(len(resources))  # Store the number of resources in use after assigning the interval -> len(resources) represents the number of overlapping intervals at that moment
    
    return max(allocation)  # Minimum number of resources needed is the maximum number of overlapping intervals at any time

# Example usage
intervals = [(0, 3), (1, 2), (2, 5), (4, 6), (5, 8), (6, 9), (7, 10)]
min_resources = interval_partitioning(intervals)
print("Minimum resources needed:", min_resources)
