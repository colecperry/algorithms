# Time complexity: 0(n) (linear time complexity): the time it takes to complete an operation grows linearly with the size of the input data set, n. As the size of the input increases, the time to complete the task increases proportionally.
    # Accessing index 0 or the index of n-1 would be 0(1) -> You don't loop and you access these nodes via the head or the tail using the .get() method
    # Accessing any other index would be 0(n) because to find the element you need to traverse the list using the .get() method

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None # Same constructor as singly linked lists, but DLL's have 
        # arrows that also point backwards

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value) # Create first node when we create the DLL
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        new_node = Node(value) # Create a new node floating in space
        if self.length == 0: # If the linked list is empty:
            self.head = new_node # Set the new node to the head 
            self.tail = new_node # and tail
        else:
            self.tail.next = new_node # Connect the current tail to the new node
            new_node.prev = self.tail # Connect the last node in the list to the prior
            # node (currently pointed at the tail)
            self.tail = new_node # Move the tail to the end of the list
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0: # If the length of the DLL is 0, 
            return None # return None (nothing to pop)
        temp = self.tail # Need to assign variable here b/c if length is 1, you go   
        # straight to the return statement (Create temp to point at the tail)
        if self.length == 1: # If the length of the DLL is 1,
            self.head = None # set the head
            self.tail = None # and tail to none
        else:
            self.tail = self.tail.prev # Move the tail back one node using ".prev"
            self.tail.next = None # Disconnect the tail from the last node (one way)
            temp.prev = None # Disconnect the last node from the one before (other way)
        self.length -= 1 # Decrement the length by one
        return temp.value # return the popped node
    
    def prepend(self, value):
        new_node = Node(value) # Create a new node floating in space
        if self.length == 0: # If the length is zero,
            self.head = new_node # Set the head and
            self.tail = new_node # tail to the newly created node
        else:
            new_node.next = self.head # Connect the new node to the current head (right)
            self.head.prev = new_node # Connect current head to the NN (other direction)
            self.head = new_node # Move the head over by pointing it at the NN
        self.length += 1 # Increment the length by one
        return True
    
    def pop_first(self):
        if self.length == 0: # If there is no Nodes in the list, 
            return None # return None because there is no nodes to pop
        temp = self.head # Need to assign variable here b/c if length is 1, you go   
        # straight to the return statement (Create temp to point at the tail)
        if self.length == 1: # If the length is one,
            self.head = None # Set the head
            self.tail = None # and tail to None
        else:
            self.head = self.head.next # Move the head over one node
            temp.next = None # Disconnect first node from second node (Arrow going right)
            self.head.prev = None # Disconnect second node from first (Arrow going left)
        self.length -= 1 # Decrement length by one
        return temp
    
    # We can optimize this method in a doubly linked list. Normally, we would set temp equal to the head and iterate through the list based on the index passed in. But with doubly linked lists, if the index passed in is more than halfway through the list, we can start out iteration from the tail.
    def get(self, index):
        if index < 0 or index >= self.length: # It is possible someone could pass in an 
            return None # index outside of our Linked List
        temp = self.head # Point a variable temp at the head of the linked list
        if index < self.length/2: # If the index is less than the midpoint of the list,
            for _ in range(index): # Create a loop that iterates the # of times based on
                temp = temp.next # the index and stops on the correct node
        else:
            temp = self.tail # If the index is greater than the midpoint of the list,
            for _ in range(index - 1, index, -1): # First argument is where to start the iteration, second is the # of times iterated based on the index, and the third is the step, or backwards by one each time
                temp = temp.prev # temp stops on the correct node
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index) # Use the "get" method to get a variable pointed at the correct node
        if temp: # Must check if we get back a node from the get method, or if we get back "None" because our index was out of range
            temp.value = value # Reassign the value
            return True # Return True if we return a node and are successful
        else:
            return False # Return False if we do not return a node 


my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)

print(my_doubly_linked_list.set_value(5,0))
my_doubly_linked_list.print_list()
