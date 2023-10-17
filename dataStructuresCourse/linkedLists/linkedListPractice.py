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

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        appended_node = Node(value)
        if self.length == 0:
            self.head = appended_node
            self.tail = appended_node
        self.tail.next = appended_node
        self.tail = appended_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        pre = self.head
        temp = self.head
        while (temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        pre.next = None
        self.length =- 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self, value):
        prepended_node = Node(value)
        if self.length == 0:
            self.head = prepended_node
            self.tail = prepended_node
        prepended_node.next = self.head
        self.head = prepended_node
        self.length += 1
        return prepended_node
    # Return True?

    def pop_first(self):
        if self.length == 0:
            return None
        first_value = self.head
        self.head = self.head.next
        first_value.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return first_value.value
    
    def get_value(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        if index < 0 or index >= self.length:
            return None
        temp = self.get_value(index)
        temp.value = value
        return temp
    
    def insert_value(self, index, value):
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        inserted_node = Node(value)
        prev = self.get_value(index - 1)
        current = prev.next
        prev.next = inserted_node
        inserted_node.next = current
        self.length -= 1
        return True
        




my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(5)
my_linked_list.print_list()
print(" ")
my_linked_list.insert_value(3, 4)
my_linked_list.print_list()
