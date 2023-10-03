# Linked List Remove - remove a node at a specific index
# Time complexity is O(n)
# Three Edge Cases:
# 1. Node at index passed in is out of range
# 2. First index passed in
# 3. Last index passed in

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
    
    def pop(self): # Remove an item from the end of the list
        if self.length == 0:
            return None
        else:
            temp = self.head # Set two variables, pre and temp equal to the head
            pre = self.head
            while(temp.next): # Loop through the linked list, and while the next node is True,
                pre = temp    # Set pre to temp
                temp = temp.next # Set temp to the next node after pre
            self.tail = pre   # Once loop finishes, set pre (node before last node) to self.tail
            self.tail.next = None # Set self.tail.next to None to pop the last node off the linked list
            self.length -= 1
            if self.length == 0: # Edge Case #2 (One node in list): If the length is zero after decrementing,
                self.head = None  # set head and tail to None, and 
                self.tail = None
            return temp # return the node, which should be None
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head # In order to remove a node, we have to have something point at it
        self.head = self.head.next # Move head over one
        temp.next = None # Remove the first node from the list
        self.length -= 1
        if self.length == 0: # Edge Case #2: If the length is zero after decrementing,
            self.tail = None # Lines 38 - 41 run if there is one node in the list, head gets set = to None, must set tail to None
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length: # It is possible someone could pass in an index outside of our Linked List
            return None
        temp = self.head # Point a variable temp at the head of the linked list
        for _ in range(index): # Create a loop that runs the number of times in the index passed in
            temp = temp.next # Move the temp over one to the right
        return temp
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None # If we are successful we return a node, if unsuccessful we return None (opposite of a node)       
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index - 1) # Need to have a variable to the left of the one we need to remove
        temp = prev.next # This is the O(1) way of assigning the temp variable vs get method is 0(n)
        prev.next = temp.next # Point the node before index passed in to the node after the index passed in
        temp.next = None # Break the node at the index passed in off of the list
        self.length -= 1
        return temp
    
my_linked_list = LinkedList(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)

print(my_linked_list.remove(2), '\n')

my_linked_list.print_list()



        
        