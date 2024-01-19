class Node:
    def __init__(self, value):
        self.value = value # Each node has a value, 
        self.left = None # Something pointing the left (child)
        self.right = None # and something pointing to the right (other child)

class BinarySearchTree:
    def __init__(self, value):
        new_node = Node(value) # Create a new node
        self.root = new_node # Point the root, or top of the tree to the created node

        # Note - you could also point the root to none, and add a node later with the
        # insert method. You also would not initialize a new node in the Binary Tree init

    def insert(self, value):
        new_node = Node(value) # Create a new node
        if self.root == None: # Edge Case: If our tree is empty,
            self.root = new_node # set the root to the newly created node
            return True # If above is equal, return True because we want to stop the code
        temp = self.root # Set a variable "temp" to the root
        while (True): # Create an infinite loop that continues until a "return" statement
            # is encountered
            if new_node.value == temp.value: # If the newly created node's value is equal
                # to the node's value we are iterating on,
                return False # Return false because you can't have to == values in a tree
            if new_node.value < temp.value: # If the newly created node's value is less
                # than the value of the node we are iterating through,
                if temp.left is None: # Check if there is an open spot to the left
                    temp.left = new_node # Set that open spot to the new node
                    return True # Return True to stop additional code from running
                else: # If there isn't a spot open to the left,
                    temp = temp.left # Move the temp pointer down to the left, then re-run
                    # the loop until you find an open spot
            else: # If the newly created node's value is greater than the value of temp
                if temp.right is None: # Check if there is an open spot to the right
                    temp.right = new_node # Set the open spot to the right
                    return True # Stop additional code from running
                else: # If there isn't an open spot to the right,
                    temp = temp.right # Move the temp pointer down to the right, then
                    # re-run the loop until you find an open spot




my_tree = BinarySearchTree(2) # Create an instance of the class
my_tree.insert(1)
my_tree.insert(3)

print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)