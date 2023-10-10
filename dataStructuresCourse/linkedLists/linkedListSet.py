# SET - Pass in an index and a value to change the node's value

# How to Solve:
    # Return the node and set to a variable using the GET method
    # If you return a node, reassign it's value
    # Don't need to solve for edge cases - that is done through GET method

# Whatever the index is, that's the number of times we have to move temp over
# Remember to remove ".value" on the return statement of GET or it will not work b/c you are returning the value when using .GET on set_value method

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
    
    def get(self, index):
        if index < 0 or index >= self.length: # It is possible someone could pass in an index outside of our Linked List
            return None
        temp = self.head # Point a variable temp at the head of the linked list
        for _ in range(index): # Create a loop that runs the number of times in the index passed in
            temp = temp.next # Move the temp over one to the right
        return temp

    
    def set_value(self, index, value): # You can't use set in Python as it is a keyword
        temp = self.get(index) # Return the node at the index we passed in
        if temp: # Test to see if temp is pointing to a node, or None
            temp.value = value # Reassign the returned node with the value passed in
            return True # Return true if valid index passed in
        return False # Return false if invalid index passed in
    
    # def set_value(self, index, value):
    #     if index < 0 or index >= self.length: # It is possible someone could pass in an index outside of our Linked List
    #         return None
    #     temp = self.head # Point a variable temp at the head of the linked list
    #     for _ in range(index): # Create a loop that runs the number of times in the index passed in
    #         temp = temp.next # Move the temp over one to the right
    #         temp.value = value  # Reassign temp's value
    #     return temp.value

    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    
    
my_linked_list = LinkedList(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)

print('LL before set_value():')
my_linked_list.print_list()

my_linked_list.set_value(1,4)

print('\nLL after set_value():')
my_linked_list.print_list()