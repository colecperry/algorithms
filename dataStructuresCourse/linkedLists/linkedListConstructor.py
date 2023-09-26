# Node class's sole responsibility is to create a new node so you can call the class to append, prepend, etc
# "Self" variables are variables that apply to a specific instance
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# First line calls the Node class to create the first node in the linked list when we create it
# Point head and tail to the first node, keep track of the length
class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        


# This is what you call to create the linked list with a single node with a value of 4
my_linked_list = LinkedList(4)

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)


"""
    EXPECTED OUTPUT:
    ----------------
    Head: 4
    Tail: 4
    Length: 1
    
"""

my_linked_list.print_list()

