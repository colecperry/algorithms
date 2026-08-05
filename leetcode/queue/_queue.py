"""
=================================================================
QUEUE COMPLETE GUIDE
=================================================================

WHAT IS A QUEUE?
----------------
A Queue is a linear data structure that follows the First-In-First-Out (FIFO) principle.
Elements are added at the rear (enqueue) and removed from the front (dequeue), like a
line of people waiting — the first person in line is the first to be served.

Key characteristics:
- FIFO ordering: First element added is first to be removed
- O(1) enqueue (append) and dequeue (popleft) with collections.deque
- Monotonic variant (deque) enables O(n) sliding window extremes
- Fixed-capacity variant (circular buffer) enables true O(1) worst-case operations

Python implementation:
    from collections import deque
    queue = deque()
    queue.append(x)      # enqueue — O(1)
    queue.popleft()      # dequeue — O(1)
    queue[0]             # peek front — O(1)

NOTE ON SCOPE: A queue is also the engine behind BFS (tree level-order, grid shortest
path, multi-source spread, topological sort). Those patterns live in the dedicated
leetcode/bfs/_bfs.py and leetcode/graph/_graph.py guides — there, the queue is just
the mechanism and graph/tree exploration is the actual technique. This guide covers
problems where the queue's FIFO behavior IS the technique: eviction, turn-order
simulation, and design.

When to use Queue:
- Sliding window maximum/minimum (monotonic deque)
- Tracking "recent" events that expire after a time/count window
- Simulating a literal line/turn order where entities cycle to the back
- Implementing FIFO behavior on top of other structures (design problems)
- Building a fixed-capacity buffer with explicit front/rear bookkeeping

Common Queue problem types:
- Sliding window max/min with monotonic deque
- Expiring window: recent calls, moving average, hit counter
- Round-robin simulation: ticket lines, senate voting, circular games
- Queue-from-stacks / stack-from-queue design
- Circular queue / deque / bounded buffer design

QUEUE CORE PATTERNS
===================
"""

from typing import List
from collections import deque

"""
QUEUE COMPLEXITY REFERENCE
===========================

+---------------------------------+------------------+------------------+
| Pattern                         | Time             | Space            |
+---------------------------------+------------------+------------------+
| Monotonic Deque                 | O(n)             | O(k)             |
| Sliding Window Eviction         | O(n) amortized   | O(w)             |
| Queue Simulation / Round-Robin  | O(sum of turns)  | O(n)             |
| Queue via Two Stacks            | O(1) amortized   | O(n)             |
| Circular Queue (Fixed Buffer)   | O(1) per op      | O(k)             |
+---------------------------------+------------------+------------------+

n = number of elements/calls, k = window size or buffer capacity,
w = max entries live in the window at once, sum of turns = total steps
across all entities before the simulation ends (e.g. total tickets bought)

WHAT EACH PATTERN IS:
- Monotonic Deque: a deque kept in sorted order so the front is always the current
  window's max (or min) — used for sliding window max/min.
- Sliding Window Eviction: a queue of recent events where you just drop stale entries
  off the front — used for "how many things happened in the last X" problems.
- Queue Simulation / Round-Robin: a queue that models a literal line of people/turns,
  where an entry goes to the back if it still has work left.
- Queue via Two Stacks: two stacks used together to fake FIFO behavior, since a
  standard stack is LIFO — used in "implement a queue" design problems.
- Circular Queue (Fixed Buffer): a fixed-size array with wraparound indexing, so old
  slots get reused instead of the array growing — used for ring buffers.

NOTES:
- Monotonic deque: each index enters and exits at most once -> O(n) total
- Sliding window eviction: each entry enqueued once, evicted once -> amortized O(1) per call
- Queue simulation: an entity re-enters the queue each "turn" it still has work left;
  total work is bounded by the sum of turns needed across all entities, not just n
- Two stacks: each element crosses input -> output at most once -> amortized O(1) pop
- Circular buffer: fixed array + modulo arithmetic -> true O(1) worst case, no amortization needed
"""

"""
==============
QUEUE PATTERNS
==============
"""

"""
================================================================
PATTERN 1: MONOTONIC DEQUE (SLIDING WINDOW EXTREMES)
PATTERN EXPLANATION: Maintain a deque of indices whose values are in monotonically decreasing order. When the window slides, remove indices that fell outside the window from the front. Remove values from the back that can never be the window's maximum — any value smaller than the current element, added earlier, will always exit first. The front of the deque is always the index of the current window's maximum.

Applications: Sliding window maximum/minimum, shortest subarray with sum at least K, constrained subsequence sum, jump game VI.
================================================================
"""

class MonotonicDeque:
    """
    Given an array nums and window size k, return the max of each window
    as it slides from left to right.

    Example 1: nums=[1,3,-1,-3,5,3,6,7], k=3 -> [3,3,5,5,6,7]
    Example 2: nums=[1], k=1 -> [1]

    Giveaway: "max/min of every window of size k" (or "next greater/smaller
    element while scanning") is the signal for a monotonic deque — you need the
    extreme value at every position without rescanning the whole window each time.
    """
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:  # LC 239
        """
        TC: O(n) - each index pushed and popped at most once
        SC: O(k) - deque stores at most k indices
        """
        result = []
        deq = deque()  # Stores indices, values in decreasing order

        for i in range(len(nums)):
            window_start = i - k + 1 # calc start of sliding window

            # front index fell out of the window (window too big) -> drop it
            if deq and deq[0] < window_start:
                deq.popleft()

            # anything smaller than nums[i] can never be a future max -> drop it
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()

            # nums[i] is now a candidate max -> add its index
            deq.append(i)

            # window has reached size k -> front of deque is this window's max, record it
            if i >= k - 1:
                result.append(nums[deq[0]])

        return result

    # Trace: nums=[1,3,-1,-3,5,3,6,7], k=3
    # i=0 (1):  deq=[0]
    # i=1 (3):  3>1 pop 0 -> deq=[1]
    # i=2 (-1): deq=[1,2], window full -> result=[3]
    # i=3 (-3): deq=[1,2,3], result=[3,3]
    # i=4 (5):  5>-3 pop 3, 5>-1 pop 2, 5>3 pop 1 -> deq=[4], result=[3,3,5]
    # i=5 (3):  deq=[4,5], result=[3,3,5,5]
    # i=6 (6):  6>3 pop 5, 6>5 pop 4 -> deq=[6], result=[3,3,5,5,6]
    # i=7 (7):  7>6 pop 6 -> deq=[7], result=[3,3,5,5,6,7] ✓

sol = MonotonicDeque()
print("Sliding Window Max:", sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))  # [3,3,5,5,6,7]
print("Sliding Window Max:", sol.maxSlidingWindow([1], 1))  # [1]


"""
================================================================
PATTERN 2: SLIDING WINDOW EVICTION (EXPIRING QUEUE)
PATTERN EXPLANATION: Maintain a queue of recent events (timestamps or values). Before answering each new query, evict entries from the FRONT that have fallen outside the valid window — no ordering or comparison is needed, just "is this entry still within range." This differs from the monotonic deque: nothing is ever removed from the back, because every entry is equally "in" or "out" of the window based purely on age.

Applications: Number of recent calls, moving average from data stream, design hit
counter, logger rate limiter.
================================================================
"""

class RecentCounter:
    """
    Giveaway: "count events/requests in the past X ms/seconds" with calls arriving
    in increasing time order — you only ever need to drop stale entries off one
    end, never compare values, which is the tell for a plain expiring queue
    rather than a monotonic deque.

    Problem: Count the number of requests that have happened in the past 3000ms
    (inclusive), given that ping() is always called with a strictly increasing t.

    Example:
        ping(1)    -> 1   (requests in [-2999, 1] = [1])
        ping(100)  -> 2   (requests in [-2900, 100] = [1, 100])
        ping(3001) -> 3   (requests in [1, 3001] = [1, 100, 3001])
        ping(3002) -> 3   (requests in [2, 3002] = [100, 3001, 3002], 1 expired)

    Steps:
    1. Maintain a deque of timestamps seen so far
    2. On each ping(t): append t (new pings are always the current max, so the
       deque is naturally sorted — no need to search for insertion point)
    3. While the front timestamp is older than t - 3000, popleft it (expired)
    4. Return the deque's length — every remaining entry is within the window
    """
    def __init__(self):  # LC 933 - Number of Recent Calls
        self.window = deque()

    def ping(self, t: int) -> int:
        """
        TC: O(1)
            - Appending and returning the length is O(1).
            - Removing outdated pings is amortized O(1) since each ping is only removed once in total, but worst-case O(N) since we could keep remove many pings if we have a back log
        
        SC: O(1)
            - The deque stores at most N (3000) timestamps, leading to O(N) space.
            - However, in practice, it holds only pings within 3000ms, so it does not grow proportional to N -> O(1).
        """
        # step 1). append the current call to the deque
        self.window.append(t)

        # step 2). invalidate the outdated pings
        while self.window[0] < t - 3000:
            self.window.popleft() # Pop the oldest ele if outside window

        return len(self.window) # Each ele = 1 second

    # Trace: ping(1), ping(100), ping(3001), ping(3002)
    # ping(1):    window=[1],              front=1 >= 1-3000=-2999    -> return 1
    # ping(100):  window=[1,100],          front=1 >= 100-3000=-2900  -> return 2
    # ping(3001): window=[1,100,3001],     front=1 >= 3001-3000=1     -> return 3
    # ping(3002): window=[1,100,3001,3002],front=1 < 3002-3000=2 -> evict 1
    #             window=[100,3001,3002],  front=100 >= 2             -> return 3 ✓

rc = RecentCounter()
print("Recent Calls:", [rc.ping(1), rc.ping(100), rc.ping(3001), rc.ping(3002)])  # [1, 2, 3, 3]


"""
================================================================
PATTERN 3: QUEUE SIMULATION / ROUND-ROBIN PROCESSING
PATTERN EXPLANATION: Model a literal turn-order process with a queue. Dequeue the
entity at the front, process one "turn" of work for it, and requeue it at the back
if it still has work left; entities that finish leave for good. There is no graph or
distance being explored — the queue purely encodes "who goes next," and the same
entity can cycle through the queue many times.

Applications: Time needed to buy tickets, number of students unable to eat lunch,
Dota2 senate, reveal cards in increasing order, find the winner of the circular game.
================================================================
"""

class QueueSimulation:
    """
    Giveaway: the problem literally describes people/entities taking turns in a
    line and going to the back if they still have work left — no distances or
    graph edges involved, just "who goes next," which is the signal to simulate
    with a plain queue instead of BFS.

    Problem: n people stand in line to buy tickets; tickets[i] is how many tickets
    person i wants. Each purchase takes 1 second, and a person who still has
    tickets left to buy goes to the back of the line instead of leaving. Return the
    time for the person initially at position k to finish buying all their tickets.

    Example:
        tickets = [2, 3, 2], k = 2
        [2,3,2] -> [3,2,1] -> [2,1,2] -> [1,2,1] -> [2,1] -> [1,1] -> [1]
        Output: 6

    Steps:
    1. Enqueue every person's INDEX (not their ticket count) so k stays trackable
       as people cycle through the line
    2. While queue not empty:
       a. Increment time by 1 (one ticket purchase)
       b. Dequeue the front index, decrement its ticket count
       c. If this was person k and their tickets hit 0, return time
       d. Otherwise, if tickets remain, requeue this index at the back
    """
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:  # LC 2073
        """
        TC: O(sum(tickets)) - one iteration per ticket purchased across everyone
        SC: O(n) - queue holds at most n indices
        """
        queue = deque(range(len(tickets)))
        time = 0

        while queue:
            time += 1
            i = queue.popleft()
            tickets[i] -= 1

            if i == k and tickets[i] == 0:
                return time

            if tickets[i] > 0:
                queue.append(i)

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


"""
================================================================
PATTERN 4: QUEUE VIA TWO STACKS (AMORTIZED DESIGN)
PATTERN EXPLANATION: Simulate FIFO queue behavior using two LIFO stacks. The input
stack receives all pushes. On pop/peek, if the output stack is empty, transfer all
elements from input to output (reversing their order once). Because each element is
transferred at most once total, pop is O(1) amortized even though a single transfer
can cost O(n). The mirror version (stack from two queues) uses the same idea in
reverse to simulate LIFO behavior on top of FIFO primitives.

Applications: Implement queue using stacks, implement stack using queues.
================================================================
"""

class QueueWithStacks:
    """
    Giveaway: the problem explicitly says "implement a queue using stacks" (or
    vice versa) — it names the two ADTs directly, so the task is translating one
    access order into the other rather than discovering a hidden pattern.

    Problem: Implement a FIFO queue using only two stacks. Support push, pop, peek,
    and empty in O(1) amortized time.

    Example:
        push(1), push(2)
        peek()  -> 1
        pop()   -> 1
        empty() -> False

    Steps:
    1. Two stacks: input_stack (accepts all pushes), output_stack (serves pops/peeks)
    2. push: append to input_stack — O(1)
    3. pop/peek: if output_stack empty, transfer everything from input_stack
       Each element crosses input -> output at most once -> amortized O(1)
    """
    def __init__(self):  # LC 232 - Implement Queue using Stacks
        self.input_stack = []
        self.output_stack = []

    def push(self, x: int) -> None:
        """TC: O(1)"""
        self.input_stack.append(x)

    def pop(self) -> int:
        """TC: O(1) amortized"""
        self._transfer()
        return self.output_stack.pop()

    def peek(self) -> int:
        """TC: O(1) amortized"""
        self._transfer()
        return self.output_stack[-1]

    def empty(self) -> bool:
        """TC: O(1)"""
        return not self.input_stack and not self.output_stack

    def _transfer(self):
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())

    # Trace: push(1), push(2), peek(), pop()
    # After pushes: input=[1,2], output=[]
    # peek(): output empty -> transfer: input=[], output=[2,1]
    #         output[-1] = 1 (front of queue) ✓
    # pop():  output=[2,1] -> pop -> return 1, output=[2]

q = QueueWithStacks()
q.push(1)
q.push(2)
print("Peek:", q.peek())    # 1
print("Pop:", q.pop())      # 1
print("Empty:", q.empty())  # False


"""
================================================================
PATTERN 5: CIRCULAR QUEUE (FIXED-CAPACITY BUFFER)
PATTERN EXPLANATION: Implement a queue over a fixed-size array using modulo
arithmetic to wrap front/rear pointers around, instead of shifting elements or
letting the array grow unbounded. This is the raw ADT mechanic that a deque hides
behind O(1) append/popleft — made explicit here for design problems that require a
bounded buffer with true O(1) worst-case operations (no amortization).

Applications: Design circular queue, design circular deque, design front middle
back queue, any fixed-size ring buffer.
================================================================
"""

class MyCircularQueue:
    """
    Giveaway: the problem says "design a circular queue/deque" with a fixed
    capacity k — a bounded size plus required O(1) worst-case (not amortized)
    ops signals a fixed array with wraparound indices, not a growable deque.

    Problem: Design a circular queue with fixed capacity k supporting enQueue,
    deQueue, Front, Rear, isEmpty, and isFull, all in O(1).

    Example:
        q = MyCircularQueue(3)
        q.enQueue(1) -> True     q.enQueue(2) -> True     q.enQueue(3) -> True
        q.enQueue(4) -> False    (full)
        q.Rear()     -> 3
        q.deQueue()  -> True     (frees a slot)
        q.enQueue(4) -> True     (reuses the freed slot via wraparound)
        q.Rear()     -> 4

    Steps:
    1. Track capacity, a fixed array of size k, front_idx, and a running count
       (count replaces the need for a "rear" pointer and disambiguates full vs empty)
    2. enQueue: if full, fail; else write to (front_idx + count) % capacity, count += 1
    3. deQueue: if empty, fail; else front_idx = (front_idx + 1) % capacity, count -= 1
    4. Front/Rear: read at front_idx / (front_idx + count - 1) % capacity
    """
    def __init__(self, k: int):  # LC 622 - Design Circular Queue
        self.capacity = k
        self.queue = [0] * k
        self.front_idx = 0
        self.count = 0

    def enQueue(self, value: int) -> bool:
        """TC: O(1)"""
        if self.isFull():
            return False
        rear_idx = (self.front_idx + self.count) % self.capacity
        self.queue[rear_idx] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        """TC: O(1)"""
        if self.isEmpty():
            return False
        self.front_idx = (self.front_idx + 1) % self.capacity
        self.count -= 1
        return True

    def Front(self) -> int:
        """TC: O(1)"""
        if self.isEmpty():
            return -1
        return self.queue[self.front_idx]

    def Rear(self) -> int:
        """TC: O(1)"""
        if self.isEmpty():
            return -1
        rear_idx = (self.front_idx + self.count - 1) % self.capacity
        return self.queue[rear_idx]

    def isEmpty(self) -> bool:
        """TC: O(1)"""
        return self.count == 0

    def isFull(self) -> bool:
        """TC: O(1)"""
        return self.count == self.capacity

    # Trace: capacity=3
    # enQueue(1): rear=(0+0)%3=0 -> queue=[1,_,_], count=1
    # enQueue(2): rear=(0+1)%3=1 -> queue=[1,2,_], count=2
    # enQueue(3): rear=(0+2)%3=2 -> queue=[1,2,3], count=3
    # enQueue(4): isFull (count==capacity) -> False
    # Rear(): rear_idx=(0+3-1)%3=2 -> queue[2]=3
    # deQueue(): front_idx=(0+1)%3=1, count=2
    # enQueue(4): rear=(1+2)%3=0 -> queue=[4,2,3], count=3 (wrapped around)
    # Rear(): rear_idx=(1+3-1)%3=0 -> queue[0]=4 ✓

cq = MyCircularQueue(3)
print("enQueue(1):", cq.enQueue(1))  # True
print("enQueue(2):", cq.enQueue(2))  # True
print("enQueue(3):", cq.enQueue(3))  # True
print("enQueue(4):", cq.enQueue(4))  # False (full)
print("Rear:", cq.Rear())            # 3
print("deQueue:", cq.deQueue())      # True
print("enQueue(4):", cq.enQueue(4))  # True
print("Rear:", cq.Rear())            # 4
