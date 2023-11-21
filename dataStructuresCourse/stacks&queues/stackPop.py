class Node: # Use the same node class as linked lists
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node # Only need to track the top of the stack since we can only add/remove from there
        self.height = 1 # Track height instead of length (think of the stack as vertical)

    def print_stack(self):
        temp = self.top # Start pointer at the top of the stack
        while temp: # While the node we are on has a value
            print(temp.value) 
            temp = temp.next # Move to the next node

    def push(self, value):
        pushed_node = Node(value) #Create a new node
        if self.height == 0: # If the height is zero,
            self.top = pushed_node # Set the top to the new node
        else:
            pushed_node.next = self.top # Connect the new node to the top
            self.top = pushed_node # Set the top to the new node
        self.height += 1

    def pop(self):
        if self.height == 0: # If the stack is empty
            return None # Return none
        else:
            temp = self.top # Point a variable at the top of the stack
            self.top = self.top.next # Move the top down a node
            temp.next = None # Pop the top node off
            self.height -=1
            return temp # Return the node you popped off 

my_stack = Stack(2)
my_stack.push(1)
my_stack.push(0)
my_stack.pop()

my_stack.print_stack()