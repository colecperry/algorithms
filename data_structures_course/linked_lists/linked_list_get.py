# GET - Pass in an index and return the node at that index

# How to Solve
    # Point a variable to the head of the linked list
    # Create a loop that runs # of times of the index
    # Solve for edge cases - if index passed in is out of range

# Time complexity is O(n)
# Whatever the index is, that's the number of times we have to move temp over

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
        if index < 0 or index >= self.length: # It is possible someone could pass in 
            return None # an index outside of our Linked List
        temp = self.head # Point a variable temp at the head of the linked list
        for _ in range(index): # Create a loop that runs the number of times in the index passed in
            temp = temp.next # Move the temp over one to the right
        return temp.value

    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    
    
my_linked_list = LinkedList(0)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)

print(my_linked_list.get(1))

