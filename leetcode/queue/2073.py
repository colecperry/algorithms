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


from collections import deque
from typing import List

class QueueSimulation:
    """
    Giveaway: the problem literally describes people/entities taking turns in a
    line and going to the back if they still have work left — no distances or
    graph edges involved, just "who goes next," which is the signal to simulate
    with a plain queue instead of BFS.

    """
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:  # LC 2073
        """
        TC: O(sum(tickets)) - one iteration per ticket purchased across everyone
        SC: O(n) - queue holds at most n indices
        """
        queue = deque(range(len(tickets))) # queue maintains order while cycling
        time = 0 # result = time it takes person k to buy all tickets

        while queue: # while there are still people that need to buy tix
            time += 1
            i = queue.popleft() # get the index of the person buying the ticket
            tickets[i] -= 1 # buy a ticket

            # check if person k & their tickets hit zero
            if i == k and tickets[i] == 0: 
                return time

            if tickets[i] > 0: # if time remains (still need tickets)
                queue.append(i) # requeue this index to the back of the q

        return time

    # Trace: tickets=[2,3,2], k=2
    # queue=[0,1,2]
    # t=1: pop 0, tickets=[1,3,2], not k, requeue -> queue=[1,2,0]
    # t=2: pop 1, tickets=[1,2,2], not k, requeue -> queue=[2,0,1]
    # t=3: pop 2, tickets=[1,2,1], i==k but tickets[2]=1 != 0, requeue -> queue=[0,1,2]
    # t=4: pop 0, tickets=[0,2,1], not k, tickets[0]==0 so don't requeue -> queue=[1,2]
    # t=5: pop 1, tickets=[0,1,1], not k, requeue -> queue=[2,1]
    # t=6: pop 2, tickets=[0,1,0], i==k and tickets[2]==0 -> return 6 ✓

sol = QueueSimulation()
print("Time to Buy Tickets:", sol.timeRequiredToBuy([2,3,2], 2))  # 6
print("Time to Buy Tickets:", sol.timeRequiredToBuy([5,1,1,1], 0))  # 8