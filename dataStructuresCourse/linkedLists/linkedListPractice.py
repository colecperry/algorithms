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
        else:
            self.tail.next = appended_node
            self.tail = appended_node
        self.length +=1
        return True
    
    # XXXX
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        # temp = pre.next
        while (temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        # temp.next = None
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        prepended_node = Node(value)
        if self.length == 0:
            self.head = prepended_node
            self.tail = prepended_node
        else:
            prepended_node.next = self.head
            self.head = prepended_node
        self.length += 1
        return prepended_node
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = temp.next
        temp.next = None
        self.length =- 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp



    


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.prepend(0)
my_linked_list.pop_first()
my_linked_list.print_list()
