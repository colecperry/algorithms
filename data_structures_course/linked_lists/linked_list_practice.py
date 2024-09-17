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
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        return True

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next= new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
            if self.length == 0:
                self.head = None
                self.tail = None
            return temp
    
    def pop(self):
        if self.length == 0:
            return None
        else:
            pre = self.head
            temp = self.head
            while temp.next:
                pre = temp
                temp = temp.next
            self.tail = pre
            pre.next = None
            self.length -= 1
            if self.length == 0:
                self.head = None
                self.tail = None
            return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set(self, index, value):
        if index < 0 or index >= self.length:
            return None
        temp = self.get(index)
        temp.value = value
        return temp

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        pre = self.head
        for _ in range(index - 1):
            pre = pre.next
        temp = pre.next
        pre.next = new_node
        new_node.next = temp
        self.length += 1
        return new_node.value

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        else:
            pre = self.head
            temp = self.head
            for _ in range(index):
                pre = temp
                temp = temp.next
            pre.next = temp.next
            temp.next = None
            self.length -= 1
            return temp
    
    def reverse(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.tail
        self.tail = temp
        pre = None
        after = temp.next
        while temp:
            after = temp.next
            temp.next = pre
            pre = temp
            temp = after
        return True






my_linked_list = LinkedList(1)
my_linked_list.prepend(0)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.reverse()
my_linked_list.print_list()
