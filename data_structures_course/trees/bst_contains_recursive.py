class Node:
    def __init__(self, value):
        self.value = value # Each node has a value, 
        self.left = None # Something pointing the left (child)
        self.right = None # and something pointing to the right (other child)

class BinarySearchTree:
    def __init__(self):
        self.root = None # Initalize the root to None - we will build add with "Insert"
    
    def __r_insert(self, current, value):
        if current == None: # Base case
            return Node(value) # Create a new node and return it to call stack, which is assigned to current.left
        if value < current.value: # If value we want to insert is less than the current node's value
            current.left = self.__r_insert(current.left, value) # Recursively call insert on the left child node until the current node becomes none
        if value > current.value: # If the value we want to insert is greater than current node's value
            current.right = self.__r_insert(current.right, value) # Recursively call insert on the right child node until the current node becomes none
        return current # Duplicates will just return


    # Helper method to pass in the root as current
    def r_insert(self, value):
        if self.root == None: # Edge case for empty 
            self.root = Node(value)
        self.__r_insert(self.root, value)

    def __r_contains(self, current, value):
        if current == None: # Edge case for empty list
            return False
        if value == current.value: # If the value you are looking for is the current node you are on
            return True
        if value < current.value: # If the value is less than the current node
            return self.__r_contains(current.left, value) # Recursively call the contains method on left child
        if value > current.value: # If the value is greater than the current node
            return self.__r_contains(current.right, value) # Recursively call the contains method on right chil


    # Helper method to pass in the root as current 
    def r_contains(self, value):
        return self.__r_contains(self.root, value)


my_tree = BinarySearchTree() # Create an instance of BST the class
my_tree.r_insert(47)
my_tree.r_insert(21)
my_tree.r_insert(76)
my_tree.r_insert(18)
my_tree.r_insert(27)
my_tree.r_insert(52)
my_tree.r_insert(82)

print('BST Contains 27: ', my_tree.r_contains(27))
print('BST Contains 17: ', my_tree.r_contains(17))