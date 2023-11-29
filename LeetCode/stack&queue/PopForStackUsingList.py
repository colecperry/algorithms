# Stack: Pop for Stack That Uses List ( ** Interview Question)
# Add a method to pop a value from the Stack implementation that we began in the last two Coding Exercises.

# Remember: This Stack implementation uses a list instead of a linked list.

class Stack:
    def __init__(self): # Create an instance variable named 'stack_list' and
        self.stack_list = [] # assign it to an empty list to store the stack
        
    def print_stack(self): # Create a loop the length of the list, starting from the last index, ending at an
        for i in range(len(self.stack_list)-1, -1, -1): # starting at the index of (len(self.stack_list)-1), 
            # ending at -1 (goes up to but does not include the index -1 (loop down to zero), with a step of -1
            print(self.stack_list[i]) # access the element of stack_list at the current index 'i' and print

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value): # Create a method, push, that takes two parameters
        self.stack_list.append(value) # Using the stack_list attribute, append the value to the end of the list

    def pop(self):
        if self.is_empty(): # Run the "is_empty" function which returns True if stack is empty and false if not
            return None # If "if" statement returns true, the pop method returns "None" (no element to pop)
        else:
            return self.stack_list.pop() # Else, use the pop method which removes the last item from the list
            
            
            
my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

print("Stack before pop():")
my_stack.print_stack()

print("\nPopped node:")
print(my_stack.pop())

print("\nStack after pop():")
my_stack.print_stack()



"""
    EXPECTED OUTPUT:
    ----------------
    Stack before pop():
    3
    2
    1
    
    Popped node:
    3
    
    Stack after pop():
    2
    1
 
"""