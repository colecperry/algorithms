class Queue:
    def __init__(self):
        self.stack = []
    
    def print(self):
        print(self.stack)
    
    def enqueue(self, value):
        self.stack.append(value)
        return True

    def dequeue(self):
        self.stack.pop(0)
        return True
    
    def peek()

my_queue = Queue()
my_queue.enqueue(0)
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.dequeue()

my_queue.print()