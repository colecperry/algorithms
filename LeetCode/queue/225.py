# 225. Implement Stack using Queues

# Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

# Implement the MyStack class:
    # void push(int x) Pushes element x to the top of the stack.
    # int pop() Removes the element on the top of the stack and returns it.
    # int top() Returns the element on the top of the stack.
    # boolean empty() Returns true if the stack is empty, false otherwise.

# Notes:
# You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
# Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.


# Example 1:

# Input
    # ["MyStack", "push", "push", "top", "pop", "empty"]
# [[], [1], [2], [], [], []]

# Output
    # [null, null, null, 2, 2, false]

# Explanation
    # MyStack myStack = new MyStack();
    # myStack.push(1);
    # myStack.push(2);
    # myStack.top(); // return 2
    # myStack.pop(); // return 2
    # myStack.empty(); // return False

from collections import deque
class MyStack(object):
    def __init__(self):
        self.queue = deque() # Initialize an attribute of the MyStack class named 
        # "queue" with an empty dequeue object (a double ended queue), which allows
        # you to add and remove elements from both ends

    def push(self, x):
        self.queue.append(x) # We know that both stacks and queue's add to the end

    def pop(self):
        for _ in range(len(self.queue) - 1): # Loop through the queue except for the
            # last item because it will acts as the top of the stack
            self.push(self.queue.popleft()) # For each item, pop the left side of the
            # queue and push it onto the right side of the queue
        return self.queue.popleft() # Pop the left item and return it

# Note for above: We are simulating a stack pop using a queue: That means that that
# the front of the queue acts like the top of the stack. When you perform a "pop" 
# operation on the stack, you need to move all the elements in the queue

    def top(self): # "top" is returning the top or most recently added value
        return self.queue[-1] # -1 returns the right most item in the stack

    def empty(self):
        return len(self.queue) == 0 # Return true if the stack is empty, false if not
        
    def print_stack(self):
        print("Stack:", list(self.queue)) # Convert the "dequeue" object "self.queue"
        # to a list

# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.print_stack()
print("Popped:", obj.pop())
obj.print_stack()
print("Popped:", obj.pop())
obj.print_stack()
print("Top:", obj.top())
print("Empty:", obj.empty())