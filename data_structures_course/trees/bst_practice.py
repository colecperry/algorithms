class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def contains(self, value):
        temp = self.root
        while temp:
            if value > temp.value:
                temp = temp.right
            elif value < temp.value:
                temp = temp.left
            else:
                return True
        return False
    
    def insert(self, value):
        new_node = Node(value)

        if self.root == None:
            self.root = new_node
            return True
        
        else:
            temp = self.root
            while temp:
                if value == temp.value:
                    return False
                if value < temp.value:
                    if temp.left is None:
                        temp.left = new_node
                        return True
                    else:
                        temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = new_node
                        return True
                    else:
                        temp = temp.right



my_tree = BinarySearchTree()
print(my_tree.insert(47))
print(my_tree.insert(21))
print(my_tree.insert(76))
print(my_tree.insert(18))
print(my_tree.insert(27))
print(my_tree.insert(52))
print(my_tree.insert(82))
print(my_tree.insert(82))
