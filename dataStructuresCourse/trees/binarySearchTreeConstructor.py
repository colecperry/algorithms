class Node:
    def __init__(self, value):
        self.value = value # Each node has a value, 
        self.left = None # Something pointing the left (child)
        self.right = None # and something pointing to the right (other child)

class BinarySearchTree:
    def __init__(self):
        self.root = None # Initalize the root to None - we will build add with "Insert"

# class BinarySearchTree:
#     def __init__(self, value):
#         new_node = Node(value) # Create a new node
#         self.root = new_node # Point the root, or top of the tree to the created node

        # Note - you could also point the root to none, and add a node later with the
        # insert method. You also would not initialize a new node in the Binary Tree init

my_tree = BinarySearchTree(1) # Create an instance of the class

print(my_tree.root)
print(my_tree.root.value)



