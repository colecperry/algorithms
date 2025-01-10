# Part 1: Start at the root, and traverse to the root
# Part 2: Once we find the node, we need to delete it
    # Leaf node is simplest scenario (bottom level) -> no children
    # If we have nodes with only left or right child, you can delete the parent and move the child up
    # If we have nodes on each side, look at the subtree on the right's children, find the node with the lowest value, and copy the value into the node we are going to delete. Then we delete the right child's lowest node

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

    def __delete_node(self, current, value):
        if current == None: # Base case when the 
            return None
        # Traverse until you either find or don't find the value
        if value < current.value: # If the value we are looking for is less than the value in the current node
            current.left = self.__delete_node(current.left, value) # Call delete recursively on the left node, set the return value to current.left
        elif value > current.value: # If the value we are looking for is more than the value in the current node
            current.right = self.__delete_node(current.right, value) # Call delete recursively on the right node
        else: # If the node we are on is equal to the value we are looking for
            if current.left == None and current.right == None: # If the node we are removing has no children
                return None # This returns none to current.left or current.right in the recursive chain, removing the node
            elif current.left == None: # If the node we are looking to remove has no left child
                current = current.right # Move current pointer to the right, when we return current to the previous call stack, it sets current.left to the right child value, moving it up one level
            elif current.right == None: # If the node we are looking to remove has no right child
                current = current.left # Move current pointer to the left
            else: # If the node we are looking to remove has two children
                sub_tree_min = self.min_value(current.right) # Look at subtree on the right and find min value
                current.value = sub_tree_min # Swap the value at current node (one we are deleting) with min
                current.right = self.__delete_node(current.right, sub_tree_min) # traverse to the node to delete


        return current # Return the current node to the previous call stack
    
    # Helper value findmin to help with delete function (when parent has two leaf nodes) - keep moving left until we reach none
    def min_value(self, current):
        while current.left is not None:
            current = current.left
        return current.value # Return the value not the node


    # Helper method that calls __delete_node with the root passed in as current
    def delete_node(self, value):
        self.root = self.__delete_node(self.root, value)



my_tree = BinarySearchTree()
my_tree.r_insert(2)
my_tree.r_insert(1)
my_tree.r_insert(3)

print("Before deleting: ")
print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)

my_tree.delete_node(2)

print("After deleting: ")
print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right)


