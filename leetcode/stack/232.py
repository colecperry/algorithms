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

# Giveaway: the problem explicitly says "implement a queue using stacks" (or vice versa) — it names the two ADTs directly, so the task is translating one access order into the other rather than discovering a hidden pattern.

class QueueWithStacks:
    def __init__(self):  # LC 232 - Implement Queue using Stacks
        self.input_stack = [] # input stack (accepts all pushes)
        self.output_stack = [] # output stack (serves pops/peeks)

    def push(self, x: int) -> None:
        """TC: O(1)"""
        self.input_stack.append(x)

    def pop(self) -> int:
        """TC: O(1) amortized"""
        self._transfer()
        return self.output_stack.pop() # goal is to pop from the end of the stack in FIFO order

    def peek(self) -> int:
        """TC: O(1) amortized"""
        self._transfer() # make input stack (LIFO) into output stack (FIFO)
        return self.output_stack[-1]

    def empty(self) -> bool:
        """TC: O(1)"""
        return not self.input_stack and not self.output_stack

    def _transfer(self):
        """
        Transfers all items from input_stack to output_stack, but only when
        output_stack is empty. This reverses their order once, so the oldest
        item (front of queue) ends up on top of output_stack.
        """
        if not self.output_stack: # if output stack is empty, items are not in FIFO order
            while self.input_stack: # transfer everything from input stack (LIFO -> FIFO)
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