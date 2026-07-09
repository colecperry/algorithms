# 155. Min Stack

# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

# Example 1:
# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2

class MinStack:
    """
        TC: O(1) for all operations
        SC: O(n) - store tuple (val, min) for each element
    """
    def __init__(self):
        self.stack = []  # Stores (value, min_at_this_level)

    def push(self, val: int) -> None:
        if not self.stack:  # First element - it's the min
            self.stack.append((val, val))
        else:
            current_min = self.stack[-1][1]  # Get previous min
            new_min = min(val, current_min)  # Update if val is smaller
            self.stack.append((val, new_min))

    def pop(self) -> None:
        self.stack.pop()  # Remove top - previous min auto-restored

    def top(self) -> int:
        val, min_val = self.stack[-1]
        return val  # Return value only

    def getMin(self) -> int:
        val, min_val = self.stack[-1]
        return min_val  # Return min only

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin()) # return -3
minStack.pop()
print(minStack.top())    # return 0
print(minStack.getMin()) # return -2