# Think of a queue as a line at a DMV
# FIFO - First in first out

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


my_queue = Queue(4)

my_queue.print_queue()