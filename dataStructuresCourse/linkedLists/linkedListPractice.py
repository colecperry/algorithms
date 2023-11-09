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
        prepended_node = Node(value)
        if self.length == 0:
            self.head = prepended_node
            self.tail = prepended_node
        else:
            prepended_node.next = self.head
            self.head = prepended_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        popped_node = self.head
        self.head = self.head.next
        popped_node.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return popped_node
    
    def append(self, value):
        appended_node = Node(value)
        if self.length == 0:
            self.head = appended_node
            self.tail = appended_node
        else:
            self.tail.next = appended_node
            self.tail = appended_node
        self.length += 1
        return True
    
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
            self.tail.next = None
            self.length -= 1
            if self.length == 0:
                self.head = None
                self.tail = None
            return temp.value
        
    def get_value(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        node = self.get_value(index)
        if node:
            node.value = value
        return node
    
    def insert_value(self, index, value):
        inserted_node = Node(value)
        if index < 0 or index > self.length:
            return False
        if index == (self.length):
            return self.append(value)
        if index == 0:
            return self.prepend(value)
        before = self.get(index - 1)
        after = before.next
        before.next = inserted_node
        inserted_node.next = after
        self.length += 1
        return inserted_node
    
    def remove_value(self, index):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.pop_first()
        if index == (self.length - 1):
            return self.pop()
        before = self.head
        after = self.head.next
        for _ in range(index - 1):
            before = after
            after = after.next
        temp = after.next
        after.next = None
        before.next = temp
        self.length -= 1
        return after
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        pre = None
        after = temp.next
        for _ in range(self.length):
            after = temp.next
            temp.next = pre
            pre = temp
            temp = after
        return True


my_linked_list = LinkedList(1)
my_linked_list.prepend(0)
my_linked_list.pop_first()
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.pop()
my_linked_list.set_value(0,2)
my_linked_list.set_value(0,1)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.insert_value(4,5)
my_linked_list.remove_value(0)
my_linked_list.reverse()
my_linked_list.print_list()