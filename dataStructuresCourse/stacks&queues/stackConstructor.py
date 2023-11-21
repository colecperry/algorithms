# We are implementing our stack using a linked list data structure
# Think of a stack as a can of tennis balls
# LIFO - Last in first out - you can only add and remove from the top

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

my_stack = Stack(4)
my_stack.print_stack()
