# Stack: Reverse String ( ** Interview Question)
# The reverse_string function takes a single parameter string, which is the string you want to reverse.

# Return a new string with the letters in reverse order.

# This will use the Stack class we created in the last three coding exercises:
    # Implement Stack Using a List
    # Push for Stack Using a List
    # Pop for Stack Using a List

# How to Solve
    # Create a new stack and empty string to store the reversed string
    # Interate through the string and push each character onto the stack
    # Use a while loop with functions "is_empty()" or "size()" and add it to the reversed string


class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()



def reverse_string(string):
    stack = Stack() # Create a new stack
    reversed_string = '' # Create an empty string to store the reversed string

    for s in string: # Iterate over the string and
        stack.push(s) # push each character into the stack

    while not stack.is_empty(): # Create a while loop - while the stack is not empty
        reversed_string += stack.pop() # Add the popped character from the stack to the reversed string
    
    return reversed_string
    
# Note: Line 49 can also we written as: " while stack.size() > 0 "






my_string = 'hello'

print ( reverse_string(my_string) )



"""
    EXPECTED OUTPUT:
    ----------------
    olleh

"""