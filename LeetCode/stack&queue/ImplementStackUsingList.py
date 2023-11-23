# Stack: Implement Stack Using a List ( ** Interview Question)
# In the Stack: We discussed how stacks are commonly implemented using a list instead of a linked list.

# Create a constructor for Class Stack that implements a new stack with an empty list called stack_list.

class Stack:
    def __init__(self): # Create an instance variable named 'stack_list' and
        self.stack_list = [] # assign it to an empty list to store the stack