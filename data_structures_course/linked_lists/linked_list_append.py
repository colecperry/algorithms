# APPEND - adding a node to the end of the list

# How to Solve : Get to the tail node
    # Create a node
    # Connect current tail to the new node
    # Point Linked List to new tail
    # Solve for edge cases

# Time complexity is 0(1) (constant time complexity) which means that the operation does not depend on the size of the input or increase with the size of the data. Append is 0(1) because the steps needed can be done without traversing the list.
# Edge case is when we do not have any items in the linked list
# In this case, there is no exisiting list to connect to new node to, so we won't be able to use "next" to connect them 

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

# Step 1: Create a new node by calling on the Node class
    def append(self,value):
        appended_node = Node(value) # Create a new node floating in space
        # If the dataset is empty, point both head and tail to the new appended node 
        if self.length == 0:
            self.head = appended_node
            self.tail = appended_node
        else:
            # Once we create a new node, it is floating in space
            # Use self.tail.next to connect the current tail to the new node
            self.tail.next = appended_node
            # Since the node is added to the end, point the tail to the new node
            self.tail = appended_node  
        self.length +=1 # Add one to the length regardless of the length of the list
        # We return true for another method that calls on append method (requires true or false)
        return True
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
# Create a linked list, assign to variable "my_linked_list"
my_linked_list = LinkedList(1)
# Call append method on linkedlist
my_linked_list.append(2)
my_linked_list.print_list()
