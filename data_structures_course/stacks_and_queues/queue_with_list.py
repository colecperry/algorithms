class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, value):
        self.queue.append(value)
    
    def dequeue(self):
        self.queue.pop(0) # By default pop removes the last item of a list, but with the argument 0, it removes the first item in the list

    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

    def peek(self):
        # Peek at the front of the queue
        if len(self.queue) > 0:
            return self.queue[0]
        else:
            return "Queue is empty"

    def size(self):
        return len(self.queue)

my_queue = Queue()
my_queue.enqueue(0)
my_queue.enqueue(1)
print(my_queue.queue)
print("size: ",my_queue.size())
print("peek: ",my_queue.peek())
print("is_empty: ",my_queue.is_empty())