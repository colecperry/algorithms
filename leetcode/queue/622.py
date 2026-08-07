# 622. Design Circular Queue

# Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle, and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

# One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

# Implement the MyCircularQueue class:

# MyCircularQueue(k) Initializes the object with the size of the queue to be k.
# int Front() Gets the front item from the queue. If the queue is empty, return -1.
# int Rear() Gets the last item from the queue. If the queue is empty, return -1.
# boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
# boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
# boolean isEmpty() Checks whether the circular queue is empty or not.
# boolean isFull() Checks whether the circular queue is full or not.
# You must solve the problem without using the built-in queue data structure in your programming language. 
 

# Example 1:
# Input
# ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
# [[3], [1], [2], [3], [4], [], [], [], [4], []]
# Output
# [null, true, true, true, false, 3, true, true, true, 4]

# Explanation
# MyCircularQueue myCircularQueue = new MyCircularQueue(3);
# myCircularQueue.enQueue(1); // return True
# myCircularQueue.enQueue(2); // return True
# myCircularQueue.enQueue(3); // return True
# myCircularQueue.enQueue(4); // return False
# myCircularQueue.Rear();     // return 3
# myCircularQueue.isFull();   // return True
# myCircularQueue.deQueue();  // return True
# myCircularQueue.enQueue(4); // return True
# myCircularQueue.Rear();     // return 4

# Giveaway: the problem says "design a circular queue/deque" with a fixed
# capacity k — a bounded size plus required O(1) worst-case (not amortized)
# ops signals a fixed array with wraparound indices, not a growable deque.

class MyCircularQueue:
    def __init__(self, k: int):  # LC 622 - Design Circular Queue
        self.capacity = k # max number of elements the queue can hold
        self.queue = [0] * k # fixed-size backing array
        self.front_idx = 0 # index of the current front element
        self.count = 0 # running count replaces need for a rear pointer

    def enQueue(self, value: int) -> bool:
        """TC: O(1)"""
        if self.isFull(): # Early exit -> queue is full
            return False
        rear_idx = (self.front_idx + self.count) % self.capacity # get next open slot, wrapping around
        self.queue[rear_idx] = value # assign that value to the open slot (rear index)
        self.count += 1
        return True

    def deQueue(self) -> bool:
        """TC: O(1)"""
        if self.isEmpty(): # Operation not successful -> Return False
            return False
        self.front_idx = (self.front_idx + 1) % self.capacity # advance front index, wrapping around
        self.queue[self.front_idx - 1] = 'EMPTY' # Just for visual/debugging effect
        self.count -= 1
        return True

    def Front(self) -> int:
        """TC: O(1)"""
        if self.isEmpty():
            return -1
        return self.queue[self.front_idx] # element at front_idx is the front

    def Rear(self) -> int:
        """TC: O(1)"""
        if self.isEmpty():
            return -1
        rear_idx = (self.front_idx + self.count - 1) % self.capacity # get last filled slot, wrapping around
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