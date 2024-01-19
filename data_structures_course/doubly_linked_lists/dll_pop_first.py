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


my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
print(my_doubly_linked_list.pop_first())
print(my_doubly_linked_list.pop_first())
print(my_doubly_linked_list.pop_first())