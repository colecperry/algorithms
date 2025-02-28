# The in-order successor of a node is the next node in the in-order traversal of the BST (left -> root -> right) which is the smallest node greater than the given node
# Case 1: If the node has a right subtree
    # The succcessor is the smallest node in the right subtree
        # Steps: 
            # If node.right exists, move to node.right
            # From there, keep going left until there are no more left children
            # The last node you reach is the successor
# Case 2: The node has NO right subtree
    # We need to move upward in the tree, the first ancestor is where the node is the left subtree (direct parent) or is in the left subtree (if we move up higher than parent)
        # Steps:
            # Start moving up the tree using a pointer
            # Stop at the first ancestor where the node is a left child

class Node:
    def __init__(self, value):
        self.value = value  # Each node has a value
        self.left = None  # Pointer to left child
        self.right = None  # Pointer to right child
        self.parent = None  # Pointer to parent (needed for successor function)

class BinarySearchTree:
    def __init__(self):
        self.root = None  # Initialize root to None

    def __r_insert(self, current, value, parent=None):
        """ Recursively inserts a value into the BST while maintaining parent links. """
        if current is None:  # Base case
            new_node = Node(value)
            new_node.parent = parent  # Set parent reference
            return new_node
        if value < current.value:  # If value is smaller, go left
            current.left = self.__r_insert(current.left, value, current)
        elif value > current.value:  # If value is larger, go right
            current.right = self.__r_insert(current.right, value, current)
        return current  # Duplicates will just return

    def r_insert(self, value):
        """ Public insert method to handle the empty tree case. """
        if self.root is None:  # If tree is empty, set root
            self.root = Node(value)
        else:
            self.__r_insert(self.root, value)

    def __r_contains(self, current, value):
        """ Recursively checks if a value exists in the BST. """
        if current is None:
            return False  # Value not found
        if value == current.value:
            return current  # Return the node (not just True) to use for successor function
        if value < current.value:
            return self.__r_contains(current.left, value)  # Search left
        return self.__r_contains(current.right, value)  # Search right

    def r_contains(self, value):
        """ Public method to check if the tree contains a value and return the node. """
        return self.__r_contains(self.root, value)

    def find_min(self, node=None):
        """ Returns the node with the smallest value in the BST or subtree. """
        current = node if node else self.root  # If a node is given, find min in its subtree
        while current and current.left:
            current = current.left  # Keep going left
        return current

    def find_max(self):
        """ Returns the node with the largest value in the BST. """
        current = self.root
        while current and current.right:
            current = current.right  # Keep going right
        return current

    def find_successor(self, node):
        """
        Finds the in-order successor of a given node in the BST.
        The successor is the next node in an in-order traversal.
        """
        if node.right:  # Case 1: If node has a right subtree
            return self.find_min(node.right)  # Find min in right subtree

        # Case 2: No right subtree, move up to the first ancestor where node is in the left subtree
        y = node.parent
        while y is not None and node == y.right:
            node = y
            y = y.parent
        return y


# =========================
# 🔹 Example Usage
# =========================
my_tree = BinarySearchTree()  # Create a BST instance

# Insert nodes
my_tree.r_insert(47)
my_tree.r_insert(21)
my_tree.r_insert(76)
my_tree.r_insert(18)
my_tree.r_insert(27)
my_tree.r_insert(52)
my_tree.r_insert(82)

#             47
#           /   \
#          /     \
#         21     76
#        /  \   /  \
#       18  27 52  82

# Search for values
print('BST Contains 27:', my_tree.r_contains(27) is not None)  # ✅ True
print('BST Contains 17:', my_tree.r_contains(17) is not None)  # ❌ False

# Find Min & Max
min_node = my_tree.find_min()
max_node = my_tree.find_max()

print('Minimum value in BST:', min_node.value if min_node else "Tree is empty")  # Expected: 18
print('Maximum value in BST:', max_node.value if max_node else "Tree is empty")  # Expected: 82

# Find Successor
node_27 = my_tree.r_contains(27)
successor_27 = my_tree.find_successor(node_27) if node_27 else None
print(f'Successor of 27: {successor_27.value if successor_27 else "None"}')  # Expected: 47

node_52 = my_tree.r_contains(52)
successor_52 = my_tree.find_successor(node_52) if node_52 else None
print(f'Successor of 52: {successor_52.value if successor_52 else "None"}')  # Expected: 76
