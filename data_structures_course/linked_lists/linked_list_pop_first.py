# Linked List POP FIRST - removes the first item in the linked list

# How to Solve: Use the head node
    # Move the head right
    # Pop off the old head
    # Solve for edge cases


# Time complexity is O(1) (constant time complexity): no traversal is required and the time that it takes to execute does not depend on the size of the input
# 2 Edge Cases:
#      1. If we have an empty linked list
#      2. If we only have one node in the list

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
    
    def pop_first(self):
        if self.length == 0:
            return None # Stop the rest of the code from running
        temp = self.head # In order to remove a node, we have to have something point at it
        self.head = self.head.next # Move head over one
        temp.next = None # Remove the first node from the list
        self.length -= 1
        if self.length == 0: # Edge Case #2: If the length is zero after decrementing,
            self.tail = None # Lines 38 - 41 run if there is one node in the list, head gets set = to None, must set tail to None
        return temp.value
    
# Another way to write pop first
    def popfirst(self):
        if self.length == 0:
            return None
        
        first_value = self.head
        second_value = self.head.next

        first_value.next = None
        self.head = second_value
        
        self.length -= 1
        if self.length == 0:
            self.tail = None
        
        return first_value

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
my_linked_list = LinkedList(2)
my_linked_list.append(1)

# 2 Items in list
print(my_linked_list.pop_first())
# 1 Item in list
print(my_linked_list.pop_first())
# 0 Items in list
print(my_linked_list.pop_first())

# my_linked_list.print_list()
