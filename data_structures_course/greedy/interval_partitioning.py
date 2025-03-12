"""
Greedy Algorithm for Interval Partitioning

This algorithm finds the minimum number of resources required to schedule intervals 
without overlapping.

Approach (Earliest Start Time First):
1. Sort the intervals by their start time (greedy choice).
2. Use a min-heap to track the end times of currently used resources.
3. Allocate a new resource if no existing resource is available at the interval’s start time.
4. Return the maximum number of resources used at any time.

Time Complexity: O(n log n) due to sorting and heap operations.
"""

import heapq

def interval_partitioning(intervals):
    """
    Function to determine the minimum number of resources needed.
    :param intervals: List of tuples (start_time, end_time)
    :return: Minimum number of resources required
    """
    # Step 1: Sort intervals by start time (Greedy approach)
    intervals.sort(key=lambda x: x[0])
    
    # Min heap to track end times of resources in use
    resources = []
    allocation = []  # Stores the number of active resources at each step

    for start, end in intervals:
        if resources and resources[0] <= start:
            # Reuse the earliest available resource
            heapq.heappop(resources)
        
        # Assign this interval a resource
        heapq.heappush(resources, end)
        allocation.append(len(resources))  # Number of active resources at this step
    
    return max(allocation)  # Minimum number of resources needed

# Test input
if __name__ == "__main__":
    test_intervals = [(0, 3), (1, 4), (2, 5), (6, 9), (7, 10), (8, 11)]
    
    print("Given Intervals:", test_intervals)
    min_resources = interval_partitioning(test_intervals)
    print("Minimum Resources Needed:", min_resources)
