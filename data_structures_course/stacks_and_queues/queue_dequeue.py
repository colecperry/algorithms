# Queue dequeue time complexity: 0(1) (constant time complexity) -> Fixed number of operations and does not depend on the size of the input

# Dequeue:
    # Solve for edge cases: length is 0, length is 1

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
        if self.length == 0: # If length is zero, return None (no nodes to dequeue in Queue)
            return None
        temp = self.first # You need to set the temp variable before the next line because it returns temp
        if self.length == 1: # If the length is 1, set first and last to None because
            self.first = None # there will be no more nodes in the Queue after dequeue'ing,
            self.last == None # and you need to correctly set first and last
        else:
            self.first = self.first.next # Move the first node one to the right
            temp.next = None # Pop the first node off the queue (node set to temp)
        self.length -= 1 # Decrement the length
        return temp
    
my_queue = Queue(1)
my_queue.enqueue(2)


# 2 Items in the queue
print(my_queue.dequeue())

# 1 Item in the queue
print(my_queue.dequeue())

# 0 Items in the queue
print(my_queue.dequeue())