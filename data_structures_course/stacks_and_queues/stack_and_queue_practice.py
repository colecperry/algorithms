class Queue:
    def __init__(self):
        self.queue = []
    
    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, value):
        self.queue.append(value)
        return True

    def dequeue(self):
        if self.is_empty():
            return None
        self.queue.pop(0)
        return True
    
    
    def peek(self):
        return self.queue[0]
    
    def print_queue(self):
        print(self.queue)
    
my_queue = Queue()
print(my_queue.dequeue())
my_queue.enqueue(0)
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.dequeue()
my_queue.dequeue()
my_queue.dequeue()
my_queue.print_queue()
