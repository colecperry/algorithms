# How to solve (without using the length attribute)
    # Use the two pointer approach
    # One pointer (slow) moves one node at a time,
    # The other pointer (fast) moves two nodes at a time
    # When the fast pointer reaches the end of the list, the slow pointer should be in the middle
    # For an even number of nodes, return the second half of the middle

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
        

    def find_middle_node(self):
        slow = self.head # Set 2 pointers, slow and fast to the head
        fast = self.head
        # We must include "while fast" because if fast gets pointed outside the list, it will become None.
        # We cannot access "None.next" so we just check the node itself
        while fast and fast.next: # Check if there is a node, and then check if there's a next node 
            slow = slow.next # Advance the slow variable to the next node
            fast = fast.next.next # Advance the fast variable two nodes forward
        return slow





my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

print(my_linked_list.find_middle_node().value)



"""
    EXPECTED OUTPUT:
    ----------------
    3
    
"""