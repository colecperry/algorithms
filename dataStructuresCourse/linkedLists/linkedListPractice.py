class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.tail = new_node
        self.head = new_node
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
        else:
            self.tail.next = appended_node
            self.tail = appended_node
        self.length += 1
        return appended_node
    
    def pop(self):
        if self.length == 0:
            return None
        else:
            pre = self.head
            temp = self.head
            while (temp.next):
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.length -= 1
            if self.length == 0:
                self.head = None
                self.tail = None
            return temp.value
        
    def prepend(self, value):
        prepended_node = Node(value)
        if self.length == 0:
            self.head = prepended_node
            self.tail = prepended_node
        else:
            prepended_node.next = self.head
            self.head = prepended_node
        self.length += 1
        return True
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert_value(self, index, value):
        if index < 0  or index >= self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        inserted_node = Node(value)
        temp = self.get(index - 1)
        inserted_node.next = temp.next
        temp.next = inserted_node
        self.length += 1
        return True


    



my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.prepend(0)
print('LL before set_value():')
my_linked_list.print_list()
my_linked_list.insert_value(0, 2)
print('\nLL after set_value():')
my_linked_list.print_list()
