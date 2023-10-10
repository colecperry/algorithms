# INSERT: Insert a new node at a particular index that has a particular value

# How to Solve:
    # Check if index passed in is out of range
    # If index is 0, prepend
    # If index is last, append
    # If index is neither, 
        # Create a new node
        # Get the index one before the index passed in to help connect it to the LL

# Time complexity is O(n)
# Edge Cases:
    # If the index we are inserting at is zero
    # If the index we are inserting at is the last index of the list

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
    
    def prepend(self,value):
        prepended_node = Node(value)
        if self.length == 0: # If the list is empty, set head and tail to the new node
            self.head = prepended_node
            self.tail = prepended_node
        else:
            prepended_node.next = self.head # Point the prepended node equal to head of current linked list
            self.head = prepended_node # Move head back by pointing it at the new prepended node
        self.length +=1 # Increment the length of the linked list
        return True # Return true to use prepend as a boolean
    
    def get(self, index):
        if index < 0 or index >= self.length: # It is possible someone could pass in an index outside of our Linked List
            return None
        temp = self.head # Point a variable temp at the head of the linked list
        for _ in range(index): # Create a loop that runs the number of times in the index passed in
            temp = temp.next # Move the temp over one to the right
        return temp
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0: # If the index is zero, prepend the node to the front of the list
            return self.prepend(value) # End the code here
        if index == self.length: # If the index is equal to the last index, append the node to the end of the list
            return self.append(value) # End the code here
        inserted_node = Node(value) # Create a new node
        temp = self.get(index - 1) # Get the node one before the index passed in
        inserted_node.next = temp.next # Point the newly created node to the node right insertion (temp.next is pointing there)
        temp.next = inserted_node # Point temp to the newly created node
        self.length += 1
        return True # Return True if successful
            
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

my_linked_list = LinkedList(0)
my_linked_list.append(2)

print('LL before insert_value():')
my_linked_list.print_list()

my_linked_list.insert(1,1)

print('\nLL after insert_value():')
my_linked_list.print_list()