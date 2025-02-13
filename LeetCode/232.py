# 232. Implement Queue using Stacks

# Topics - Stack, Design, Queue

# Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

# Implement the MyQueue class:

# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.
# Notes:

# You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

# Example 1:
# Input
# ["MyQueue", "push", "push", "peek", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 1, 1, false]

# Explanation
# MyQueue myQueue = new MyQueue();
# myQueue.push(1); // queue is: [1]
# myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
# myQueue.peek(); // return 1
# myQueue.pop(); // return 1, queue is [2]
# myQueue.empty(); // return false

# How to solve: O(n)
    # To push an element into the queue, it is the same as pushing an element into the stack. If we want to pop an element from the queue (removes the front element), we can only use standard operations of a stack which means we can't dequeue from the front. To accomplish a queue dequeue using only stack operations and two stacks, we can pop each ele from the stack and push it into the other stack, where we get the same list reverse ordered. stack1 -> [1,2,3,4] -> pop & push 4,3,2,1 -> stack2 [4,3,2,1]. Now if we pop using stack operations, it would remove 1, which is the element we need to remove for the queue dequeue. Now we pop and push the elements back into stack1 -> [2,3,4]

    # Time complexity -> O(1) to push into the stack, popping is O(n) because we have to iterate through the input array, move the elements to the other array, and then move them back after popping

# How to solve: O(1)
    # We can move the elements from stack1 to stack2:
        # stack1 = [1,2,3,4] -> stack2 = [4,3,2,1], now stack1 is []
    # For popping, the bottleneck for O(n) was moving the ele's back and forth to each stack. What if we just left the ele's in stack2, that way each time we wanted to pop an element, we could do it in constant time? 
        # ex. stack1 = [4,3,2,1], pop -> [4,3,2], pop -> [4,3]
    # If we want to push an element 5 and 6 to the stack, we can push it to stack1 -> stack1 = [5, 6]. Say we continue popping from stack2 until it becomes empty, we go back to stack1, and move them to stack2 -> [6, 5], and then pop 5.
    # Peek:
        # If s2 is empty, move ele's from s1 to s2, and the last ele in s2 will be the front of the queue: s1: [1,2,3], s2 = [], pop ele's off s1 and move to s2 -> s1: [], s2 = [3,2,1], front of queue is s2[-1]
        # s2 is not empty:
            # Start by enqueue'ing ele's 1, 2, 3 -> s1: [1,2,3], s2: []
            # Dequeue one element -> move 3, 2, 1 to s2: s1: [], s2: [3,2,1], remove 1, s2: [3,2]
            # Enqueue more elements 4, 5, 6 -> s1: [4, 5, 6], s2: [3, 2]
            # Call peek -> returns top of s2, which is 2

    # Time Complexity -> Average case is O(1). Pushing into stack1 is O(1), popping from stack1 and pushing into stack2 is O(n), and then popping and pushing after that is O(1) until stack2 is empty and we need to pop, so average time complexity is O(1)
    

# O(n) solution
class MyQueue(object):

    def __init__(self):
        self.stack1 = []  # Main stack where elements are pushed
        self.stack2 = []  # Temporary stack for reversing order

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)  # Always push to stack1 (O(1))

    def pop(self):
        """
        :rtype: int
        """
        while self.stack1:  # While there are ele's in stack1
            self.stack2.append(self.stack1.pop()) # Pop ele from stack1 and append to stack2
        
        front_element = self.stack2.pop()  # Pop ele from front of queue and store in var

        while self.stack2:  # While there are ele's in stack2
            self.stack1.append(self.stack2.pop()) # Move ele's back to stack1

        return front_element  # Return dequeued element

    def peek(self):
        """
        :rtype: int
        """
        while self.stack1: # Move ele's from stack1 to stack2
            self.stack2.append(self.stack1.pop())

        front_element = self.stack2[-1]  # Get front element of the queue

        while self.stack2: # Move ele's back to stack1
            self.stack1.append(self.stack2.pop())

        return front_element

    def empty(self):
        """
        :rtype: bool
        """
        return not self.stack1  # Queue is empty if stack1 is empty

# O(1) solution
class MyQueue2:
    def __init__(self):
        self.s1 = []  # Primary stack for pushing elements
        self.s2 = []  # Secondary stack for reversing order

    def push(self, x: int) -> None:
        """Pushes an element to the queue."""
        self.s1.append(x)

    def pop(self) -> int:
        """Removes and returns the front element of the queue."""
        if not self.s2:  # If s2 is empty, transfer elements from s1
            while self.s1: # Continue until stack1 is empty
                self.s2.append(self.s1.pop()) # Pop ele's from stack1 and append to stack2
        return self.s2.pop() # Pop and return last ele from stack2

    # Peek shows the first ele in the queue
    def peek(self) -> int:
        """Returns the front element of the queue without removing it."""
        if not self.s2:  # If s2 is empty, transfer elements from s1
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1] # If stack2 is not empty, front of queue is last ele in stack2

    # Check if both stacks are empty because we are using two stacks simultaneously
    def empty(self) -> bool:
        """Checks if the queue is empty."""
        return max(len(self.s1), len(self.s2)) == 0  # Returns True if both stacks are empty


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# Step 1: Create the queue
# queue = MyQueue()  # Initializes an empty queue
queue2 = MyQueue2()

# Step 2: Push elements into the queue
# queue.push(1)  # Queue: [1]
# queue.push(2)  # Queue: [1, 2]

queue2.push(1)  # Queue: [1]
queue2.push(2)  # Queue: [1, 2]


# Step 3: Pop the front element
# print(queue.pop())  # Output: 1  (Queue becomes [2])
print(queue2.pop())

# # Step 4: Peek the front element
# # print(queue.peek())  # Output: 1  (Front element remains 1)
queue2.push(5)  # Queue: [1]
queue2.push(7)  # Queue: [1]
print(queue2.peek())

# Step 5: Check if the queue is empty
# print(queue.empty())  # Output: False (Queue still has [2])
print(queue2.empty())
