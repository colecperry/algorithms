# Notes for practice coding:
    # Check if root is none - edge case - if so, stop code
    # Set pointer equal to the root
    # Create a loop
    # If the value we are looking for is greater than the node we are looping on, go right
    # If the value we are looking for is less than the node we are looping on, go left
    # Else, the only other option is that it is equal, stop code
    # If we go all the way through the code and don't get a match, stop code

# Time complexity for contains:
    # For balanced Binary Search Trees (ensures the height is kept to a minimum relative to the number of nodes) the time complexity of contains is 0(log n) (logarithmic time complexity) which means that the number of operations increases logarithmically with the size of the input. In each iteration the number of operations are halved
    # An unbalanced Binary Search Tree does not ensure any specific structure, meaning that the height can vary. The worst case, an unbalanced tree can degrade into a structure that resembles a linked list which would make the time complexity 0(n) (linear time complexity) and the input is equal to the number of operations

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

    def contains(self, value):
        if self.root == None: # If the tree is empty
            return False # Return False to stop the loop
        temp = self.root # Set a variable "temp" equal to the root
        while temp: # Create a loop that runs as long as temp is equal to a val
            if value < temp.value: # If the value we are looking for is less than the value
                # of the node we are iterating on
                temp = temp.left # Move the "temp" variable down and to the left
            elif temp.value > value: # If the value we are looking for is greater than the
                # value of the node we are iterating on
                temp = temp.right # Move the "temp" variable down and to the right
            else: # The only possibility left is that it is equal
                return True # In that case, return True
        return False # If we break out of the while loop (when temp hits None), we did not
        # find our value, and we return False

my_tree = BinarySearchTree(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.contains(27))
print(my_tree.contains(17))
