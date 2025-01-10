#             47
#            /   \
#           /     \
#          21     76
#         /  \   /  \
#        18  27 52  82
# Breadth first tree traversal: Visit each node from each row left to right, and down the tree - 47, 21, 76, 18, 27, 52, 82
# Depth first tree traversal: Start at the bottom left, visit parent, visit other child, move up to parent's parent, then visit right side of the tree's left bottom child, visit parent, and then visit other child - 18, 21, 27, 47, 52, 76, 82

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
    
    def BFS(self):
        current = self.root # Create a current pointer
        queue = [] # Create an empty queue as a list
        results = [] # Create an empty results list
        queue.append(current) # Append the current node to the queue to start
        while len(queue) > 0: # Run a while loop as long as there are items in the queue
            current = queue.pop(0) # Pop the first item off the queue and assign to current 
            results.append(current.value) # Append current's value to the results list
            if current.left is not None: # If there is a node to the left of current
                queue.append(current.left) # Append it to the queue
            if current.right is not None: # Repeat for the right node
                queue.append(current.right)
        return results # Return the BFS List of nodes


my_tree = BinarySearchTree() # Create an instance of the class
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.BFS())

# [47, 21, 76, 18, 27, 52, 82]
