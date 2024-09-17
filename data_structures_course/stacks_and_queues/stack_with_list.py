class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"
        
    def size(self):
        return len(self.stack)
    
my_stack = Stack()
my_stack.push(0)
my_stack.push(1)
my_stack.push(2)
my_stack.pop()
print(my_stack.stack)
print("Is my stack empty?", my_stack.is_empty())
print("Peek at the top of the stack: ", my_stack.peek())
print("Stack size: ", my_stack.size())
    
# fixed size stack
class FixedSizeStack:
    def __init__(self, size):
        self.stack = [0] * size # Initialize the stack with zeros
        self.top = -1 # Variable to track the top element
        self.max_size = size # Maximum size of the stack

    def push(self, item):
        if self.top < self.max_size - 1:
            self.top += 1
            self.stack[self.top] = item # Place the item at the top
        else:
            return "Stack overflow"

    def pop(self):
        if self.top >= 0:
            item = self.stack[self.top]
            self.top -= 1
            return item
        else:
            return "Stack Underflow"
        
    def peek(self):
        if self.top >= 0:
            return self.stack[self.top]
        else:
            return "Stack is empty"
        
    def is_empty(self):
        return self.top == -1
    
    def size(self):
        return self.top + 1
