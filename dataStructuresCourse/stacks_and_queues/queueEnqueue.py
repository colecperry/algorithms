class Node: # Use the same node class as linked lists
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value) # Create a new node to start the queue
        self.first = new_node # Keep track of first (People first in line)
        self.last = new_node # and last (Last people added to the queue)
        self.length = 1

    def print_queue(self):
        temp = self.first # Start the pointer at "first"
        while temp: # While the current node is True
            print(temp.value) 
            temp = temp.next # Move to the next node

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0: # If the list is empty
            self.first = new_node # Set first and last to the new node
            self.last = new_node
        else:
            self.last.next = new_node # Connect the new node to the end
            self.last = new_node # Set "last" to the new node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp



my_queue = Queue(1)
my_queue.enqueue(2)
print(my_queue.dequeue())
