# Stack: Push for Stack That Uses List ( ** Interview Question)
# Add a method to push a value onto the Stack implementation that we began in the last Coding Exercise.

# Remember: This Stack implementation uses a list instead of a linked list.

class Stack:
    def __init__(self): # Create an instance variable named 'stack_list' and
        self.stack_list = [] # assign it to an empty list to store the stack
        
    def print_stack(self): # Create a loop the length of the list, starting from the last index, ending at an
        for i in range(len(self.stack_list)-1, -1, -1): # index of -1, with a step of -1 (decrementing by 1)
            print(self.stack_list[i]) # access the element of stack_list at the current index 'i' and print

    def push(self, value): # Create a method, push, that takes two parameters
        self.stack_list.append(value) # Using the stack_list attribute, append the value to the end of the list

# Note - when working within a class method, you have to use the 'self' keyword to access attributes or methods
# beloning to the instance of the class ('stack_list' belongs to class Stack.) Other methods written under the
# class which have their own local variables would not need to follow this rule

my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

my_stack.print_stack()



"""
    EXPECTED OUTPUT:
    ----------------
    3 
    2
    1
 
"""