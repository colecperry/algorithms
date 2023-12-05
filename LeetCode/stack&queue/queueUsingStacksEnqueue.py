# Queue Using Stacks: Enqueue ( ** Interview Question)
# You are given a class MyQueue which implements a queue using two stacks. Your task
# is to implement the enqueue method which should add an element to the back of the
# queue.

# To achieve this, you can use the two stacks stack1 and stack2. Initially, all
# elements are stored in stack1 and stack2 is empty. In order to add an element to
# the back of the queue, you need to first transfer all elements from stack1 to stack2
# using a loop that pops each element from stack1 and pushes it onto stack2.

# Once all elements have been transferred to stack2, push the new element onto stack1.
# Finally, transfer all elements from stack2 back to stack1 in the same way as before,
# so that the queue maintains its ordering.

# Your implementation should satisfy the following constraints:
    # The method signature should be def enqueue(self, value).
    # The method should add the element value to the back of the queue.

class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def enqueue(self, value):
        while len(self.stack1) > 0: # Check if stack1 has any elements in it
            self.stack2.append(self.stack1.pop()) # Pop elements from stack1 one at
            # a time and append them to stack2 (This is done we can add new element
            # to bottom of stack1) - AKA Transfer all elements from stack1 to stack2
        self.stack1.append(value) # Once all elements have been transferred from
        # stack1 to stack2, append the new element value to the bottom of stack1
        while len(self.stack2) > 0: # Enter another while loop as long as stack2 has
            # elements in it
            self.stack1.append(self.stack2.pop()) # Transfer all elements back from
            # stack2 to stack1 in their original order, ensuring the queue is 
            # maintained in a First-In-First-Out ordering

        # Notes to Understand:
            # We want to implement a queue using the stack data structure
            # We need to implement the "enqueue" method using basic stack operations 
            # like push and pop
            # Since we can only use a stack, if we "enqueue", we need to add our value
            # to the bottom of the stack because a stack because since a stack is LIFO
            # and a queue is FIFO, any new values added to our stack need to be added
            # to the bottom since we are solving for a queue. This is also why stack1
            # appears reversed


        # Notes for each loop:
        # Enqueue(1) - Initially, stack1 is empty, and stack2 is also empty. The first
            # while loop doesn't execute because len(self.stack1) is initially 0.
            # The element 1 is added to the end of stack1.
            # The second while loop doesn't execute because len(self.stack2) is still
            # 0.
        # Enqueue(2) - The first while loop reverses the order of elements in
            # stack1 by:
            # Popping 1 off stack1 and pushing onto stack2.
            # The element 2 is added to the end of stack1.
            # The second while loop moves elements back from stack2 to stack1 by:
            # Popping 1 off stack2 and adding to stack1
            # (restoring their original order).
        # Enqueue(3) - The first while loop reverses the order of elements in stack1
            # by:
            # Popping 1 off stack1 and pushing onto stack2.
            # Popping 2 off stack1 and pushing onto stack2
            # The element 3 is added to the end of stack1.
            # The second while loop moves elements back from stack2 to stack1 by:
            # Popping 2 off stack2 and adding to stack1
            # Popping 1 off stack2 and adding to stack1
            # (restoring their original order).
        

    def peek(self):
        return self.stack1[-1]

    def is_empty(self):
        return len(self.stack1) == 0
        
        

# Create a new queue
q = MyQueue()

# Enqueue some values
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Output the front of the queue
print("Front of the queue:", q.peek())

# Check if the queue is empty
print("Is the queue empty?", q.is_empty())


"""
    EXPECTED OUTPUT:
    ----------------
    Front of the queue: 1
    Is the queue empty? False
    
"""