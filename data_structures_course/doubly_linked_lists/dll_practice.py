class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.length = 1
        self.head = new_node
        self.tail = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop(self):
        temp = self.tail
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            temp.prev = None
            self.tail.next = None
        self.length -= 1
        return temp

    def pop_first(self):
        temp = self.head
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length / 2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(index - 1, index, -1): # Where to start the iteration, how many times to iterate, and the step
                temp = temp.prev
        return temp

    def set_value(self, index, value):
        if index < 0 or index >= self.length:
            return None
        temp = self.get(index)
        temp.value = value
        return temp

    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        else:
            temp = self.get(index)
            pre = temp.prev
            pre.next = new_node
            new_node.prev = pre
            new_node.next = temp
            temp.prev = new_node
            self.length += 1
            return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.pop_first()
        if index == (self.length - 1):
            return self.pop()
        else:
            pre = self.get(index - 1)
            temp = pre.next
            after = temp.next
            pre.next = after
            after.prev = pre
            temp.prev = None
            temp.next = None
            self.length -= 1
            return True



my_doubly_linked_list = DoublyLinkedList(6)
my_doubly_linked_list.prepend(4)
my_doubly_linked_list.prepend(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.pop()
my_doubly_linked_list.remove(2)
my_doubly_linked_list.print_list()