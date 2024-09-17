# Time complexity: 0(1) (constant time complexity) -> the operation takes a constant amount of time to complete regardless of the input. Since you have a reference to the tail, prev, and next, each of the steps take a constant amount of time independent of how many nodes are already in the list. (no traversal needed)

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

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.print_list()