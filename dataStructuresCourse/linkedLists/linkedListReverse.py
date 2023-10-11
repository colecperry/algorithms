# Linked List REVERSE - Reverse head and tail, point all arrows backwards

# How to Solve:
    # Swap head and tail
    # Point to node's before and after head
    # Change the direction that the node is pointing by using .next
    # Move the pointers over

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

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    # Step 1: Create a new node by calling on the Node class
    def append(self,value):
        appended_node = Node(value)
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
        self.length +=1
        # We return true for another method that calls on append method (requires true or false)
        return True

    def reverse(self):
        temp = self.head # Point to the head
        self.head = self.tail # Set head equal to the tail
        self.tail = temp # Set tail back to head (temp was pointing there)
        after = temp.next # Point to node after the head
        before = None # Point to node before the head
        for _ in range(self.length): # Loop through the linked list
            after = temp.next # Get variable pointed at .next of temp (self.head) (This later moves the first node)
            temp.next = before # Flip the arrow pointing right to pointing left
            before = temp # Move before node pointer over
            temp = after # Move temp node pointer over

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

my_linked_list.reverse()

my_linked_list.print_list()

