# Notes for practice code:
    # Create a new node
    # Check for edge case: If the root is empty
    # Create pointer and an infite loop that ends if we return False
    # See if new node is equal to node we are looping on (not allowed) and stop code
    # Then see if the new node is less than the node we are looping on,
        # If so, check if the next spot is open, if it is, place the new node and stop code
        # If the spot is not open, move to the next node
    # Repeat last 3 steps for if the new node is greater than the node we are looping on

# Time complexity for insert:
    # For balanced Binary Search Trees (ensures the height is kept to a minimum relative to the number of nodes) the time complexity of contains is 0(log n) (logarithmic time complexity) which means that the number of operations increases logarithmically with the size of the input. In each iteration the number of operations are halved.
    # An unbalanced Binary Search Tree does not ensure any specific structure, meaning that the height can vary. The worst case, an unbalanced tree can degrade into a structure that resembles a linked list which would make the time complexity 0(n) (linear time complexity) and the input is equal to the number of operations

class Node:
    def __init__(self, value):
        self.value = value # Each node has a value, 
        self.left = None # Something pointing the left (child)
        self.right = None # and something pointing to the right (other child)

class BinarySearchTree:
    def __init__(self):
        self.root = None # Point the root to None, a placeholder for the top of the tree

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




my_tree = BinarySearchTree() # Create an instance of the class
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)

print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)