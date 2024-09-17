# PREPEND - Add a node to the beginning of the list

# How to Solve: Use the head node
    # Create a new node
    # Link new node to the head of the linked list
    # Set head to the new node
    # Solve for edge cases

# Time complexity is O(1) (constant time complexity): no traversal is required to prepend a node 
# For linkedlist big O is faster than regular lists! 0(1) vs 0(n)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
        return True

    def prepend(self,value):
        prepended_node = Node(value)
        if self.length == 0: # If the list is empty, set head and tail to the new node
            self.head = prepended_node
            self.tail = prepended_node
        else:
            prepended_node.next = self.head # Link the new node to the linked list
            self.head = prepended_node # Point the head to the correct node (the new prepended node)
        self.length +=1 # Increment the length of the linked list
        return True # Return true to use prepend as a boolean
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next                     
    
my_linked_list = LinkedList(2)
my_linked_list.append(3)

my_linked_list.prepend(1)
my_linked_list.print_list()
