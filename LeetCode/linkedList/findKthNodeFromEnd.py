# Implement the find_kth_from_end function, which takes the LinkedList (ll) and an integer k as input, and returns
# the k-th node from the end of the linked list WITHOUT USING LENGTH.

# Given this LinkedList:
# 1 -> 2 -> 3 -> 4
# If k=1 then return the first node from the end (the last node) which contains the value of 4.
# If k=2 then return the second node from the end which contains the value of 3, etc.
# If the linked list has fewer than k items, the program should return None.

# How to Solve:
    # Initalize a slow and fast pointer to the head
    # Loop through the list and move the fast pointer forward K times
    # Loop again and move each slow and fast pointers forward until fast reaches the end of the list
    # Return the slow node - idea is to create a gap between each pointer and return the correct node

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

    def find_kth_from_end(self, k): # Takes in a linked list and an integer K, and returns the k-th node from the end
        slow = self.head
        fast = self.head
        for _ in range(k): # Loop K times
            if fast == None: # Happens if "k" passed in is longer than the length of the linked list
                return None 
            fast = fast.next # Move fast over "k" times
        while fast: # While fast is not None
            slow = slow.next # Move the slow pointer over
            fast = fast.next # Move the fast pointer over
        return slow






my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 2
result = my_linked_list.find_kth_from_end(k)

print(result.value)  # Output: 4