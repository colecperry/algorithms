"""
Activity Selection Problem - Greedy Algorithm

This algorithm finds the maximum number of non-overlapping activities that can be scheduled from a given set of start and finish times. 

Approach:
1. Sort activities by their finish time (greedy choice).
2. Select activities that do not overlap with the last selected activity.
3. Return the list of selected activities.

Time Complexity: O(n log n) due to sorting the intervals array by finish time, then O(n) for iterating through the array once and selecting the non overlapping intervals, making it O(n log n) overall.

How we would have known to sort by finish time:
1. Sorting by Start Time - If we sort by start time, we might pick an activity that lasts a long time, blocking many other potential activities. Example: If we choose an activity that starts early but finishes very late, we might miss several shorter ones that could fit in the same time frame.
2. Sorting by Duration (Shortest Job First)- Choosing the shortest activities first doesn’t guarantee that we can fit the most activities overall. A short activity might overlap with many others, limiting our choices.
3. Sorting by Finish Time (Best Choice - If we always pick the activity that finishes the earliest, we free up space for as many future activities as possible. This greedy approach ensures we fit the maximum number of activities. So we make the greedy decision at the for each choice, which means sorting my finish times.
"""

def earliest_finish_time(intervals):
    # Step 1: Sort intervals by finish time
    intervals.sort(key=lambda x: x[1])  
    
    # Step 2: Select non-overlapping intervals
    selected_intervals = []
    last_finish_time = float('-inf')

    for start, finish in intervals:
        if start >= last_finish_time:  # Non-overlapping condition
            selected_intervals.append((start, finish)) # Append interval
            last_finish_time = finish  # Update last finish time

    return selected_intervals

# Example Usage:
intervals = [(1, 3), (2, 5), (3, 9), (6, 8), (8, 9)]
optimal_schedule = earliest_finish_time(intervals)

# Print the result
print("Optimal Schedule:", optimal_schedule)
