#             47
#            /   \
#           /     \
#          21     76
#         /  \   /  \
#        18  27 52  82

# Depth first tree traversal
# Pre Order: Move to the left as far as you can while adding each node to the result as you visit them. Once you reach the end come back up to the parent node and go to the right, go back up to root node, go left first, come back to parent, go right -> 47, 21, 18, 27, 76, 52, 82

# Post Order: Move to the left as far as you can, if there are no children nodes, add the result to the list, then come back up to the parent and go right -> 18, 27, 21, 52, 82, 76, 47

# In Order: Move left as far as you can until you reach 18. From 18, try to go left, add the result to the list, then go right. Then go back to the parent (21) and go right (since you already went left). Try to go left, add value, try to go right. -> 18, 21, 27, 47, 52, 76, 82

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

    def dfs_pre_order(self):
        results = []

        def traverse(current): # Function inside of a function, pass traverse a node

            results.append(current.value) # Append current node's value to the list
            if current.left is not None: # If there is a node on the left
                traverse(current.left) # Run traverse on the left
            if current.right is not None: # If there is a node on the right
                traverse(current.right) # Run traverse on the right

        traverse(self.root) # Call the function with the root, and push an instance onto call stack
        return results
    
    
    def dfs_post_order(self):
        results = []

        def traverse(current): # Function inside of a function, pass traverse a node
            if current.left is not None: # If there is a node on the left
                traverse(current.left) # Run traverse on the left
            if current.right is not None: # If there is a node on the right
                traverse(current.right) # Run traverse on the right
            results.append(current.value) # Append current node's value to the list
        
        traverse(self.root) # Call the function with the root, and push an instance onto call stack
        return results
    
    def dfs_in_order(self):
        results = []

        def traverse(current): # Function inside of a function, pass traverse a node
            if current.left is not None: # If there is a node on the left
                traverse(current.left) # Run traverse on the left
            results.append(current.value) # Append current node's value to the list
            if current.right is not None: # If there is a node on the right
                traverse(current.right) # Run traverse on the right
        
        traverse(self.root) # Call the function with the root, and push an instance onto call stack
        return results




my_tree = BinarySearchTree() # Create an instance of the class
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.dfs_pre_order())
# [47, 21, 18, 27, 76, 52, 82]

print(my_tree.dfs_post_order())
# [18, 27, 21, 52, 82, 76, 47]

print(my_tree.dfs_in_order())
# [18, 21, 27, 47, 52, 76, 82]



