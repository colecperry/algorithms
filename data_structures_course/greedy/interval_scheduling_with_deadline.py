"""
Greedy Algorithm for Scheduling Jobs to Minimize Maximum Lateness: We are given a set of n jobs, all of which must be scheduled on a single resource. We are given n jobs, each with a processing time, and a deadline. This algorithm schedules jobs with deadlines in a way that minimizes the maximum lateness.

Approach (Earliest Deadline First - EDF):
1. Sort the jobs by their deadline in ascending order (greedy choice) to ensure we handle the most urgent jobs first and ensures we're making the best local decision
2. Process jobs in this sorted order, keeping track of the current time.
3. Calculate the lateness of each job and track the maximum lateness.

Time Complexity: O(n log n) due to sorting, then O(n) looping through the jobs and calcuating lateness, making it O(n log n) overall.
"""

def earliest_deadline_first(jobs):
    # Sort jobs by deadline
    jobs.sort(key=lambda x: x[1]) # Sort by deadline
    
    current_time = 0 # Track when job finishes
    max_lateness = 0 # Stores the worst lateness observed
    schedule = []  # Stores the order of scheduled jobs
    
    for job_time, deadline in jobs:
        current_time += job_time  # Add time required to process a job to total processing time
        lateness = max(0, current_time - deadline) # Lateness for each job: 0 or calculate
        max_lateness = max(max_lateness, lateness) # Store max lateness encountered so far
        schedule.append((job_time, deadline)) # Store the schedule order
    
    return max_lateness, schedule

# Example usage
jobs = [(3, 9), (2, 5), (1, 6), (4, 7), (5, 10)]
max_lateness, schedule = earliest_deadline_first(jobs)
print("Maximum lateness:", max_lateness)
print("Job schedule:", schedule)