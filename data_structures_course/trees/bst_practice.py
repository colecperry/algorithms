class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while temp:
            if value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
            if value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                return False
        
    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while temp:
            if value is temp.value:
                return True
            elif value > temp.value:
                temp = temp.right
            elif value < temp.value:
                temp = temp.left
        return False
    

my_tree = BinarySearchTree()
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.contains(27))
print(my_tree.contains(17))