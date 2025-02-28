"""
Greedy Algorithm for Scheduling Jobs to Minimize Maximum Lateness

This algorithm schedules jobs with deadlines in a way that minimizes the maximum lateness.

Approach (Earliest Deadline First - EDF):
1. Sort the jobs by their deadline in ascending order (greedy choice).
2. Process jobs in this sorted order, keeping track of the current time.
3. Calculate the lateness of each job and track the maximum lateness.

Time Complexity: O(n log n) due to sorting, then O(n) for scheduling, making it O(n log n) overall.
"""

def earliest_deadline_first(jobs):
    """
    Function to schedule jobs to minimize maximum lateness.
    :param jobs: List of tuples (processing_time, deadline)
    :return: Maximum lateness and the job schedule
    """
    # Step 1: Sort jobs by deadline (Greedy approach)
    jobs.sort(key=lambda x: x[1])
    
    # Step 2: Schedule jobs and track lateness
    current_time = 0
    max_lateness = 0
    schedule = []  # Stores the order of scheduled jobs

    for processing_time, deadline in jobs:
        current_time += processing_time  # Process job
        lateness = max(0, current_time - deadline)  # Compute lateness
        max_lateness = max(max_lateness, lateness)  # Track max lateness
        schedule.append((processing_time, deadline))
    
    return max_lateness, schedule

# Test input
if __name__ == "__main__":
    test_jobs = [(3, 9), (2, 5), (1, 2), (5, 8)]  # (processing_time, deadline)
    
    print("Given Jobs:", test_jobs)
    lateness, job_schedule = earliest_deadline_first(test_jobs)
    print("Scheduled Jobs:", job_schedule)
    print("Maximum Lateness:", lateness)