# How to print LinkedList:
def print_list(self):
    temp = self.head # Set a variable "temp" to self.head
    while temp is not None: # Create a while loop that continues until the end of the linked list
        print(temp.value) # Print out the value of the current node
        temp = temp.next # Update temp variable to point to the next node in the linked list

# my_linked_list.print_list()