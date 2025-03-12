# 2073. Time Needed to Buy Tickets

# Topics: Array, Queue, Simulation

# There are n people in a line queuing to buy tickets, where the 0th person is at the front of the line and the (n - 1)th person is at the back of the line.

# You are given a 0-indexed integer array tickets of length n where the number of tickets that the ith person would like to buy is tickets[i].

# Each person takes exactly 1 second to buy a ticket. A person can only buy 1 ticket at a time and has to go back to the end of the line (which happens instantaneously) in order to buy more tickets. If a person does not have any tickets left to buy, the person will leave the line.

# Return the time taken for the person initially at position k (0-indexed) to finish buying tickets.


# Example 1:
# Input: tickets = [2,3,2], k = 2
# Output: 6

# Explanation:
# The queue starts as [2,3,2], where the kth person is underlined.
# After the person at the front has bought a ticket, the queue becomes [3,2,1] at 1 second.
# Continuing this process, the queue becomes [2,1,2] at 2 seconds.
# Continuing this process, the queue becomes [1,2,1] at 3 seconds.
# Continuing this process, the queue becomes [2,1] at 4 seconds. Note: the person at the front left the queue.
# Continuing this process, the queue becomes [1,1] at 5 seconds.
# Continuing this process, the queue becomes [1] at 6 seconds. The kth person has bought all their tickets, so return 6.

# Example 2:
# Input: tickets = [5,1,1,1], k = 0
# Output: 8

# Explanation:
# The queue starts as [5,1,1,1], where the kth person is underlined.
# After the person at the front has bought a ticket, the queue becomes [1,1,1,4] at 1 second.
# Continuing this process for 3 seconds, the queue becomes [4] at 4 seconds.
# Continuing this process for 4 seconds, the queue becomes [] at 8 seconds. The kth person has bought all their tickets, so return 8.

# How to Solve (Deque):
    # Big Picture: We use a deque to store the original indexes, we pop from the front and append to the back, and we maintain tickets in it's original array and decrement from there
    # If we simply used tickets, turned it into a deque and popped/appended from there, tracking k becomes tricky each loop 
    # Initialize a deque with indexes so we can track which person is at the front, and move them
    # Loop through the deque
        # Increment time by 1
        # Dequeue to get index of next person in line
        # Decrement the ticket by 1 at that index
            # If the index we popped is the front and the tickets at front == 0, person at index k has bought all their tickets, return time
            # If not, append the index to the end of the queue
    
    # Time Complexity:
    # - Each person buys exactly tickets[i] tickets.
    # - In each iteration, we pop from the queue (O(1)) and append back if necessary (O(1)).
    # - The total number of operations is proportional to the sum of all tickets.
    # - Therefore, the worst-case time complexity is **O(sum(tickets))**
        # If we had [1,1,1,1,1] -> total operations = 5
        # If we had [1000, 500, 2000, 300], total operations = 3800

    # Space Complexity:
    # - We store the indices of people in a queue.
    # - In the worst case, the queue stores all n people, giving us **O(n)** space.
    # - The `tickets` array is modified in place, so no additional space is needed for it.
    # - Hence, the overall space complexity is **O(n)**.

# How to Solve (One pass):
    # Case 1: 
        # The index we are iterating (i) has not passed k (before or equal to k) -> This means the person at index i can only buy either the minimum of tickets[i] or tickets[k]
            # tickets = [1,3,2], k = 2 -> person at index 0 can only buy 1 ticket (tickets[i])
            # tickets = [3,3,2], k = 2 -> person at index 0 can only buy 2 tickets (tickets[k])
    # Case 2: 
        # The index we are iterating (i) has passed k -> This means the person at index i can only buy either the minimum of tickets[i] or tickets[k] - 1
            # tickets = [5,3,2], k = 0, -> person at index 1 can only buy 3 tickets (tickets[i])
            # tickets = [2,3,3], k = 0, -> person at index 1 can only 1 ticket (tickets[k] - 1)

    # Time Complexity: O(n) -> Iterating once
    # Space Complexity: O(1) -> No data structures

from collections import deque

def timeRequiredToBuy(tickets, k):
            queue = deque()

            # Initialize the queue with ticket indices
            for i in range(len(tickets)):
                queue.append(i)

            time = 0

            # Loop until the queue is empty
            while queue:
                # Increment the time counter for each iteration
                time += 1

                # Get the front index and dequeue
                front = queue.popleft()

                # Decrement the ticket at the index we popped
                tickets[front] -= 1

                # If person k bought all their tickets, return time
                if k == front and tickets[front] == 0:
                    return time

                # Re-add the current index to the queue for the next iteration
                if tickets[front] != 0:
                    queue.append(front)

            return time

def timeRequiredToBuy2(tickets, k):
        seconds = 0
        for i in range(len(tickets)):
            if i <= k: # If index has not passed k or == k
                seconds += min(tickets[i], tickets[k]) # Get the min and add to the result
            else: # Index has passed k
                seconds += min(tickets[i], tickets[k] - 1)
        return seconds


print(timeRequiredToBuy([2,3,2], 2))
print(timeRequiredToBuy([5,1,1,1], 0))