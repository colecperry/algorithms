"""
Activity Selection Problem - Greedy Algorithm

This algorithm finds the maximum number of non-overlapping activities that can be scheduled from a given set of start and finish times.

Approach:
1. Sort activities by their finish time (greedy choice).
2. Select activities that do not overlap with the last selected activity.
3. Return the list of selected activities.

Time Complexity: O(n log n) due to sorting, then O(n) for selection, making it O(n log n) overall.
"""

def earliest_finish_time(intervals):
    """
    Function to select the maximum number of non-overlapping intervals.
    :param intervals: List of tuples (start_time, finish_time)
    :return: List of selected non-overlapping intervals
    """
    # Step 1: Sort intervals by finish time (Greedy approach)
    intervals.sort(key=lambda x: x[1])
    
    # Step 2: Select non-overlapping intervals
    selected_intervals = []
    last_finish_time = float('-inf')  # Initialize with negative infinity

    for start, finish in intervals:
        if start >= last_finish_time:  # Non-overlapping condition
            selected_intervals.append((start, finish))
            last_finish_time = finish  # Update last selected finish time
    
    return selected_intervals

# Test input
if __name__ == "__main__":
    activities = [(1, 3), (2, 5), (3, 9), (6, 8), (8, 11), (5, 7), (9, 12)]
    
    print("Given Activities:", activities)
    result = earliest_finish_time(activities)
    print("Selected Activities:", result)
