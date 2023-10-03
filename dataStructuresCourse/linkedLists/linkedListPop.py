# Pop removes the last item in the linked list
# Time complexity is O(n)
# What makes this more complicated is that the tail is moving to the left, and the arrows are pointing right
# The only way to move the tail is to get to the node before it, and use .next 
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

    def pop(self):          # Remove an item from the end of the list
        if self.length == 0:
            return None
        else:
            temp = self.head # Set two variables, pre and temp equal to the head
            pre = self.head
            while(temp.next): # Loop through the linked list, and while the next node is not none,
                pre = temp    # Set pre to temp
                temp = temp.next # Set temp to the next node after pre
            self.tail = pre   # Once loop finishes, set pre (node before last node) to self.tail
            self.tail.next = None # Set self.tail.next to None to pop the last node off the linked list
            self.length -= 1
            if self.length == 0: # Edge Case #2: If the length is zero after decrementing,
                self.head = None  # set head and tail to None to accurately represent the state of an empty LL
                self.tail = None
            return temp.value # return the node, which should be None

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
my_linked_list = LinkedList(1)
my_linked_list.append(2)

# Returns the value of the node that was deleted
print(my_linked_list.pop())
# Returns the value of the node that was deleted
print(my_linked_list.pop())
# Returns an empty list
print(my_linked_list.pop()) 

# If you want to return the value instead of the node, change line 39 to return temp.value