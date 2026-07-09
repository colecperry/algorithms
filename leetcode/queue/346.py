# 346. Moving Average from Data Stream

# Topics: Array, Design, Queue, Data Stream

# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

# Implement the MovingAverage class:

# MovingAverage(int size) Initializes the object with the size of the window size.
# double next(int val) Returns the moving average of the last size values of the stream.

# Example 1:
# Input
# ["MovingAverage", "next", "next", "next", "next"]
# [[3], [1], [10], [3], [5]]
# Output
# [null, 1.0, 5.5, 4.66667, 6.0]

# Explanation
# MovingAverage movingAverage = new MovingAverage(3);
# movingAverage.next(1); // return 1.0 = 1 / 1
# movingAverage.next(10); // return 5.5 = (1 + 10) / 2
# movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
# movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3

# How to solve: (with list)
    # Use a queue of "size" and sum the queue to find the average
    # Use the next() function to check if size is at capacity, then pop off the first element
    # Append the next ele and return the sum

    # Time complexity is O(n): Popping is O(n) since all elements must move left one index, and summing is O(n)
    # Space complexity is O(n): the queue stores at most "size" elements, O(size) = O(n)


class MovingAverage(object):

    def __init__(self, size):
        self.size = size # Max size of the queue
        self.queue = [] # Actual queue
        

    def next(self, val):
        if len(self.queue) == self.size: # If queue at max window size
            self.queue.pop(0) # Pop off first ele
        self.queue.append(val) # Append val to queue
        return float(sum(self.queue))/len(self.queue) # Return sum of queue
    
# How to solve (with deque):
    # Initialize a deque with a max size and a window sum
    # If the len of the queue is equal to the size, subtract the oldest ele's val from the window sum
    # Append the new ele to the deque, which automatically removes the oldest ele if we reach max len
    # Update the window sum by adding the new ele
    # Return the average of the window

    # Time complexity: O(1) because popping is O(1) with a deque because it uses a doubly linked list internally, and since we use a running sum we don't have to iterate O(n) times for the sum() fn
    # Space complexity: O(n) because the deque stores at least "size" elements where n is the window size
    
from collections import deque

class MovingAverageOptimized:
    def __init__(self, size: int):
        self.size = size  # Max size of the window
        self.queue = deque(maxlen=size)  # Use deque with max size
        self.window_sum = 0  # Store the sum of elements in the current window

    def next(self, val: int) -> float:
        if len(self.queue) == self.size:
            self.window_sum -= self.queue[0]  # Subtract the outgoing element from sum - always at index 0 because of size 3 queue

        self.queue.append(val)  # Adding new ele manually removes the oldest ele when it reaches max len
        self.window_sum += val  # Update sum with new element

        return self.window_sum / len(self.queue)  # Compute and return the average

# Your MovingAverage object will be instantiated and called as such:
obj = MovingAverageOptimized(3)
print(obj.next(1))
print(obj.next(10))
print(obj.next(3))
print(obj.next(5))
